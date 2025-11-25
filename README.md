# Autonomous QA Agent for Test Case and Script Generation

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An intelligent, autonomous QA agent that constructs a "testing brain" from project documentation using RAG (Retrieval-Augmented Generation) technology. The system generates comprehensive test cases and executable Selenium Python scripts, all grounded strictly in provided documentation.

---

## 🎯 Features

- **📚 Knowledge Base Ingestion**: Processes multiple document formats (MD, TXT, JSON, PDF, HTML)
- **🧠 RAG-Powered Intelligence**: Uses vector embeddings for semantic document search
- **🧪 Test Case Generation**: Creates comprehensive, documentation-grounded test plans
- **💻 Selenium Script Generation**: Produces executable Python Selenium scripts with proper selectors
- **🚀 FastAPI Backend**: RESTful API for all operations
- **🎨 Streamlit UI**: Intuitive web interface for easy interaction
- **✅ Zero Hallucinations**: All test cases strictly reference provided documentation

---

## 📋 Table of Contents

- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage Guide](#-usage-guide)
- [API Documentation](#-api-documentation)
- [Support Documents](#-support-documents-included)
- [Configuration](#-configuration)
- [Testing](#-testing)
- [Troubleshooting](#-troubleshooting)
---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager
- (Optional) Ollama for LLM functionality ([Install Ollama](https://ollama.ai))

### Installation (5 minutes)

```bash
# 1. Clone the repository
git clone Autonomous QA Agent for Test Case and Script Generation
Python 3.9+ FastAPI Streamlit License: MIT

An intelligent, autonomous QA agent that constructs a "testing brain" from project documentation using RAG (Retrieval-Augmented Generation) technology. The system generates comprehensive test cases and executable Selenium Python scripts, all grounded strictly in provided documentation.

🎯 Features
📚 Knowledge Base Ingestion: Processes multiple document formats (MD, TXT, JSON, PDF, HTML)
🧠 RAG-Powered Intelligence: Uses vector embeddings for semantic document search
🧪 Test Case Generation: Creates comprehensive, documentation-grounded test plans
💻 Selenium Script Generation: Produces executable Python Selenium scripts with proper selectors
🚀 FastAPI Backend: RESTful API for all operations
🎨 Streamlit UI: Intuitive web interface for easy interaction
✅ Zero Hallucinations: All test cases strictly reference provided documentation
📋 Table of Contents
Quick Start
Project Structure
Installation
Usage Guide
API Documentation
Support Documents
Configuration
Testing
Troubleshooting
Demo Video
🚀 Quick Start
Prerequisites
Python 3.9 or higher
pip package manager
(Optional) Ollama for LLM functionality (Install Ollama)
Installation (5 minutes)
# 1. Clone the repository
git clone Autonomous QA Agent for Test Case and Script Generation
Python 3.9+ FastAPI Streamlit License: MIT

An intelligent, autonomous QA agent that constructs a "testing brain" from project documentation using RAG (Retrieval-Augmented Generation) technology. The system generates comprehensive test cases and executable Selenium Python scripts, all grounded strictly in provided documentation.

🎯 Features
📚 Knowledge Base Ingestion: Processes multiple document formats (MD, TXT, JSON, PDF, HTML)
🧠 RAG-Powered Intelligence: Uses vector embeddings for semantic document search
🧪 Test Case Generation: Creates comprehensive, documentation-grounded test plans
💻 Selenium Script Generation: Produces executable Python Selenium scripts with proper selectors
🚀 FastAPI Backend: RESTful API for all operations
🎨 Streamlit UI: Intuitive web interface for easy interaction
✅ Zero Hallucinations: All test cases strictly reference provided documentation
📋 Table of Contents
Quick Start
Project Structure
Installation
Usage Guide
API Documentation
Support Documents
Configuration
Testing
Troubleshooting
Demo Video
🚀 Quick Start
Prerequisites
Python 3.9 or higher
pip package manager
(Optional) Ollama for LLM functionality (Install Ollama)
Installation (5 minutes)
# 1. Clone the repository
git clone [https://github.com/Shrinidhigans/Autonomous-QA-Agent-project]
cd qa-agent-project

# 2. Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Install and start Ollama
# Download from https://ollama.ai
# Pull a model:
ollama pull llama3.2
Running the Application
# Terminal 1: Start FastAPI Backend
uvicorn backend.main:app --reload

# Terminal 2: Start Streamlit UI
streamlit run frontend/streamlit_app.py
The application will open automatically in your browser at http://localhost:8501

📁 Project Structure
qa-agent-project/
│
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── rag_engine.py          # RAG pipeline with LLM integration
│   ├── document_processor.py  # Document parsing (MD, TXT, JSON, PDF, HTML)
│   └── vector_store.py        # ChromaDB vector database (auto-created)
│
├── frontend/
│   └── streamlit_app.py       # Streamlit web interface
│
├── assets/
│   ├── checkout.html          # Sample e-commerce checkout page
│   └── support_docs/
│       ├── product_specs.md       # Product specifications
│       ├── ui_ux_guide.txt        # UI/UX design guidelines
│       ├── api_endpoints.json     # API documentation
│       ├── test_strategy.md       # Testing strategy
│       └── validation_rules.txt   # Validation specifications
│
├── generated/                  # Auto-created directories
│   ├── test_cases/            # Generated test case JSON files
│   └── selenium_scripts/      # Generated Python scripts
│
├── vector_db/                 # ChromaDB storage (auto-created)
│
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .gitignore                 # Git ignore rules
└── demo_video.md             # Demo video guide

💿 Installation
Step-by-Step Installation
1. System Requirements
Operating System: Windows 10/11, macOS 10.15+, or Linux
Python: Version 3.9, 3.10, or 3.11
RAM: Minimum 8GB (16GB recommended)
Storage: 2GB free space
2. Clone Repository
git clone https://github.com/yourusername/qa-agent-project.git
cd qa-agent-project
3. Create Virtual Environment
# Using venv (recommended)
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
4. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt
This installs:

FastAPI & Uvicorn (web framework)
Streamlit (UI)
LangChain (RAG framework)
ChromaDB (vector database)
Sentence Transformers (embeddings)
BeautifulSoup4 (HTML parsing)
PyMuPDF (PDF processing)
Selenium (for script generation)
And other supporting libraries
5. Verify Installation
python -c "import fastapi, streamlit, langchain, chromadb; print('All packages installed successfully!')"
6. Optional: Install Ollama (for LLM functionality)
The system works with mock responses if Ollama is not installed, but for full functionality:

Download Ollama from https://ollama.ai
Install and start Ollama
Pull a model:
ollama pull llama3.2
📖 Usage Guide
Phase 1: Knowledge Base Ingestion
Start the Backend:

uvicorn backend.main:app --reload
Backend runs at http://localhost:8000

Start the Frontend:

streamlit run frontend/streamlit_app.py
Frontend opens at http://localhost:8501

Upload Documents:

Navigate to "Document Upload" tab
Upload the 5 support documents from assets/support_docs/
Upload assets/checkout.html
Click "Build Knowledge Base"
Wait for processing (creates vector embeddings)
Phase 2: Test Case Generation
Navigate to "Test Case Generation" tab

Enter your query. Examples:

Generate comprehensive test cases for discount code functionality
Create positive and negative test cases for form validation
Generate test cases for shipping method selection
Adjust number of test cases (1-10)

Click "Generate Test Cases"

Review generated test cases:

Each test case shows:
Test ID
Feature being tested
Test scenario description
Test type (positive/negative)
Preconditions
Step-by-step test steps
Expected results
Source documentation reference
Phase 3: Selenium Script Generation
Navigate to "Script Generation" tab

Select a test case from the dropdown

Review test case details

Click "Generate Selenium Script"

Download or copy the script:

Script includes:
Proper imports
WebDriver setup
Element locators matching actual HTML
Test step implementations
Assertions for verification
Error handling
Run the script (example):

# Update the file path in the script first
python generated/selenium_scripts/TC-001_selenium.py
🔌 API Documentation
Backend API Endpoints
Health Check
GET http://localhost:8000/health
Response:

{
  "status": "healthy",
  "knowledge_base_built": true,
  "html_uploaded": true,
  "num_documents": 6
}
Upload Documents
POST http://localhost:8000/upload_documents
Content-Type: multipart/form-data

files: [file1, file2, ...]
Response:

{
  "status": "success",
  "processed_documents": [
    {
      "filename": "product_specs.md",
      "type": "support_doc",
      "chunks": 15
    }
  ],
  "message": "Uploaded 5 document(s)"
}
Build Knowledge Base
POST http://localhost:8000/build_knowledge_base
Response:

{
  "status": "success",
  "num_documents": 6,
  "num_chunks": 87,
  "message": "Knowledge base built successfully"
}
Generate Test Cases
POST http://localhost:8000/generate_test_cases
Content-Type: application/json

{
  "query": "Generate test cases for discount code",
  "num_cases": 5
}
Response:

{
  "status": "success",
  "test_cases": [
    {
      "test_id": "TC-001",
      "feature": "Discount Code",
      "test_scenario": "Apply valid discount code SAVE15",
      "test_type": "positive",
      "preconditions": "Cart has items",
      "test_steps": [...],
      "expected_result": "15% discount applied",
      "grounded_in": "product_specs.md"
    }
  ],
  "count": 5
}
Generate Selenium Script
POST http://localhost:8000/generate_selenium_script
Content-Type: application/json

{
  "test_case_id": "TC-001",
  "test_case_content": { ... }
}
Response:

{
  "status": "success",
  "test_case_id": "TC-001",
  "script": "from selenium import webdriver..."
}
📚 Support Documents Included
1. product_specs.md (5.2 KB)
Complete product specifications including:

Product catalog (3 products)
Shopping cart functionality
Discount code rules (SAVE15, SAVE20)
Shipping options (Standard FREE, Express $10)
Payment methods (Credit Card, PayPal)
Order calculation logic
Business rules
2. ui_ux_guide.txt (11.8 KB)
Comprehensive UI/UX specifications:

Color palette and gradients
Typography standards
Button specifications
Form element styling
Error message formats
Validation display rules
Accessibility requirements (WCAG 2.1 AA)
3. api_endpoints.json (7.3 KB)
API documentation including:

10 REST endpoints
Request/response formats
Validation rules
Error codes
Rate limiting
Authentication details
4. test_strategy.md (14.1 KB)
Testing strategy document:

Test objectives and metrics
Test types (functional, UI/UX, accessibility)
Test case categories
Automation strategy
Entry/exit criteria
Risk mitigation
5. validation_rules.txt (15.6 KB)
Detailed validation specifications:

Field-by-field validation rules
Email regex patterns
Error message text
Validation timing
Edge cases
Implementation checklist
6. checkout.html (13.2 KB)
Target web application:

E-commerce checkout page
3 products with "Add to Cart"
Shopping cart with quantity controls
Discount code input
Customer details form
Shipping/payment selection
Complete JavaScript functionality
⚙️ Configuration
Environment Variables (Optional)
Create a .env file in the project root:

# LLM Configuration
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Embedding Model
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Vector Database
VECTOR_DB_PATH=./vector_db

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
Customizing RAG Parameters
Edit backend/rag_engine.py:

# Text chunking parameters
self.text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Adjust chunk size
    chunk_overlap=200,      # Adjust overlap
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]
)

# Number of retrieved chunks
context_docs = self.retrieve_context(query, k=8)  # Adjust k value
🧪 Testing
Running the Application
Test Backend:

# Start backend
uvicorn backend.main:app --reload

# In another terminal, test health endpoint
curl http://localhost:8000/health
Test Frontend:

streamlit run frontend/streamlit_app.py
Access at http://localhost:8501

Sample Test Queries
Try these queries in the Test Case Generation tab:

Generate test cases for adding products to cart
Create negative test cases for form validation with invalid email formats
Generate test cases for discount code SAVE15 and SAVE20 application
Create test cases for shipping method selection and cost calculation
Generate boundary test cases for cart quantity limits
🔧 Troubleshooting
Common Issues and Solutions
Issue: "ModuleNotFoundError"
Solution: Ensure virtual environment is activated and dependencies installed

pip install -r requirements.txt
Issue: "Port 8000 already in use"
Solution: Kill the process or use a different port

# Find process
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Use different port
uvicorn backend.main:app --port 8001
Issue: "Ollama connection failed"
Solution: System works with mock responses. For full functionality:

Install Ollama from https://ollama.ai
Start Ollama service
Pull a model: ollama pull llama3.2
Issue: "ChromaDB directory not found"
Solution: Directory is created automatically. Ensure write permissions in project folder.

Issue: "Embeddings download slow"
Solution: First run downloads sentence-transformers model (~90MB). Subsequent runs use cached model.

Issue: "Streamlit shows connection error"
Solution:

Ensure FastAPI backend is running first
Check API_URL in streamlit_app.py matches backend address
Default: http://localhost:8000
🎥 Demo Video
Creating Your Demo Video (5-10 minutes)
Record a demo showing:

Introduction (30 seconds)

Briefly explain the project
Show project structure
Phase 1: Document Upload (2 minutes)

Start backend and frontend
Upload support documents
Upload checkout.html
Click "Build Knowledge Base"
Show success message
Phase 2: Test Case Generation (2-3 minutes)

Enter a test query
Adjust number of test cases
Generate test cases
Review generated test cases
Highlight:
Test case structure
Source document references
Positive and negative scenarios
Phase 3: Script Generation (2-3 minutes)

Select a test case
Generate Selenium script
Review the script code
Show proper element selectors
Demonstrate download functionality
(Optional) Run the script
Conclusion (1 minute)

Recap key features
Mention RAG technology
Highlight zero hallucinations
Screen Recording Tools
Windows: OBS Studio, ShareX
macOS: QuickTime, OBS Studio
Linux: SimpleScreenRecorder, OBS Studio
Online: Loom, Screencast-O-Matic
🏗️ Architecture
System Components
┌─────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                    │
│              (User Interface - Port 8501)                │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP Requests
┌─────────────────────▼───────────────────────────────────┐
│                   FastAPI Backend                        │
│              (REST API - Port 8000)                      │
├──────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌──────────────────────────────┐  │
│  │   Document      │  │      RAG Engine              │  │
│  │   Processor     │─▶│  - Vector Store (Chroma)     │  │
│  │  - MD, TXT      │  │  - Embeddings (HuggingFace)  │  │
│  │  - JSON, PDF    │  │  - LLM Integration (Ollama)  │  │
│  │  - HTML Parser  │  │  - Context Retrieval         │  │
│  └─────────────────┘  └──────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
                      │
         ┌────────────┴───────────────┐
         │                            │
    ┌────▼─────┐              ┌───────▼────────┐
    │ ChromaDB │              │  Ollama LLM    │
    │ (Vector  │              │  (Optional)    │
    │  Store)  │              └────────────────┘
    └──────────┘
Technology Stack
Frontend: Streamlit 1.29
Backend: FastAPI 0.104
RAG Framework: LangChain 0.1
Vector Database: ChromaDB 0.4
Embeddings: Sentence Transformers
LLM: Ollama (llama3.2) or Mock
Document Processing: BeautifulSoup, PyMuPDF
Test Automation: Selenium 4.15
🤝 Contributing
Contributions are welcome! Please:

Fork the repository
Create a feature branch
Make your changes
Submit a pull request
📝 License
This project is licensed under the MIT License.

👥 Authors
Your Name - Initial work
🙏 Acknowledgments
LangChain for RAG framework
Anthropic for Claude AI inspiration
Ollama for local LLM support
ChromaDB for vector storage
Streamlit for beautiful UI framework
📧 Support
For questions or issues:

Open an issue on GitHub
Email: your.email@example.com
🗺️ Roadmap
 Add support for more document formats (DOCX, PPTX)
 Implement test case export to various formats
 Add support for Playwright script generation
 Integrate with CI/CD pipelines
 Add test execution and reporting
 Multi-language support for test cases
 Cloud deployment guide
⭐ If this project helped you, please consider giving it a star on GitHub!

Last Updated: November 25, 2024
cd qa-agent-project

# 2. Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Install and start Ollama
# Download from https://ollama.ai
# Pull a model:
ollama pull llama3.2
Running the Application
# Terminal 1: Start FastAPI Backend
uvicorn backend.main:app --reload

# Terminal 2: Start Streamlit UI
streamlit run frontend/streamlit_app.py
The application will open automatically in your browser at http://localhost:8501

📁 Project Structure
qa-agent-project/
│
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── rag_engine.py          # RAG pipeline with LLM integration
│   ├── document_processor.py  # Document parsing (MD, TXT, JSON, PDF, HTML)
│   └── vector_store.py        # ChromaDB vector database (auto-created)
│
├── frontend/
│   └── streamlit_app.py       # Streamlit web interface
│
├── assets/
│   ├── checkout.html          # Sample e-commerce checkout page
│   └── support_docs/
│       ├── product_specs.md       # Product specifications
│       ├── ui_ux_guide.txt        # UI/UX design guidelines
│       ├── api_endpoints.json     # API documentation
│       ├── test_strategy.md       # Testing strategy
│       └── validation_rules.txt   # Validation specifications
│
├── generated/                  # Auto-created directories
│   ├── test_cases/            # Generated test case JSON files
│   └── selenium_scripts/      # Generated Python scripts
│
├── vector_db/                 # ChromaDB storage (auto-created)
│
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .gitignore                 # Git ignore rules
└── demo_video.md             # Demo video guide

💿 Installation
Step-by-Step Installation
1. System Requirements
Operating System: Windows 10/11, macOS 10.15+, or Linux
Python: Version 3.9, 3.10, or 3.11
RAM: Minimum 8GB (16GB recommended)
Storage: 2GB free space
2. Clone Repository
git clone https://github.com/yourusername/qa-agent-project.git
cd qa-agent-project
3. Create Virtual Environment
# Using venv (recommended)
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
4. Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt
This installs:

FastAPI & Uvicorn (web framework)
Streamlit (UI)
LangChain (RAG framework)
ChromaDB (vector database)
Sentence Transformers (embeddings)
BeautifulSoup4 (HTML parsing)
PyMuPDF (PDF processing)
Selenium (for script generation)
And other supporting libraries
5. Verify Installation
python -c "import fastapi, streamlit, langchain, chromadb; print('All packages installed successfully!')"
6. Optional: Install Ollama (for LLM functionality)
The system works with mock responses if Ollama is not installed, but for full functionality:

Download Ollama from https://ollama.ai
Install and start Ollama
Pull a model:
ollama pull llama3.2
📖 Usage Guide
Phase 1: Knowledge Base Ingestion
Start the Backend:

uvicorn backend.main:app --reload
Backend runs at http://localhost:8000

Start the Frontend:

streamlit run frontend/streamlit_app.py
Frontend opens at http://localhost:8501

Upload Documents:

Navigate to "Document Upload" tab
Upload the 5 support documents from assets/support_docs/
Upload assets/checkout.html
Click "Build Knowledge Base"
Wait for processing (creates vector embeddings)
Phase 2: Test Case Generation
Navigate to "Test Case Generation" tab

Enter your query. Examples:

Generate comprehensive test cases for discount code functionality
Create positive and negative test cases for form validation
Generate test cases for shipping method selection
Adjust number of test cases (1-10)

Click "Generate Test Cases"

Review generated test cases:

Each test case shows:
Test ID
Feature being tested
Test scenario description
Test type (positive/negative)
Preconditions
Step-by-step test steps
Expected results
Source documentation reference
Phase 3: Selenium Script Generation
Navigate to "Script Generation" tab

Select a test case from the dropdown

Review test case details

Click "Generate Selenium Script"

Download or copy the script:

Script includes:
Proper imports
WebDriver setup
Element locators matching actual HTML
Test step implementations
Assertions for verification
Error handling
Run the script (example):

# Update the file path in the script first
python generated/selenium_scripts/TC-001_selenium.py
🔌 API Documentation
Backend API Endpoints
Health Check
GET http://localhost:8000/health
Response:

{
  "status": "healthy",
  "knowledge_base_built": true,
  "html_uploaded": true,
  "num_documents": 6
}
Upload Documents
POST http://localhost:8000/upload_documents
Content-Type: multipart/form-data

files: [file1, file2, ...]
Response:

{
  "status": "success",
  "processed_documents": [
    {
      "filename": "product_specs.md",
      "type": "support_doc",
      "chunks": 15
    }
  ],
  "message": "Uploaded 5 document(s)"
}
Build Knowledge Base
POST http://localhost:8000/build_knowledge_base
Response:

{
  "status": "success",
  "num_documents": 6,
  "num_chunks": 87,
  "message": "Knowledge base built successfully"
}
Generate Test Cases
POST http://localhost:8000/generate_test_cases
Content-Type: application/json

{
  "query": "Generate test cases for discount code",
  "num_cases": 5
}
Response:

{
  "status": "success",
  "test_cases": [
    {
      "test_id": "TC-001",
      "feature": "Discount Code",
      "test_scenario": "Apply valid discount code SAVE15",
      "test_type": "positive",
      "preconditions": "Cart has items",
      "test_steps": [...],
      "expected_result": "15% discount applied",
      "grounded_in": "product_specs.md"
    }
  ],
  "count": 5
}
Generate Selenium Script
POST http://localhost:8000/generate_selenium_script
Content-Type: application/json

{
  "test_case_id": "TC-001",
  "test_case_content": { ... }
}
Response:

{
  "status": "success",
  "test_case_id": "TC-001",
  "script": "from selenium import webdriver..."
}
📚 Support Documents Included
1. product_specs.md (5.2 KB)
Complete product specifications including:

Product catalog (3 products)
Shopping cart functionality
Discount code rules (SAVE15, SAVE20)
Shipping options (Standard FREE, Express $10)
Payment methods (Credit Card, PayPal)
Order calculation logic
Business rules
2. ui_ux_guide.txt (11.8 KB)
Comprehensive UI/UX specifications:

Color palette and gradients
Typography standards
Button specifications
Form element styling
Error message formats
Validation display rules
Accessibility requirements (WCAG 2.1 AA)
3. api_endpoints.json (7.3 KB)
API documentation including:

10 REST endpoints
Request/response formats
Validation rules
Error codes
Rate limiting
Authentication details
4. test_strategy.md (14.1 KB)
Testing strategy document:

Test objectives and metrics
Test types (functional, UI/UX, accessibility)
Test case categories
Automation strategy
Entry/exit criteria
Risk mitigation
5. validation_rules.txt (15.6 KB)
Detailed validation specifications:

Field-by-field validation rules
Email regex patterns
Error message text
Validation timing
Edge cases
Implementation checklist
6. checkout.html (13.2 KB)
Target web application:

E-commerce checkout page
3 products with "Add to Cart"
Shopping cart with quantity controls
Discount code input
Customer details form
Shipping/payment selection
Complete JavaScript functionality
⚙️ Configuration
Environment Variables (Optional)
Create a .env file in the project root:

# LLM Configuration
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Embedding Model
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Vector Database
VECTOR_DB_PATH=./vector_db

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
Customizing RAG Parameters
Edit backend/rag_engine.py:

# Text chunking parameters
self.text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Adjust chunk size
    chunk_overlap=200,      # Adjust overlap
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]
)

# Number of retrieved chunks
context_docs = self.retrieve_context(query, k=8)  # Adjust k value
🧪 Testing
Running the Application
Test Backend:

# Start backend
uvicorn backend.main:app --reload

# In another terminal, test health endpoint
curl http://localhost:8000/health
Test Frontend:

streamlit run frontend/streamlit_app.py
Access at http://localhost:8501

Sample Test Queries
Try these queries in the Test Case Generation tab:

Generate test cases for adding products to cart
Create negative test cases for form validation with invalid email formats
Generate test cases for discount code SAVE15 and SAVE20 application
Create test cases for shipping method selection and cost calculation
Generate boundary test cases for cart quantity limits
🔧 Troubleshooting
Common Issues and Solutions
Issue: "ModuleNotFoundError"
Solution: Ensure virtual environment is activated and dependencies installed

pip install -r requirements.txt
Issue: "Port 8000 already in use"
Solution: Kill the process or use a different port

# Find process
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Use different port
uvicorn backend.main:app --port 8001
Issue: "Ollama connection failed"
Solution: System works with mock responses. For full functionality:

Install Ollama from https://ollama.ai
Start Ollama service
Pull a model: ollama pull llama3.2
Issue: "ChromaDB directory not found"
Solution: Directory is created automatically. Ensure write permissions in project folder.

Issue: "Embeddings download slow"
Solution: First run downloads sentence-transformers model (~90MB). Subsequent runs use cached model.

Issue: "Streamlit shows connection error"
Solution:

Ensure FastAPI backend is running first
Check API_URL in streamlit_app.py matches backend address
Default: http://localhost:8000
🎥 Demo Video
Creating Your Demo Video (5-10 minutes)
Record a demo showing:

Introduction (30 seconds)

Briefly explain the project
Show project structure
Phase 1: Document Upload (2 minutes)

Start backend and frontend
Upload support documents
Upload checkout.html
Click "Build Knowledge Base"
Show success message
Phase 2: Test Case Generation (2-3 minutes)

Enter a test query
Adjust number of test cases
Generate test cases
Review generated test cases
Highlight:
Test case structure
Source document references
Positive and negative scenarios
Phase 3: Script Generation (2-3 minutes)

Select a test case
Generate Selenium script
Review the script code
Show proper element selectors
Demonstrate download functionality
(Optional) Run the script
Conclusion (1 minute)

Recap key features
Mention RAG technology
Highlight zero hallucinations
Screen Recording Tools
Windows: OBS Studio, ShareX
macOS: QuickTime, OBS Studio
Linux: SimpleScreenRecorder, OBS Studio
Online: Loom, Screencast-O-Matic
🏗️ Architecture
System Components
┌─────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                    │
│              (User Interface - Port 8501)                │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP Requests
┌─────────────────────▼───────────────────────────────────┐
│                   FastAPI Backend                        │
│              (REST API - Port 8000)                      │
├──────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌──────────────────────────────┐  │
│  │   Document      │  │      RAG Engine              │  │
│  │   Processor     │─▶│  - Vector Store (Chroma)     │  │
│  │  - MD, TXT      │  │  - Embeddings (HuggingFace)  │  │
│  │  - JSON, PDF    │  │  - LLM Integration (Ollama)  │  │
│  │  - HTML Parser  │  │  - Context Retrieval         │  │
│  └─────────────────┘  └──────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
                      │
         ┌────────────┴───────────────┐
         │                            │
    ┌────▼─────┐              ┌───────▼────────┐
    │ ChromaDB │              │  Ollama LLM    │
    │ (Vector  │              │  (Optional)    │
    │  Store)  │              └────────────────┘
    └──────────┘
Technology Stack
Frontend: Streamlit 1.29
Backend: FastAPI 0.104
RAG Framework: LangChain 0.1
Vector Database: ChromaDB 0.4
Embeddings: Sentence Transformers
LLM: Ollama (llama3.2) or Mock
Document Processing: BeautifulSoup, PyMuPDF
Test Automation: Selenium 4.15
🤝 Contributing
Contributions are welcome! Please:

Fork the repository
Create a feature branch
Make your changes
Submit a pull request
📝 License
This project is licensed under the MIT License.

👥 Authors
Your Name - Initial work
🙏 Acknowledgments
LangChain for RAG framework
Anthropic for Claude AI inspiration
Ollama for local LLM support
ChromaDB for vector storage
Streamlit for beautiful UI framework
📧 Support
For questions or issues:

Open an issue on GitHub
Email: your.email@example.com
🗺️ Roadmap
 Add support for more document formats (DOCX, PPTX)
 Implement test case export to various formats
 Add support for Playwright script generation
 Integrate with CI/CD pipelines
 Add test execution and reporting
 Multi-language support for test cases
 Cloud deployment guide
⭐ If this project helped you, please consider giving it a star on GitHub!

Last Updated: November 25, 2024
cd qa-agent-project

# 2. Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. (Optional) Install and start Ollama
# Download from https://ollama.ai
# Pull a model:
ollama pull llama3.2
```

### Running the Application

```bash
# Terminal 1: Start FastAPI Backend
uvicorn backend.main:app --reload

# Terminal 2: Start Streamlit UI
streamlit run frontend/streamlit_app.py
```

The application will open automatically in your browser at `http://localhost:8501`

---

## 📁 Project Structure

```
qa-agent-project/
│
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── rag_engine.py          # RAG pipeline with LLM integration
│   ├── document_processor.py  # Document parsing (MD, TXT, JSON, PDF, HTML)
│   └── vector_store.py        # ChromaDB vector database (auto-created)
│
├── frontend/
│   └── streamlit_app.py       # Streamlit web interface
│
├── assets/
│   ├── checkout.html          # Sample e-commerce checkout page
│   └── support_docs/
│       ├── product_specs.md       # Product specifications
│       ├── ui_ux_guide.txt        # UI/UX design guidelines
│       ├── api_endpoints.json     # API documentation
│       ├── test_strategy.md       # Testing strategy
│       └── validation_rules.txt   # Validation specifications
│
├── generated/                  # Auto-created directories
│   ├── test_cases/            # Generated test case JSON files
│   └── selenium_scripts/      # Generated Python scripts
│
├── vector_db/                 # ChromaDB storage (auto-created)
│
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── .gitignore                 # Git ignore rules
└── demo_video.md             # Demo video guide

```

---

## 💿 Installation

### Step-by-Step Installation

#### 1. System Requirements

- **Operating System**: Windows 10/11, macOS 10.15+, or Linux
- **Python**: Version 3.9, 3.10, or 3.11
- **RAM**: Minimum 8GB (16GB recommended)
- **Storage**: 2GB free space

#### 2. Clone Repository

```bash
git clone https://github.com/yourusername/qa-agent-project.git
cd qa-agent-project
```

#### 3. Create Virtual Environment

```bash
# Using venv (recommended)
python -m venv venv

# Activate on Windows
venv\Scripts\activate

# Activate on macOS/Linux
source venv/bin/activate
```

#### 4. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs:

- FastAPI & Uvicorn (web framework)
- Streamlit (UI)
- LangChain (RAG framework)
- ChromaDB (vector database)
- Sentence Transformers (embeddings)
- BeautifulSoup4 (HTML parsing)
- PyMuPDF (PDF processing)
- Selenium (for script generation)
- And other supporting libraries

#### 5. Verify Installation

```bash
python -c "import fastapi, streamlit, langchain, chromadb; print('All packages installed successfully!')"
```

#### 6. Optional: Install Ollama (for LLM functionality)

The system works with mock responses if Ollama is not installed, but for full functionality:

1. Download Ollama from [https://ollama.ai](https://ollama.ai)
2. Install and start Ollama
3. Pull a model:
   ```bash
   ollama pull llama3.2
   ```

---

## 📖 Usage Guide

### Phase 1: Knowledge Base Ingestion

1. **Start the Backend**:

   ```bash
   uvicorn backend.main:app --reload
   ```

   Backend runs at `http://localhost:8000`

2. **Start the Frontend**:

   ```bash
   streamlit run frontend/streamlit_app.py
   ```

   Frontend opens at `http://localhost:8501`

3. **Upload Documents**:
   - Navigate to "Document Upload" tab
   - Upload the 5 support documents from `assets/support_docs/`
   - Upload `assets/checkout.html`
   - Click "Build Knowledge Base"
   - Wait for processing (creates vector embeddings)

### Phase 2: Test Case Generation

1. **Navigate to "Test Case Generation" tab**

2. **Enter your query**. Examples:

   ```
   Generate comprehensive test cases for discount code functionality
   ```

   ```
   Create positive and negative test cases for form validation
   ```

   ```
   Generate test cases for shipping method selection
   ```

3. **Adjust number of test cases** (1-10)

4. **Click "Generate Test Cases"**

5. **Review generated test cases**:
   - Each test case shows:
     - Test ID
     - Feature being tested
     - Test scenario description
     - Test type (positive/negative)
     - Preconditions
     - Step-by-step test steps
     - Expected results
     - Source documentation reference

### Phase 3: Selenium Script Generation

1. **Navigate to "Script Generation" tab**

2. **Select a test case** from the dropdown

3. **Review test case details**

4. **Click "Generate Selenium Script"**

5. **Download or copy the script**:

   - Script includes:
     - Proper imports
     - WebDriver setup
     - Element locators matching actual HTML
     - Test step implementations
     - Assertions for verification
     - Error handling

6. **Run the script** (example):
   ```bash
   # Update the file path in the script first
   python generated/selenium_scripts/TC-001_selenium.py
   ```

---

## 🔌 API Documentation

### Backend API Endpoints

#### Health Check

```http
GET http://localhost:8000/health
```

**Response**:

```json
{
  "status": "healthy",
  "knowledge_base_built": true,
  "html_uploaded": true,
  "num_documents": 6
}
```

#### Upload Documents

```http
POST http://localhost:8000/upload_documents
Content-Type: multipart/form-data

files: [file1, file2, ...]
```

**Response**:

```json
{
  "status": "success",
  "processed_documents": [
    {
      "filename": "product_specs.md",
      "type": "support_doc",
      "chunks": 15
    }
  ],
  "message": "Uploaded 5 document(s)"
}
```

#### Build Knowledge Base

```http
POST http://localhost:8000/build_knowledge_base
```

**Response**:

```json
{
  "status": "success",
  "num_documents": 6,
  "num_chunks": 87,
  "message": "Knowledge base built successfully"
}
```

#### Generate Test Cases

```http
POST http://localhost:8000/generate_test_cases
Content-Type: application/json

{
  "query": "Generate test cases for discount code",
  "num_cases": 5
}
```

**Response**:

```json
{
  "status": "success",
  "test_cases": [
    {
      "test_id": "TC-001",
      "feature": "Discount Code",
      "test_scenario": "Apply valid discount code SAVE15",
      "test_type": "positive",
      "preconditions": "Cart has items",
      "test_steps": [...],
      "expected_result": "15% discount applied",
      "grounded_in": "product_specs.md"
    }
  ],
  "count": 5
}
```

#### Generate Selenium Script

```http
POST http://localhost:8000/generate_selenium_script
Content-Type: application/json

{
  "test_case_id": "TC-001",
  "test_case_content": { ... }
}
```

**Response**:

```json
{
  "status": "success",
  "test_case_id": "TC-001",
  "script": "from selenium import webdriver..."
}
```

---

## 📚 Support Documents Included

### 1. product_specs.md (5.2 KB)

Complete product specifications including:

- Product catalog (3 products)
- Shopping cart functionality
- Discount code rules (SAVE15, SAVE20)
- Shipping options (Standard FREE, Express $10)
- Payment methods (Credit Card, PayPal)
- Order calculation logic
- Business rules

### 2. ui_ux_guide.txt (11.8 KB)

Comprehensive UI/UX specifications:

- Color palette and gradients
- Typography standards
- Button specifications
- Form element styling
- Error message formats
- Validation display rules
- Accessibility requirements (WCAG 2.1 AA)

### 3. api_endpoints.json (7.3 KB)

API documentation including:

- 10 REST endpoints
- Request/response formats
- Validation rules
- Error codes
- Rate limiting
- Authentication details

### 4. test_strategy.md (14.1 KB)

Testing strategy document:

- Test objectives and metrics
- Test types (functional, UI/UX, accessibility)
- Test case categories
- Automation strategy
- Entry/exit criteria
- Risk mitigation

### 5. validation_rules.txt (15.6 KB)

Detailed validation specifications:

- Field-by-field validation rules
- Email regex patterns
- Error message text
- Validation timing
- Edge cases
- Implementation checklist

### 6. checkout.html (13.2 KB)

Target web application:

- E-commerce checkout page
- 3 products with "Add to Cart"
- Shopping cart with quantity controls
- Discount code input
- Customer details form
- Shipping/payment selection
- Complete JavaScript functionality

---

## ⚙️ Configuration

### Environment Variables (Optional)

Create a `.env` file in the project root:

```env
# LLM Configuration
OLLAMA_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2

# Embedding Model
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Vector Database
VECTOR_DB_PATH=./vector_db

# API Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Streamlit Configuration
STREAMLIT_SERVER_PORT=8501
```

### Customizing RAG Parameters

Edit `backend/rag_engine.py`:

```python
# Text chunking parameters
self.text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # Adjust chunk size
    chunk_overlap=200,      # Adjust overlap
    length_function=len,
    separators=["\n\n", "\n", ". ", " ", ""]
)

# Number of retrieved chunks
context_docs = self.retrieve_context(query, k=8)  # Adjust k value
```

---

## 🧪 Testing

### Running the Application

1. **Test Backend**:

   ```bash
   # Start backend
   uvicorn backend.main:app --reload

   # In another terminal, test health endpoint
   curl http://localhost:8000/health
   ```

2. **Test Frontend**:
   ```bash
   streamlit run frontend/streamlit_app.py
   ```
   Access at `http://localhost:8501`

### Sample Test Queries

Try these queries in the Test Case Generation tab:

```
Generate test cases for adding products to cart
```

```
Create negative test cases for form validation with invalid email formats
```

```
Generate test cases for discount code SAVE15 and SAVE20 application
```

```
Create test cases for shipping method selection and cost calculation
```

```
Generate boundary test cases for cart quantity limits
```

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: "ModuleNotFoundError"

**Solution**: Ensure virtual environment is activated and dependencies installed

```bash
pip install -r requirements.txt
```

#### Issue: "Port 8000 already in use"

**Solution**: Kill the process or use a different port

```bash
# Find process
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Use different port
uvicorn backend.main:app --port 8001
```

#### Issue: "Ollama connection failed"

**Solution**: System works with mock responses. For full functionality:

1. Install Ollama from https://ollama.ai
2. Start Ollama service
3. Pull a model: `ollama pull llama3.2`

#### Issue: "ChromaDB directory not found"

**Solution**: Directory is created automatically. Ensure write permissions in project folder.

#### Issue: "Embeddings download slow"

**Solution**: First run downloads sentence-transformers model (~90MB). Subsequent runs use cached model.

#### Issue: "Streamlit shows connection error"

**Solution**:

1. Ensure FastAPI backend is running first
2. Check `API_URL` in `streamlit_app.py` matches backend address
3. Default: `http://localhost:8000`

---

## 🎥 Demo Video

### Creating Your Demo Video (5-10 minutes)

Record a demo showing:

1. **Introduction** (30 seconds)

   - Briefly explain the project
   - Show project structure

2. **Phase 1: Document Upload** (2 minutes)

   - Start backend and frontend
   - Upload support documents
   - Upload checkout.html
   - Click "Build Knowledge Base"
   - Show success message

3. **Phase 2: Test Case Generation** (2-3 minutes)

   - Enter a test query
   - Adjust number of test cases
   - Generate test cases
   - Review generated test cases
   - Highlight:
     - Test case structure
     - Source document references
     - Positive and negative scenarios

4. **Phase 3: Script Generation** (2-3 minutes)

   - Select a test case
   - Generate Selenium script
   - Review the script code
   - Show proper element selectors
   - Demonstrate download functionality
   - (Optional) Run the script

5. **Conclusion** (1 minute)
   - Recap key features
   - Mention RAG technology
   - Highlight zero hallucinations

### Screen Recording Tools

- **Windows**: OBS Studio, ShareX
- **macOS**: QuickTime, OBS Studio
- **Linux**: SimpleScreenRecorder, OBS Studio
- **Online**: Loom, Screencast-O-Matic

---

## 🏗️ Architecture

### System Components

```
┌─────────────────────────────────────────────────────────┐
│                    Streamlit Frontend                    │
│              (User Interface - Port 8501)                │
└─────────────────────┬───────────────────────────────────┘
                      │ HTTP Requests
┌─────────────────────▼───────────────────────────────────┐
│                   FastAPI Backend                        │
│              (REST API - Port 8000)                      │
├──────────────────────────────────────────────────────────┤
│  ┌─────────────────┐  ┌──────────────────────────────┐  │
│  │   Document      │  │      RAG Engine              │  │
│  │   Processor     │─▶│  - Vector Store (Chroma)     │  │
│  │  - MD, TXT      │  │  - Embeddings (HuggingFace)  │  │
│  │  - JSON, PDF    │  │  - LLM Integration (Ollama)  │  │
│  │  - HTML Parser  │  │  - Context Retrieval         │  │
│  └─────────────────┘  └──────────────────────────────┘  │
└──────────────────────────────────────────────────────────┘
                      │
         ┌────────────┴───────────────┐
         │                            │
    ┌────▼─────┐              ┌───────▼────────┐
    │ ChromaDB │              │  Ollama LLM    │
    │ (Vector  │              │  (Optional)    │
    │  Store)  │              └────────────────┘
    └──────────┘
```

### Technology Stack

- **Frontend**: Streamlit 1.29
- **Backend**: FastAPI 0.104
- **RAG Framework**: LangChain 0.1
- **Vector Database**: ChromaDB 0.4
- **Embeddings**: Sentence Transformers
- **LLM**: Ollama (llama3.2) or Mock
- **Document Processing**: BeautifulSoup, PyMuPDF
- **Test Automation**: Selenium 4.15

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📝 License

This project is licensed under the MIT License.

---

## 👥 Authors

- Shrinidhi Ganesan - Initial work

---

## 🙏 Acknowledgments

- LangChain for RAG framework
- Anthropic for Claude AI inspiration
- Ollama for local LLM support
- ChromaDB for vector storage
- Streamlit for beautiful UI framework

---

## 📧 Support

For questions or issues:

- Open an issue on GitHub
- Email: shrinidhiganesan0507@gmail.com

---

## 🗺️ Roadmap

- [ ] Add support for more document formats (DOCX, PPTX)
- [ ] Implement test case export to various formats
- [ ] Add support for Playwright script generation
- [ ] Integrate with CI/CD pipelines
- [ ] Add test execution and reporting
- [ ] Multi-language support for test cases
- [ ] Cloud deployment guide

---

**⭐ If this project helped you, please consider giving it a star on GitHub!**

---
---

**Happy Optimizing & Automating! 🚀**

---

> Built with ❤️ for the optimization and QA community.  
> For questions or support, [open an issue] or email: shrinidhiganesan0507@gmail.com
