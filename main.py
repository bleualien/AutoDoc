import streamlit as st
from src.parser import CodeParser
from src.ai_engine import AIEngine
from src.security import SecurityScanner

# 1. Page Configuration
st.set_page_config(page_title="AutoDoc", layout="centered")

# 2. Eye-Pleasing Dark Aesthetics
st.markdown("""
    <style>
    /* Main Background: Deep Charcoal/Black */
    .stApp {
        background-color: #0f172a;
    }
    
    /* Text Colors: Off-White for readability */
    h1, h2, h3, p, span, label {
        color: #f1f5f9 !important;
        font-family: 'Inter', sans-serif;
    }

    /* Muted Caption */
    .stCaption {
        color: #94a3b8 !important;
    }

    /* Clean Info/Warning Boxes: Darker Blue-Gray */
    .stAlert {
        background-color: #1e293b;
        border: 1px solid #334155;
        color: #cbd5e1;
    }

    /* Minimalist Button: Cool Slate Blue */
    .stButton>button {
        background-color: #334155;
        color: #f1f5f9;
        border: 1px solid #475569;
        border-radius: 4px;
        padding: 0.5rem 2rem;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #475569;
        border: 1px solid #3b82f6;
        color: white;
    }

    /* Divider Color */
    hr {
        border-top: 1px solid #334155 !important;
    }

    /* File Uploader Box */
    [data-testid="stFileUploadDropzone"] {
        background-color: #1e293b;
        border: 1px dashed #475569;
    }

    /* Code Block Contrast */
    code {
        color: #38bdf8 !important;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # Initialize Engine silently
    if 'engine' not in st.session_state:
        try:
            st.session_state.engine = AIEngine()
        except Exception:
            st.error("Engine failed to start. Check your GOOGLE_API_KEY.")
            return

    # Header Section
    st.title("AutoDoc")
    st.caption("Secure AI-Powered Documentation")
    
    # 1. Upload Section
    uploaded_file = st.file_uploader("Upload a Python file", type="py", label_visibility="collapsed")

    if uploaded_file:
        raw_code = uploaded_file.getvalue().decode("utf-8")
        
        # 2. Simple Action Button
        if st.button("Generate Documentation"):
            
            # Step A: Security & Parsing
            safe_code, was_masked = SecurityScanner.mask_secrets(raw_code)
            functions = CodeParser.extract_functions(safe_code)

            if was_masked:
                st.info("Security Filter: Sensitive data was identified and masked.")

            if not functions:
                st.warning("No functions found in this file.")
            else:
                st.write("---")
                
                # Step B: Display Results
                full_md = f"# Docs: {uploaded_file.name}\n\n"
                
                for func in functions:
                    with st.container():
                        # We use a spinner for better UX
                        with st.spinner(f"Analyzing {func['name']}..."):
                            doc_chunk = st.session_state.engine.generate_documentation(func['name'], func['code'])
                        
                        st.markdown(doc_chunk)
                        st.write("---")
                        full_md += doc_chunk + "\n\n"

                # Step C: Export
                st.download_button("Download README.md", full_md, "documentation.md")
                
                # Show source code at the bottom (Secondary)
                with st.expander("View Cleaned Source Code"):
                    st.code(safe_code, language="python")
    else:
        st.write("---")
        st.caption("Upload a .py file to begin analysis.")

if __name__ == "__main__":
    main()