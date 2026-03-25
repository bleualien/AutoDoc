import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

class AIEngine:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("API Key missing in .env")
        
        genai.configure(api_key=api_key)
        
        # This logic finds the BEST available model for your specific API key
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Priority list: Flash -> Pro -> Default
        if 'models/gemini-1.5-flash' in available_models:
            model_name = 'models/gemini-1.5-flash'
        elif 'models/gemini-pro' in available_models:
            model_name = 'models/gemini-pro'
        else:
            # Fallback to the first available model if the others aren't found
            model_name = available_models[0] if available_models else 'gemini-pro'
            
        self.model = genai.GenerativeModel(model_name)
        self.total_tokens = 0

    def generate_documentation(self, func_name, func_code):
        prompt = (
            f"As a Senior Dev, document this Python function: {func_name}\n\n"
            f"CODE:\n{func_code}\n\n"
            "Return Markdown with: ### Description, ### Args, and ### Returns."
        )
        try:
            response = self.model.generate_content(prompt)
            # Some versions of the API return usage, some don't. We check safely.
            try:
                if hasattr(response, 'usage_metadata'):
                    self.total_tokens += response.usage_metadata.total_token_count
            except:
                pass 
                
            return response.text
        except Exception as e:
            return f"> Error documenting {func_name}: {str(e)}"

    def get_token_count(self):
        return self.total_tokens