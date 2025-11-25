import json
from typing import Dict, List
from bs4 import BeautifulSoup
import pymupdf  # PyMuPDF for PDF processing

class DocumentProcessor:
    def __init__(self):
        self.documents = []
        self.html_content = ""
    
    def process_file(self, content: bytes, filename: str) -> str:
        """Process a file and extract text content"""
        
        if filename.endswith('.md') or filename.endswith('.txt'):
            text = content.decode('utf-8')
        
        elif filename.endswith('.json'):
            text = self._process_json(content)
        
        elif filename.endswith('.pdf'):
            text = self._process_pdf(content)
        
        elif filename.endswith('.html'):
            text = self._process_html(content)
        
        else:
            # Try to decode as text
            try:
                text = content.decode('utf-8')
            except:
                text = str(content)
        
        # Store document
        self.documents.append({
            'filename': filename,
            'content': text
        })
        
        return text
    
    def set_html_content(self, html: str):
        """Store HTML content separately"""
        self.html_content = html
        
        # Also add to documents
        self.documents.append({
            'filename': 'checkout.html',
            'content': self._extract_html_features(html)
        })
    
    def _process_json(self, content: bytes) -> str:
        """Convert JSON to readable text"""
        try:
            data = json.loads(content.decode('utf-8'))
            return json.dumps(data, indent=2)
        except:
            return content.decode('utf-8')
    
    def _process_pdf(self, content: bytes) -> str:
        """Extract text from PDF"""
        try:
            # Create a PDF document from bytes
            pdf = pymupdf.open(stream=content, filetype="pdf")
            text = ""
            
            for page in pdf:
                text += page.get_text()
            
            pdf.close()
            return text
        
        except Exception as e:
            print(f"PDF processing error: {e}")
            return f"PDF content (processing error: {e})"
    
    def _process_html(self, content: bytes) -> str:
        """Extract meaningful text from HTML"""
        html = content.decode('utf-8')
        return self._extract_html_features(html)
    
    def _extract_html_features(self, html: str) -> str:
        """Extract features and structure from HTML"""
        soup = BeautifulSoup(html, 'html.parser')
        
        features = []
        
        # Extract title
        title = soup.find('title')
        if title:
            features.append(f"Page Title: {title.get_text()}")
        
        # Extract forms
        forms = soup.find_all('form')
        for i, form in enumerate(forms):
            features.append(f"\nForm {i+1}:")
            
            # Form inputs
            inputs = form.find_all('input')
            for inp in inputs:
                input_type = inp.get('type', 'text')
                input_id = inp.get('id', '')
                input_name = inp.get('name', '')
                features.append(f"  - Input: type={input_type}, id={input_id}, name={input_name}")
        
        # Extract buttons
        buttons = soup.find_all('button')
        features.append(f"\nButtons:")
        for btn in buttons:
            btn_id = btn.get('id', '')
            btn_text = btn.get_text().strip()
            features.append(f"  - Button: id={btn_id}, text='{btn_text}'")
        
        # Extract interactive elements
        selects = soup.find_all('select')
        if selects:
            features.append(f"\nSelect Elements:")
            for sel in selects:
                sel_id = sel.get('id', '')
                sel_name = sel.get('name', '')
                features.append(f"  - Select: id={sel_id}, name={sel_name}")
        
        # Extract text content (headers, paragraphs)
        headers = soup.find_all(['h1', 'h2', 'h3'])
        if headers:
            features.append(f"\nPage Headers:")
            for h in headers:
                features.append(f"  - {h.name}: {h.get_text().strip()}")
        
        return "\n".join(features)
    
    def get_all_documents(self) -> List[Dict[str, str]]:
        """Return all processed documents"""
        return self.documents
    
    def clear(self):
        """Clear all stored documents"""
        self.documents = []
        self.html_content = ""