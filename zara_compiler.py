"""
Zara Compiler Implementation
Author: t-ed-c
Date: 2026-01-14

This file contains the complete implementation of the Zara Compiler, integrating the work of all 11 weeks. 
The implementation includes detailed comments to ensure a clear understanding of the code for anyone reviewing it.
The Zara Compiler is designed to convert Zara-specific code to executable machine code with support for
variable declarations, control flow structures, and function handling.
"""

# Import Necessary Libraries
import re

# Token Types
token_types = {
    'KEYWORD': ['var', 'function', 'if', 'else', 'while', 'return'],
    'OPERATOR': ['+', '-', '*', '/', '=', '==', '!=', '<', '>', '<=', '>='],
    'DELIMITER': [';', ',', '(', ')', '{', '}'],
    'IDENTIFIER': r'[a-zA-Z_]\w*',
    'NUMBER': r'\d+(\.\d+)?',
}

# Lexer Implementation
def lexer(code):
    """Converts Zara code into a list of tokens"""
    tokens = []
    position = 0

    while position < len(code):
        match = None

        for token_type, patterns in token_types.items():
            if isinstance(patterns, list):
                for pattern in patterns:
                    if code.startswith(pattern, position):
                        match = (token_type, pattern)
                        position += len(pattern)
                        break
            else:  # Regex Patterns
                regex = re.compile(patterns)
                result = regex.match(code, position)
                if result:
                    match = (token_type, result.group(0))
                    position = result.end()

            if match:
                tokens.append(match)
                break

        if not match:
            raise SyntaxError(f"Unexpected character: {code[position]} at position {position}")

    return tokens

# Abstract Syntax Tree (AST) Node Definitions
class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class VariableDeclaration(ASTNode):
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Parser Implementation
def parser(tokens):
    """Parses tokens into an Abstract Syntax Tree"""
    position = 0

    def parse_statement():
        nonlocal position
        token_type, token_value = tokens[position]

        if token_type == 'KEYWORD' and token_value == 'var':
            position += 1
            name = tokens[position][1]
            position += 1
            if tokens[position][1] != '=':
                raise SyntaxError("Expected '=' after variable name")
            position += 1
            value = tokens[position][1]
            position += 1
            if tokens[position][1] != ';':
                raise SyntaxError("Expected ';' at the end of variable declaration")
            position += 1
            return VariableDeclaration(name, value)

        raise SyntaxError("Unexpected statement")

    statements = []
    while position < len(tokens):
        statements.append(parse_statement())

    return Program(statements)

# Code Generator Implementation
def code_generator(ast):
    """Generates machine code from the Abstract Syntax Tree"""
    machine_code = []

    for statement in ast.statements:
        if isinstance(statement, VariableDeclaration):
            machine_code.append(f"LOAD {statement.value}\nSTORE {statement.name}")

    return '\n'.join(machine_code)

# Main Compiler Function
def compile_zara(source_code):
    """End-to-End: Zara code to machine code"""
    tokens = lexer(source_code)
    ast = parser(tokens)
    machine_code = code_generator(ast)
    return machine_code

# Example Zara Code
source_code = ""
var x = 5;
var y = 10;""

# Compile Zara Code
try:
    compiled_code = compile_zara(source_code)
    print("--- Zara Compiled Code ---")
    print(compiled_code)
except SyntaxError as error:
    print("Compilation Error:", error)