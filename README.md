# SlateDoc: Secure AI Documentation Engine

SlateDoc is a minimalist, high-performance tool built to automate technical documentation for Python projects using **Gemini 1.5 Flash**.

## 🛡️ Engineering Highlights (Mid-Level Patterns)
- **Security-First Architecture**: Features a pre-processing layer that masks PII and secrets (API keys/passwords) before data transmission to the LLM.
- **AST Structural Analysis**: Uses Python's `ast` module for robust function extraction, ensuring accuracy that regular expressions cannot provide.
- **Resilient AI Orchestration**: Implemented dynamic model discovery and fallback logic to handle API versioning (v1/v1beta) and service availability.
- **Resource Auditing**: Built-in token tracking to monitor and audit cloud compute costs per session.

## 🎨 Design Philosophy
The UI is built with a "Cool Slate" aesthetic, focusing on a distraction-free environment with muted tones to reduce cognitive load during technical reviews.

## 🛠️ Tech Stack
- **Language**: Python 3.12
- **LLM**: Google Gemini 1.5 Flash
- **Interface**: Streamlit (Custom CSS)
- **Parsing**: Abstract Syntax Trees (AST)

## 🚀 Setup
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/SlateDoc.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your `GOOGLE_API_KEY` to a `.env` file.
4. Run: `streamlit run main.py`