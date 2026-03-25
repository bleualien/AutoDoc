import ast

class CodeParser:
    @staticmethod
    def extract_functions(source_code: str):
        try:
            tree = ast.parse(source_code)
            functions = []
            lines = source_code.splitlines()
            
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    start = node.lineno - 1
                    end = node.end_lineno
                    functions.append({
                        "name": node.name,
                        "code": "\n".join(lines[start:end])
                    })
            return functions
        except Exception:
            return []