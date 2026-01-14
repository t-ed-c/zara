# Zara Compiler

The Zara Compiler is a cutting-edge project designed to simplify the process of translating high-level programming code into efficient machine-level instructions. This project showcases a powerful and modern compiler with a focus on performance, extensibility, and ease of use. Zara is aimed at developers who seek a reliable and robust solution for compiling code across varied architectures.

---

## Development Timeline

The Zara Compiler was meticulously developed over an 11-week timeframe, with a structured timeline devoted to achieving key milestones:

1. **Week 1-2:** Research & Requirement Analysis
   - Conducted an in-depth study of compiler design principles and targeted features.
2. **Week 3-5:** Core Development
   - Implemented the lexical analyzer and parser modules.
   - Designed the Abstract Syntax Tree (AST) for code representation.
3. **Week 6-8:** Code Generation & Optimization
   - Developed machine code generation techniques.
   - Integrated optimization routines for enhanced performance.
4. **Week 9-10:** Testing & Debugging
   - Rigorous testing for edge cases and performance benchmarking.
5. **Week 11:** Documentation & Finalization
   - Completed core documentation, README, and user manuals.

---

## Key Features

The Zara Compiler incorporates a range of modern and essential features:

- **Multi-language Support:** Zara can parse and compile code written in multiple programming languages.
- **Optimized Code Generation:** Ensures high performance by utilizing advanced optimization techniques.
- **Cross-Platform Compatibility:** Allows developers to compile code for different target architectures.
- **Extensible Modules:** Easy to extend for additional programming languages and architectures.
- **Comprehensive Debugging Tools:** Integrated tools to trace and debug code effectively.

---

## Prerequisites

Before setting up the Zara Compiler, ensure you have the following:

- Operating System: Linux/MacOS/Windows
- Compiler: GCC, Clang, or MSVC
- Tooling: Git, CMake (v3.15+), Python3 (optional)

---

## Setup Instructions

Follow these steps to set up the Zara Compiler:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/t-ed-c/zara.git
   cd zara
   ```

2. **Build the Source:**
   ```bash
   mkdir build && cd build
   cmake ..
   make
   ```

3. **Run Tests (Optional):**
   ```bash
   make test
   ```

4. **Install the Compiler:** (requires appropriate permissions)
   ```bash
   sudo make install
   ```

---

## Usage Instructions

Once the Zara Compiler is installed, you can use it to compile your projects. Below is a basic example of Zara Compiler commands:

```bash
zara -o output_file input_file.zara
```

- `-o`: Specifies the output file.
- `input_file.zara`: The Zara code file you wish to compile.

To learn about all available options:
```bash
zara --help
```

---

## Contributing

Contributions to the Zara Compiler project are welcome! If you wish to contribute:

1. Fork the repository.
2. Create a new branch.
3. Submit a pull request with your proposed changes.

---

## License

This project is licensed under the [MIT License](./LICENSE), allowing you the freedom to use, modify, and distribute Zara in your own projects.

---

## Support

For support or queries, feel free to open an issue in this repository or reach out to the project maintainers.