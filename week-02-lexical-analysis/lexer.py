# Zara Compiler's Week 2 Lexical Analyzer

def analyze_lexical(content):
    tokens = []
    current_token = ""

    for char in content:
        if char.isspace():
            if current_token:
                tokens.append(current_token)
                current_token = ""
        elif char.isalnum() or char == '_':
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            tokens.append(char)

    if current_token:
        tokens.append(current_token)

    return tokens

if __name__ == "__main__":
    content = "int x = 42;"
    print("Tokens:", analyze_lexical(content))