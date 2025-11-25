from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import json
import os
from pathlib import Path

from backend.rag_engine import RAGEngine
from backend.document_processor import DocumentProcessor

app = FastAPI(title="Autonomous QA Agent API")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
rag_engine = RAGEngine()
doc_processor = DocumentProcessor()

# Data models
class TestCaseRequest(BaseModel):
    query: str
    num_cases: Optional[int] = 5

class ScriptGenerationRequest(BaseModel):
    test_case_id: str
    test_case_content: dict

class KnowledgeBaseStatus(BaseModel):
    status: str
    num_documents: int
    num_chunks: int
    message: str

# Storage
uploaded_html = ""
knowledge_base_built = False

@app.get("/")
async def root():
    return {"message": "Autonomous QA Agent API", "status": "running"}

@app.post("/upload_documents")
async def upload_documents(files: List[UploadFile] = File(...)):
    """Upload and process support documents"""
    try:
        processed_docs = []
        
        for file in files:
            content = await file.read()
            
            # Process based on file type
            if file.filename.endswith('.html'):
                global uploaded_html
                uploaded_html = content.decode('utf-8')
                doc_processor.set_html_content(uploaded_html)
                processed_docs.append({
                    "filename": file.filename,
                    "type": "html",
                    "size": len(content)
                })
            else:
                # Process as support document
                text_content = doc_processor.process_file(
                    content, 
                    file.filename
                )
                processed_docs.append({
                    "filename": file.filename,
                    "type": "support_doc",
                    "chunks": len(text_content) // 500
                })
        
        return {
            "status": "success",
            "processed_documents": processed_docs,
            "message": f"Uploaded {len(files)} document(s)"
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/build_knowledge_base")
async def build_knowledge_base() -> KnowledgeBaseStatus:
    """Build vector database from uploaded documents"""
    try:
        if not doc_processor.documents:
            raise HTTPException(
                status_code=400, 
                detail="No documents uploaded. Please upload documents first."
            )
        
        # Build knowledge base
        num_chunks = rag_engine.build_knowledge_base(doc_processor.documents)
        
        global knowledge_base_built
        knowledge_base_built = True
        
        return KnowledgeBaseStatus(
            status="success",
            num_documents=len(doc_processor.documents),
            num_chunks=num_chunks,
            message="Knowledge base built successfully"
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_test_cases")
async def generate_test_cases(request: TestCaseRequest):
    """Generate test cases using RAG + LLM"""
    try:
        if not knowledge_base_built:
            raise HTTPException(
                status_code=400,
                detail="Knowledge base not built. Please build it first."
            )
        
        # Generate test cases
        test_cases = rag_engine.generate_test_cases(
            query=request.query,
            num_cases=request.num_cases
        )
        
        return {
            "status": "success",
            "test_cases": test_cases,
            "count": len(test_cases)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/generate_selenium_script")
async def generate_selenium_script(request: ScriptGenerationRequest):
    """Generate Selenium script for a specific test case"""
    try:
        if not knowledge_base_built:
            raise HTTPException(
                status_code=400,
                detail="Knowledge base not built. Please build it first."
            )
        
        if not uploaded_html:
            raise HTTPException(
                status_code=400,
                detail="No HTML file uploaded. Please upload checkout.html."
            )
        
        print(f"Generating script for test case: {request.test_case_id}")
        
        # Generate Selenium script - pass html_content parameter
        script = rag_engine.generate_selenium_script(
            test_case=request.test_case_content,
            html_content=uploaded_html
        )
        
        return {
            "status": "success",
            "test_case_id": request.test_case_id,
            "script": script
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "knowledge_base_built": knowledge_base_built,
        "html_uploaded": bool(uploaded_html),
        "num_documents": len(doc_processor.documents)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)