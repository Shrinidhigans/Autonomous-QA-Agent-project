import streamlit as st
import requests
import json
from typing import List

# Configuration
API_URL = "http://localhost:8000"

# Page config
st.set_page_config(
    page_title="Autonomous QA Agent",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .success-box {
        padding: 1rem;
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .info-box {
        padding: 1rem;
        background-color: #d1ecf1;
        border-left: 5px solid #17a2b8;
        border-radius: 5px;
        margin: 1rem 0;
    }
    .test-case-card {
        border: 2px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.5rem 0;
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'knowledge_base_built' not in st.session_state:
    st.session_state.knowledge_base_built = False
if 'test_cases' not in st.session_state:
    st.session_state.test_cases = []
if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []

# Header
st.markdown('<h1 class="main-header">🤖 Autonomous QA Agent</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align: center; font-size: 1.2rem; color: #666;">Intelligent Test Case & Selenium Script Generation</p>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["📁 Document Upload", "🧪 Test Case Generation", "💻 Script Generation"])

# TAB 1: Document Upload
with tab1:
    st.header("Phase 1: Knowledge Base Ingestion")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Upload Documents")
        
        # File uploader
        uploaded_files = st.file_uploader(
            "Upload support documents (MD, TXT, JSON, PDF) and HTML file",
            type=['md', 'txt', 'json', 'pdf', 'html'],
            accept_multiple_files=True,
            help="Upload product specs, UI guides, API docs, and the checkout.html file"
        )
        
        if uploaded_files:
            st.session_state.uploaded_files = uploaded_files
            
            # Display uploaded files
            st.write(f"**{len(uploaded_files)} file(s) uploaded:**")
            for file in uploaded_files:
                file_type = "🌐 HTML" if file.name.endswith('.html') else "📄 Document"
                st.write(f"{file_type} {file.name} ({file.size} bytes)")
        
        # Build knowledge base button
        if st.button("🔨 Build Knowledge Base", type="primary", disabled=not uploaded_files):
            with st.spinner("Processing documents and building knowledge base..."):
                try:
                    # Upload documents
                    files_data = []
                    for file in uploaded_files:
                        files_data.append(
                            ('files', (file.name, file.getvalue(), file.type))
                        )
                    
                    response = requests.post(
                        f"{API_URL}/upload_documents",
                        files=files_data
                    )
                    
                    if response.status_code == 200:
                        st.success("✅ Documents uploaded successfully!")
                        
                        # Build knowledge base
                        build_response = requests.post(f"{API_URL}/build_knowledge_base")
                        
                        if build_response.status_code == 200:
                            result = build_response.json()
                            st.session_state.knowledge_base_built = True
                            
                            st.markdown(f"""
                            <div class="success-box">
                                <h3>✅ Knowledge Base Built Successfully!</h3>
                                <p><strong>Documents processed:</strong> {result['num_documents']}</p>
                                <p><strong>Text chunks created:</strong> {result['num_chunks']}</p>
                                <p>You can now generate test cases in the next tab.</p>
                            </div>
                            """, unsafe_allow_html=True)
                        else:
                            st.error(f"Failed to build knowledge base: {build_response.text}")
                    else:
                        st.error(f"Upload failed: {response.text}")
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")
    
    with col2:
        st.subheader("Status")
        
        # Health check
        try:
            health = requests.get(f"{API_URL}/health").json()
            
            st.metric("Knowledge Base", "✅ Built" if health['knowledge_base_built'] else "❌ Not Built")
            st.metric("HTML Uploaded", "✅ Yes" if health['html_uploaded'] else "❌ No")
            st.metric("Documents", health['num_documents'])
            
        except:
            st.warning("⚠️ Backend API not reachable. Please start the FastAPI server.")
        
        # Instructions
        st.info("""
        **Instructions:**
        1. Upload 3-5 support documents
        2. Upload the checkout.html file
        3. Click "Build Knowledge Base"
        4. Wait for processing to complete
        """)

# TAB 2: Test Case Generation
with tab2:
    st.header("Phase 2: Test Case Generation")
    
    if not st.session_state.knowledge_base_built:
        st.warning("⚠️ Please build the knowledge base first (Tab 1)")
    else:
        col1, col2 = st.columns([3, 1])
        
        with col1:
            st.subheader("Generate Test Cases")
            
            # Query input
            query = st.text_area(
                "Describe what you want to test:",
                value="Generate comprehensive test cases for the checkout page including discount code, form validation, shipping options, and payment methods.",
                height=100,
                help="Be specific about features, scenarios, or areas you want to test"
            )
            
            num_cases = st.slider("Number of test cases", 1, 10, 5)
            
            if st.button("🧪 Generate Test Cases", type="primary"):
                with st.spinner("Generating test cases using RAG + LLM..."):
                    try:
                        response = requests.post(
                            f"{API_URL}/generate_test_cases",
                            json={
                                "query": query,
                                "num_cases": num_cases
                            }
                        )
                        
                        if response.status_code == 200:
                            result = response.json()
                            st.session_state.test_cases = result['test_cases']
                            st.success(f"✅ Generated {len(st.session_state.test_cases)} test case(s)!")
                        else:
                            st.error(f"Generation failed: {response.text}")
                    
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        
        with col2:
            st.subheader("Options")
            st.info("""
            **Tips:**
            - Be specific in your query
            - Request both positive and negative cases
            - Mention specific features
            """)
        
        # Display test cases
        if st.session_state.test_cases:
            st.subheader("Generated Test Cases")
            
            for i, tc in enumerate(st.session_state.test_cases):
                with st.expander(f"📋 {tc.get('test_id', f'TC-{i+1}')} - {tc.get('feature', 'Test Case')}", expanded=(i == 0)):
                    col1, col2 = st.columns([3, 1])
                    
                    with col1:
                        st.markdown(f"**Test Scenario:** {tc.get('test_scenario', 'N/A')}")
                        st.markdown(f"**Type:** `{tc.get('test_type', 'N/A')}`")
                        st.markdown(f"**Preconditions:** {tc.get('preconditions', 'N/A')}")
                        
                        st.markdown("**Test Steps:**")
                        steps = tc.get('test_steps', [])
                        for j, step in enumerate(steps, 1):
                            st.markdown(f"{j}. {step}")
                        
                        st.markdown(f"**Expected Result:** {tc.get('expected_result', 'N/A')}")
                        st.markdown(f"**📚 Grounded in:** `{tc.get('grounded_in', 'N/A')}`")
                    
                    with col2:
                        if st.button(f"Generate Script", key=f"gen_{i}"):
                            st.session_state.selected_test_case = tc
                            st.session_state.selected_test_id = tc.get('test_id', f'TC-{i+1}')
                            st.info("Go to 'Script Generation' tab to see the script!")

# TAB 3: Script Generation
with tab3:
    st.header("Phase 3: Selenium Script Generation")
    
    if not st.session_state.knowledge_base_built:
        st.warning("⚠️ Please build the knowledge base first")
    elif not st.session_state.test_cases:
        st.warning("⚠️ Please generate test cases first")
    else:
        st.subheader("Select Test Case")
        
        # Test case selector
        test_case_options = [
            f"{tc.get('test_id', f'TC-{i+1}')} - {tc.get('feature', 'Test')}"
            for i, tc in enumerate(st.session_state.test_cases)
        ]
        
        selected_idx = st.selectbox(
            "Choose a test case to generate Selenium script:",
            range(len(test_case_options)),
            format_func=lambda x: test_case_options[x]
        )
        
        selected_tc = st.session_state.test_cases[selected_idx]
        
        # Display selected test case
        with st.expander("📋 Selected Test Case Details", expanded=True):
            st.json(selected_tc)
        
        # Generate script button
        if st.button("💻 Generate Selenium Script", type="primary"):
            with st.spinner("Generating Python Selenium script..."):
                try:
                    response = requests.post(
                        f"{API_URL}/generate_selenium_script",
                        json={
                            "test_case_id": selected_tc.get('test_id', 'TC-001'),
                            "test_case_content": selected_tc
                        }
                    )
                    
                    if response.status_code == 200:
                        result = response.json()
                        script = result['script']
                        
                        st.success("✅ Script generated successfully!")
                        
                        # Display script
                        st.subheader("Generated Selenium Script")
                        st.code(script, language='python')
                        
                        # Download button
                        st.download_button(
                            label="📥 Download Script",
                            data=script,
                            file_name=f"{selected_tc.get('test_id', 'test')}_selenium.py",
                            mime="text/x-python"
                        )
                        
                        st.info("""
                        **To run this script:**
                        1. Install Selenium: `pip install selenium`
                        2. Download ChromeDriver
                        3. Update the file path to your checkout.html
                        4. Run: `python script_name.py`
                        """)
                    else:
                        st.error(f"Generation failed: {response.text}")
                
                except Exception as e:
                    st.error(f"Error: {str(e)}")

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666; padding: 2rem;">
    <p>🤖 Autonomous QA Agent | Powered by RAG + LLM Technology</p>
    <p>FastAPI Backend | Streamlit Frontend | ChromaDB Vector Store</p>
</div>
""", unsafe_allow_html=True)