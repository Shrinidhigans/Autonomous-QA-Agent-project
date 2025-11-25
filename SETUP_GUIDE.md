# Quick Setup Guide - Autonomous QA Agent

This guide will help you set up and run the project in 10 minutes or less.

---

## 📋 Prerequisites Checklist

Before starting, ensure you have:

- [ ] Python 3.9 or higher installed
- [ ] pip package manager
- [ ] Git (for cloning)
- [ ] Text editor (VS Code, PyCharm, etc.)
- [ ] Terminal/Command Prompt access

Check your Python version:

```bash
python --version
# Should show 3.9 or higher
```

---

## 🚀 5-Minute Setup

### Step 1: Get the Code (1 minute)

```bash
# Clone repository
git clone https://github.com/yourusername/qa-agent-project.git

# Navigate to project
cd qa-agent-project
```

### Step 2: Set Up Environment (2 minutes)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Your prompt should now show (venv)
```

### Step 3: Install Dependencies (2 minutes)

```bash
# Upgrade pip
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt

# This will take 1-2 minutes
```

---

## ▶️ Running the Application

### Option A: Quick Start (Recommended)

Open **two terminal windows**:

**Terminal 1 - Backend:**

```bash
cd qa-agent-project
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
uvicorn backend.main:app --reload
```

**Terminal 2 - Frontend:**

```bash
cd qa-agent-project
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
streamlit run frontend/streamlit_app.py
```

The Streamlit UI will open automatically in your browser!

### Option B: One-Command Start (Advanced)

Create a `start.bat` (Windows) or `start.sh` (Mac/Linux):

**start.bat:**

```batch
@echo off
start cmd /k "cd /d %~dp0 && venv\Scripts\activate && uvicorn backend.main:app --reload"
start cmd /k "cd /d %~dp0 && venv\Scripts\activate && streamlit run frontend/streamlit_app.py"
```

**start.sh:**

```bash
#!/bin/bash
cd "$(dirname "$0")"
source venv/bin/activate
uvicorn backend.main:app --reload &
streamlit run frontend/streamlit_app.py
```

Then run:

```bash
# Windows:
start.bat

# Mac/Linux:
chmod +x start.sh
./start.sh
```

---

## 🎯 First Run Walkthrough

### 1. Upload Documents (2 minutes)

1. Go to **"Document Upload"** tab
2. Click **"Browse files"**
3. Navigate to `assets/support_docs/`
4. Select all 5 documents:
   - product_specs.md
   - ui_ux_guide.txt
   - api_endpoints.json
   - test_strategy.md
   - validation_rules.txt
5. Also upload `assets/checkout.html`
6. Click **"Build Knowledge Base"**
7. Wait for success message (30 seconds)

### 2. Generate Test Cases (1 minute)

1. Go to **"Test Case Generation"** tab
2. Enter query:
   ```
   Generate comprehensive test cases for discount code functionality
   ```
3. Set number of test cases: **5**
4. Click **"Generate Test Cases"**
5. Review the generated test cases

### 3. Generate Script (1 minute)

1. Go to **"Script Generation"** tab
2. Select a test case from dropdown
3. Click **"Generate Selenium Script"**
4. Download or copy the script

---

## 🔧 Troubleshooting

### Issue: "Command not found: python"

**Solution:** Try `python3` instead of `python`

### Issue: "Permission denied"

**Solution (Mac/Linux):**

```bash
chmod +x venv/bin/activate
```

### Issue: "Port already in use"

**Solution:**

```bash
# Use different port
uvicorn backend.main:app --port 8001
```

### Issue: "Module not found"

**Solution:**

```bash
# Ensure virtual environment is activated
# Look for (venv) in your prompt
pip install -r requirements.txt
```

### Issue: "Slow first run"

**Reason:** Downloading embedding model (~90MB)
**Solution:** Wait for first run to complete. Subsequent runs will be fast.

---

## 🎓 Understanding the Workflow

```
1. Upload Documents → 2. Build KB → 3. Generate Tests → 4. Generate Scripts
      ↓                     ↓               ↓                   ↓
   [5 docs + HTML]    [Vector Store]  [Test Cases JSON]  [Selenium Python]
