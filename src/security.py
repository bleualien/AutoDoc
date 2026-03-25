import re

class SecurityScanner:
    PATTERNS = {
        "Secret": r'(?i)(password|secret|passwd|pwd)\s*[:=]\s*["\'](.*?)["\']',
        "API_Key": r'(?i)(api[_-]?key|auth[_-]?token)\s*[:=]\s*["\'](.*?)["\']',
    }

    @staticmethod
    def mask_secrets(code: str) -> tuple[str, bool]:
        masked_code = code
        found_secret = False
        for label, pattern in SecurityScanner.PATTERNS.items():
            if re.search(pattern, masked_code):
                found_secret = True
                masked_code = re.sub(pattern, r'\1: "[MASKED_FOR_SECURITY]"', masked_code)
        return masked_code, found_secret