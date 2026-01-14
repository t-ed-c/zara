# Zara Compiler Week 9 Object-Oriented Module
# This module introduces basic support for classes and inheritance.

class BaseClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}"

class DerivedClass(BaseClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display_info(self):
        return f"I am {self.name} and I am {self.age} years old."

# Example usage
if __name__ == "__main__":
    base = BaseClass("Base")
    print(base.greet())

    derived = DerivedClass("Derived", 25)
    print(derived.greet())
    print(derived.display_info())