```

### What Happens Behind the Scenes:

1. **Document Upload**:

   - Files parsed (MD, TXT, JSON, HTML)
   - Text extracted and cleaned
   - Stored in memory

2. **Build Knowledge Base**:

   - Text split into chunks (1000 chars)
   - Embeddings generated (sentence-transformers)
   - Stored in ChromaDB vector database
   - ~87 chunks created from 6 documents

3. **Generate Test Cases**:

   - Query embedded
   - Similar chunks retrieved (semantic search)
   - Context sent to LLM
   - Test cases generated in JSON format
   - Each case references source document

4. **Generate Script**:
   - Test case + HTML structure sent to LLM
   - Selenium script generated
   - Proper element selectors included
   - Ready-to-run Python code

---

## 📁 Project File Overview

```
qa-agent-project/
├── backend/           ← FastAPI server code
├── frontend/          ← Streamlit UI
├── assets/            ← Test documents
│   ├── checkout.html          ← Target application
│   └── support_docs/          ← 5 documentation files
├── requirements.txt   ← Python dependencies
└── README.md         ← Full documentation
```

---

## 🎬 Creating Your Demo Video

### Recording Checklist:

- [ ] Start with clean state (clear browser cache)
- [ ] Record in 1080p for clarity
- [ ] Show terminal commands being executed
- [ ] Zoom in on important text
- [ ] Use voiceover or captions
- [ ] Keep it under 10 minutes
- [ ] Include:
  - [ ] Project introduction
  - [ ] Document upload process
  - [ ] Knowledge base building
  - [ ] Test case generation
  - [ ] Script generation
  - [ ] Generated script review

### Suggested Structure:

```
0:00 - 0:30   Introduction & Project Overview
0:30 - 2:00   Phase 1: Upload Documents
2:00 - 4:00   Phase 2: Generate Test Cases
4:00 - 6:00   Phase 3: Generate Selenium Scripts
6:00 - 7:00   Show Generated Script
7:00 - 8:00   Highlight Key Features
8:00 - 10:00  Q&A or Additional Features
```

---

## 🚨 Common First-Time Mistakes

❌ **Not activating virtual environment**
✅ Always activate: `venv\Scripts\activate`

❌ **Using wrong Python version**
✅ Check with: `python --version` (need 3.9+)

❌ **Not waiting for knowledge base build**
✅ Wait for "Knowledge Base Built Successfully!" message

❌ **Generating script before test cases**
✅ Follow order: Upload → Build KB → Test Cases → Scripts

---

## 💡 Pro Tips

1. **Faster Startup**: Keep terminals open, just restart servers with Ctrl+C then up arrow

2. **Better Test Cases**: Be specific in queries:

   - ✅ "Generate test cases for form validation with invalid email formats"
   - ❌ "Generate some tests"

3. **Script Customization**: Generated scripts are templates. Adjust file paths and add assertions as needed.

4. **Document Updates**: Re-upload documents and rebuild KB if you modify support docs.

5. **API Testing**: Use Postman or curl to test API endpoints directly:
   ```bash
   curl http://localhost:8000/health
   ```

---

## 📞 Getting Help

If you're stuck:

1. **Check the logs** in the terminal
2. **Review README.md** for detailed info
3. **Check API health**: `http://localhost:8000/health`
4. **Restart everything**: Ctrl+C both terminals, restart
5. **Reinstall dependencies**: `pip install -r requirements.txt --force-reinstall`

---

## ✅ Verification Steps

After setup, verify everything works:

```bash
# 1. Test Python imports
python -c "import fastapi, streamlit, langchain; print('✓ All imports work')"

# 2. Check backend
curl http://localhost:8000/health

# 3. Check Streamlit
# Should open in browser automatically
```

Expected:

- ✓ Backend running at http://localhost:8000
- ✓ Frontend at http://localhost:8501
- ✓ No error messages in terminals
- ✓ Can upload documents successfully

---

## 🎉 Success!

You're now ready to:

- ✓ Upload documents
- ✓ Build knowledge bases
- ✓ Generate test cases
- ✓ Create Selenium scripts
- ✓ Impress your evaluators!

---

**⏱️ Total Setup Time: ~10 minutes**
**🎯 Next Step: Follow the "First Run Walkthrough" above**

Good luck with your assignment! 🚀
