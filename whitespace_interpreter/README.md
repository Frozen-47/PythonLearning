# Whitespace Programs

This directory contains a collection of programs written in the esoteric programming language [Whitespace](https://en.wikipedia.org/wiki/Whitespace_(programming_language)), along with a custom interpreter and generator scripts written in Python.

## Files

1. **[helloworld.ws](file:///d:/Programming/Github%20Projects/PythonLearning/WhitespaceHelloWorld/helloworld.ws)**: The raw Whitespace Hello World program. If you open this in a normal text editor, it will appear empty because Whitespace ignores all visible characters.
2. **[helloworld_annotated.txt](file:///d:/Programming/Github%20Projects/PythonLearning/WhitespaceHelloWorld/helloworld_annotated.txt)**: A human-readable annotation of `helloworld.ws` showing the spaces, tabs, and newlines representing instructions.
3. **[generate_whitespace.py](file:///d:/Programming/Github%20Projects/PythonLearning/WhitespaceHelloWorld/generate_whitespace.py)**: The Python script that compiles a string to a raw Whitespace file.
4. **[echo.ws](file:///d:/Programming/Github%20Projects/PythonLearning/WhitespaceHelloWorld/echo.ws)**: An interactive Whitespace program that prompts the user, reads a line of input from stdin, stores it in heap memory, and echoes it back.
5. **[echo_annotated.txt](file:///d:/Programming/Github%20Projects/PythonLearning/WhitespaceHelloWorld/echo_annotated.txt)**: Human-readable annotations detailing the labels, heap access, stack arithmetic, loops, and conditions of `echo.ws`.
6. **[generate_echo.py](file:///d:/Programming/Github%20Projects/PythonLearning/WhitespaceHelloWorld/generate_echo.py)**: The Python script that generates `echo.ws` and its annotations.
7. **[run_whitespace.py](file:///d:/Programming/Github%20Projects/PythonLearning/WhitespaceHelloWorld/run_whitespace.py)**: A fully functional Whitespace interpreter in Python.

## How to Run

### Hello World Program
Run the static Hello World program:
```bash
python WhitespaceHelloWorld/run_whitespace.py WhitespaceHelloWorld/helloworld.ws
```
Output:
```text
Hello, World!
```

### Echo (Interactive User Input) Program
Run the interactive user input program:
```bash
python WhitespaceHelloWorld/run_whitespace.py WhitespaceHelloWorld/echo.ws
```
You can type some text and press Enter, and the program will echo your text back.

Example of piping input:
```bash
"Hello Antigravity" | python WhitespaceHelloWorld/run_whitespace.py WhitespaceHelloWorld/echo.ws
```
Output:
```text
Enter text: You entered: Hello Antigravity
```
