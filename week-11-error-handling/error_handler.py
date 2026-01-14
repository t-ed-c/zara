# Zara Compiler's Week 11 Error Handler
# This module provides robust error recovery mechanisms.

def handle_error(error_code):
    errors = {
        404: "Resource not found.",
        500: "Internal server error.",
        403: "Access forbidden. Check permissions.",
    }
    return errors.get(error_code, "Unknown error code. Contact support.")

if __name__ == "__main__":
    test_code = 404
    print(f"Handling error for code {test_code}: {handle_error(test_code)}")