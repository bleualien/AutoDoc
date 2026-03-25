# System Architecture

The Proshore AutoDoc tool follows a modular pipe-and-filter architecture:

1. **UI Layer (Streamlit)**: Handles file uploads and state management.
2. **Security Filter**: Scans raw strings for PII/Secrets using Regex patterns.
3. **AST Parser**: Deconstructs Python source into an Abstract Syntax Tree to isolate function logic.
4. **AI Orchestrator**: Manages dynamic model selection (Flash vs Pro) and tracks token consumption for cost auditing.
5. **Output Generator**: Formats and serves the finalized Markdown documentation.