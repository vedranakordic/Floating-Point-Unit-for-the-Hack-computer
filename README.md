## Floating-Point Unit for the Hack Computer

This repository contains an implementation of a **16-bit Hack computer** extended with floating-point support, inspired by the "Nand2Tetris" project. The goal is to enable the Hack platform to represent and manipulate floating-point numbers, both in hardware and software, following the IEEE 754 standard \[1]\[2].


### Overview

* **Foundation**: Extension of the classic Hack computer from *The Elements of Computing Systems* by Nisan and Schocken \[5].
* **Standard**: IEEE 754 for floating-point representation \[1].
* **Technologies**: Python for tooling, HDL for hardware components.
* **Key Components**:

  * Hardware Floating-Point Unit (FPU) in HDL \[2].
  * Extended assembler and VM parser to support floating-point operations \[1].
  * Compiler for the Jack language with floating-point support \[1].


### Repository Structure

```
├── ASM_Parser/       # Hack assembler parser with float support
├── Compiler/         # Jack language compiler (extended for float)
├── FPU_HDL/          # HDL code for the floating-point unit
├── VM_Parser/        # VM language parser with floating-point instructions
└── ...               # Additional tools and tests
```


### Installation & Usage

1. **Download Nand2Tetris tools** and place them in the `tools/` directory.
2. **Compile Jack programs:**

   ```bash
   python Compiler/jack_compiler.py [input.jack] [output.vm]
   ```
3. **Run tests:**
   Example floating-point programs are available in the `tests/` directory.


### Features

* **Hardware support:** The FPU supports basic arithmetic operations (addition, subtraction, multiplication) \[2].
* **Software integration:**

  * Extended VM language with `FADD`, `FSUB`, `FMUL` instructions \[1].
  * Support for floating-point literals in Jack (e.g., `var float x = 3.14159;`) \[1].
* **Compatibility:** Works with standard Nand2Tetris tools and Hack programs \[3].


### Academic Context

* **Project origin:** Developed as a bachelor thesis at the Faculty of Applied Mathematics and Informatics, Osijek \[1].
* **Mentor:** Assoc. Prof. Domagoj Matijević \[1].
* **Full documentation:** See the \[thesis PDF]\[1].


### License

This project is open source under the MIT license. Please credit the original repository if you use this code in your own work.


**Keywords:** floating-point, Hack computer, Nand2Tetris, FPU, HDL, assembler, virtual machine, compiler, Jack \[1]\[2].


> "In this project, we will be focusing on the software aspect of building a 16-bit computer as part of the 'Nand2Tetris' project and enhancing it to be able to handle floating-point numbers. We will get familiar with the basics of hardware operation, assembly language, the overall syntax of the virtual machine language, and the Jack programming language. Additionally, we will create a compiler for the Jack language."
> — \[Vedrana Kordić, 2023]\[1]


### References

\[1] [https://www.mathos.unios.hr/\~mdjumic/uploads/diplomski/KOR20.pdf](https://www.mathos.unios.hr/~mdjumic/uploads/diplomski/KOR20.pdf)
\[2] [https://www.mathos.unios.hr/\~mdjumic/uploads/diplomski/ORL02.pdf](https://www.mathos.unios.hr/~mdjumic/uploads/diplomski/ORL02.pdf)
\[3] [https://github.com/edunfelt/nand2tetris](https://github.com/edunfelt/nand2tetris)
\[4] [https://www.reddit.com/r/beneater/comments/udrns2/i\_built\_the\_hack\_computer\_from\_nand2tetris\_on/](https://www.reddit.com/r/beneater/comments/udrns2/i_built_the_hack_computer_from_nand2tetris_on/)
\[5] [https://en.wikipedia.org/wiki/Hack\_computer](https://en.wikipedia.org/wiki/Hack_computer)

