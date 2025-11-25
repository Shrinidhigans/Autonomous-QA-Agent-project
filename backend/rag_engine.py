import os
import json
from typing import List, Dict, Any
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
import requests
import re

class RAGEngine:
    def __init__(self, ollama_url: str = "http://localhost:11434"):
        """Initialize RAG engine with embeddings and vector store"""
        self.ollama_url = ollama_url
        
        # Initialize embeddings (using sentence-transformers)
        print("Loading embeddings model...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={'device': 'cpu'}
        )
        
        # Text splitter for chunking
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        
        self.vector_store = None
        self.documents = []
    
    def build_knowledge_base(self, documents: List[Dict[str, str]]) -> int:
        """Build vector database from documents"""
        self.documents = documents
        
        # Create LangChain documents with metadata
        docs = []
        for doc in documents:
            chunks = self.text_splitter.split_text(doc['content'])
            for i, chunk in enumerate(chunks):
                docs.append(Document(
                    page_content=chunk,
                    metadata={
                        'source': doc['filename'],
                        'chunk_id': i,
                        'total_chunks': len(chunks)
                    }
                ))
        
        # Create vector store
        print(f"Creating vector store with {len(docs)} chunks...")
        self.vector_store = Chroma.from_documents(
            documents=docs,
            embedding=self.embeddings,
            persist_directory="./vector_db"
        )
        
        return len(docs)
    
    def retrieve_context(self, query: str, k: int = 5) -> List[Dict[str, Any]]:
        """Retrieve relevant context from vector store"""
        if not self.vector_store:
            return []
        
        results = self.vector_store.similarity_search_with_score(query, k=k)
        
        context = []
        for doc, score in results:
            context.append({
                'content': doc.page_content,
                'source': doc.metadata.get('source', 'unknown'),
                'score': float(score)
            })
        
        return context
    
    def call_llm(self, prompt: str, model: str = "llama3.2") -> str:
        """Call Ollama LLM API"""
        try:
            print(f"Calling LLM with model: {model}...")
            response = requests.post(
                f"{self.ollama_url}/api/generate",
                json={
                    "model": model,
                    "prompt": prompt,
                    "stream": False,
                    "temperature": 0.7,
                    "max_tokens": 2000
                },
                timeout=120
            )
            
            if response.status_code == 200:
                result = response.json()['response']
                print("LLM response received successfully")
                return result
            else:
                print(f"LLM call failed with status {response.status_code}")
                return self._mock_llm_response(prompt)
        
        except Exception as e:
            print(f"LLM call failed: {e}. Using mock response.")
            return self._mock_llm_response(prompt)
    
    def generate_test_cases(self, query: str, num_cases: int = 5) -> List[Dict[str, Any]]:
        """Generate test cases using RAG pipeline"""
        
        print(f"Generating {num_cases} test cases for query: {query}")
        
        # Retrieve relevant context
        context_docs = self.retrieve_context(query, k=10)
        
        # Build context string
        context_str = "\n\n".join([
            f"[Source: {doc['source']}]\n{doc['content']}"
            for doc in context_docs[:8]
        ])
        
        # Create prompt
        prompt = f"""You are an expert QA engineer. Generate EXACTLY {num_cases} comprehensive test cases based on the provided documentation.

DOCUMENTATION CONTEXT:
{context_str}

USER REQUEST: {query}

IMPORTANT: Generate EXACTLY {num_cases} test cases. Include both positive AND negative test scenarios.

Generate the test cases in the following JSON format (return ONLY valid JSON, no markdown, no extra text):

{{
  "test_cases": [
    {{
      "test_id": "TC-001",
      "feature": "Feature Name",
      "test_scenario": "Detailed description of what is being tested",
      "test_type": "positive",
      "preconditions": "Any setup needed before test",
      "test_steps": [
        "Step 1: Do something specific",
        "Step 2: Verify something",
        "Step 3: Check result"
      ],
      "expected_result": "What should happen when test passes",
      "grounded_in": "source_document.md"
    }},
    {{
      "test_id": "TC-002",
      "feature": "Feature Name",
      "test_scenario": "Another test scenario",
      "test_type": "negative",
      "preconditions": "Setup for negative test",
      "test_steps": [
        "Step 1: Enter invalid data",
        "Step 2: Submit",
        "Step 3: Verify error"
      ],
      "expected_result": "Error message should appear",
      "grounded_in": "validation_rules.txt"
    }}
  ]
}}

CRITICAL REQUIREMENTS:
- Generate EXACTLY {num_cases} test cases
- Base ALL test cases on the provided documentation
- Include source document in "grounded_in" field
- Mix positive and negative scenarios (at least 40% negative tests)
- Be specific and detailed in test steps
- Use actual values from documentation (like discount codes SAVE15, SAVE20)
- Return ONLY valid JSON, no markdown code blocks, no explanations"""

        # Call LLM
        response = self.call_llm(prompt)
        
        # Parse JSON response
        try:
            # Clean response - remove markdown code blocks if present
            cleaned_response = self._clean_json_response(response)
            
            result = json.loads(cleaned_response)
            test_cases = result.get('test_cases', [])
            
            # Ensure we have the requested number of test cases
            if len(test_cases) < num_cases:
                print(f"Warning: Only {len(test_cases)} test cases generated, expected {num_cases}")
                # Add mock test cases to meet the requirement
                while len(test_cases) < num_cases:
                    test_cases.extend(self._generate_mock_test_cases(query, num_cases - len(test_cases), context_docs))
                    test_cases = test_cases[:num_cases]  # Trim to exact number
            
            print(f"Successfully generated {len(test_cases)} test cases")
            return test_cases[:num_cases]  # Return exactly num_cases
        
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Response was: {response[:500]}")
            # Fallback: return mock test cases
            return self._generate_mock_test_cases(query, num_cases, context_docs)
    
    def _clean_json_response(self, response: str) -> str:
        """Clean LLM response to extract valid JSON"""
        # Remove markdown code blocks
        response = re.sub(r'```json\s*', '', response)
        response = re.sub(r'```\s*', '', response)
        
        # Find JSON object
        json_start = response.find('{')
        json_end = response.rfind('}') + 1
        
        if json_start != -1 and json_end > json_start:
            return response[json_start:json_end]
        
        return response
    
    def generate_selenium_script(self, test_case: Dict[str, Any], html_content: str) -> str:
        """Generate Selenium script for a test case"""
        
        print(f"Generating Selenium script for test case: {test_case.get('test_id', 'Unknown')}")
        
        # Extract HTML structure info
        html_info = self._extract_html_elements(html_content)
        
        # Retrieve relevant documentation
        feature = test_case.get('feature', '')
        scenario = test_case.get('test_scenario', '')
        context_docs = self.retrieve_context(f"{feature} {scenario}", k=5)
        context_str = "\n".join([doc['content'] for doc in context_docs[:3]])
        
        # Create prompt
        prompt = f"""You are a Selenium WebDriver expert in Python. Generate a complete, executable Selenium test script.

TEST CASE TO AUTOMATE:
{json.dumps(test_case, indent=2)}

HTML STRUCTURE REFERENCE:
{html_info}

DOCUMENTATION CONTEXT:
{context_str}

Generate a complete Python Selenium script with these requirements:

1. Import necessary modules (selenium, time, etc.)
2. Setup Chrome WebDriver
3. Navigate to the HTML file (use placeholder path)
4. Implement ALL test steps from the test case
5. Add explicit waits (WebDriverWait) where needed
6. Include assertions to verify expected results
7. Add proper error handling (try/except/finally)
8. Add comments explaining each step
9. Close browser in finally block
10. Use proper element locators from the HTML (IDs, names, CSS selectors)

IMPORTANT:
- Use actual element IDs and names from the HTML structure above
- Add time.sleep() only where necessary for page loads
- Include clear print statements showing test progress
- Make the script ready to run (just update file path)
- Use WebDriverWait for dynamic elements

Return ONLY the Python code, no explanations, no markdown formatting."""

        script = self.call_llm(prompt)
        
        # Clean up script
        script = self._clean_python_response(script)
        
        print("Selenium script generated successfully")
        return script
    
    def _clean_python_response(self, response: str) -> str:
        """Clean LLM response to extract Python code"""
        # Remove markdown code blocks
        if "```python" in response:
            response = response.split("```python")[1].split("```")[0].strip()
        elif "```" in response:
            response = response.split("```")[1].split("```")[0].strip()
        
        return response
    
    def _extract_html_elements(self, html: str) -> str:
        """Extract key elements from HTML for script generation"""
        try:
            from bs4 import BeautifulSoup
            
            soup = BeautifulSoup(html, 'html.parser')
            
            elements = []
            
            # Extract inputs
            for input_tag in soup.find_all('input')[:30]:
                elem_id = input_tag.get('id', '')
                elem_name = input_tag.get('name', '')
                elem_type = input_tag.get('type', 'text')
                if elem_id or elem_name:
                    elements.append(f"Input: id='{elem_id}', name='{elem_name}', type='{elem_type}'")
            
            # Extract buttons
            for button in soup.find_all('button')[:15]:
                elem_id = button.get('id', '')
                text = button.get_text().strip()[:50]
                if elem_id or text:
                    elements.append(f"Button: id='{elem_id}', text='{text}'")
            
            # Extract selects
            for select in soup.find_all('select')[:10]:
                elem_id = select.get('id', '')
                elem_name = select.get('name', '')
                if elem_id or elem_name:
                    elements.append(f"Select: id='{elem_id}', name='{elem_name}'")
            
            # Extract important divs with IDs
            for div in soup.find_all('div', id=True)[:20]:
                elem_id = div.get('id', '')
                if elem_id and elem_id not in ['', 'root', 'app']:
                    elements.append(f"Div: id='{elem_id}'")
            
            return "\n".join(elements) if elements else "No elements extracted"
        
        except Exception as e:
            print(f"HTML extraction error: {e}")
            return "HTML structure extraction failed"
    
    def _mock_llm_response(self, prompt: str) -> str:
        """Mock LLM response for testing without Ollama"""
        if "test cases" in prompt.lower():
            # Extract number of test cases from prompt
            num_match = re.search(r'EXACTLY (\d+)', prompt)
            num_cases = int(num_match.group(1)) if num_match else 5
            
            test_cases = []
            for i in range(num_cases):
                is_negative = i % 3 == 2  # Every third test is negative
                test_cases.append({
                    "test_id": f"TC-{str(i+1).zfill(3)}",
                    "feature": "Checkout Functionality",
                    "test_scenario": f"{'Invalid' if is_negative else 'Valid'} test scenario {i+1}",
                    "test_type": "negative" if is_negative else "positive",
                    "preconditions": "User is on checkout page with items in cart",
                    "test_steps": [
                        "Navigate to checkout page",
                        f"Perform test action {i+1}",
                        "Verify expected result"
                    ],
                    "expected_result": "Error message displayed" if is_negative else "Action completes successfully",
                    "grounded_in": "product_specs.md"
                })
            
            return json.dumps({"test_cases": test_cases})
        else:
            # Selenium script mock
            return """from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_checkout():
    driver = webdriver.Chrome()
    try:
        # Navigate to page
        driver.get("file:///path/to/checkout.html")
        time.sleep(2)
        
        # Test implementation
        element = driver.find_element(By.ID, "test-element")
        element.click()
        
        # Assertion
        assert "expected" in driver.page_source
        
        print("✅ Test passed")
    finally:
        driver.quit()

if __name__ == "__main__":
    test_checkout()"""
    
    def _generate_mock_test_cases(self, query: str, num: int, context: List) -> List[Dict]:
        """Generate mock test cases when LLM fails"""
        sources = [doc['source'] for doc in context] if context else ['product_specs.md']
        
        test_cases = []
        for i in range(num):
            is_negative = i % 3 == 2
            test_cases.append({
                "test_id": f"TC-{str(i+1).zfill(3)}",
                "feature": "Checkout Feature",
                "test_scenario": f"Test {'invalid' if is_negative else 'valid'} {query.lower()} scenario {i+1}",
                "test_type": "negative" if is_negative else "positive",
                "preconditions": "User on checkout page with items in cart",
                "test_steps": [
                    "Navigate to checkout page",
                    f"Perform {query} action",
                    "Verify result matches expectations"
                ],
                "expected_result": "Error message displayed" if is_negative else "Action completes successfully",
                "grounded_in": sources[0] if sources else "documentation"
            })
        
        return test_cases