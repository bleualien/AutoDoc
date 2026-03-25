# Auto-Doc AI 🤖

A professional AI-powered tool that parses Python source code and automatically generates technical documentation using Google Gemini 1.5 Flash.

## ✨ Features
- **AST Parsing**: Uses Python's Abstract Syntax Tree to identify functions safely.
- **Modular Architecture**: Separated Logic (src/) from UI (main.py).
- **Streamlit UI**: Clean, web-based interface for file uploads and markdown previews.
- **Secure**: Uses `.env` for API key management.

## 🛠️ Setup
1. Clone this folder.
2. Create a `.env` file and add your `GOOGLE_API_KEY`.
3. Install dependencies: `pip install -r requirements.txt`
4. Run the app: `streamlit run main.py`