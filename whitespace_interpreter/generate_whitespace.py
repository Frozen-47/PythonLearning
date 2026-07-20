import os

def to_ws_num(n):
    """Convert integer n to Whitespace binary representation."""
    if n == 0:
        return "SL"
    sign = "S" if n > 0 else "T"
    binary_str = bin(abs(n))[2:]  # Remove the '0b' prefix
    ws_binary = "".join("T" if b == "1" else "S" for b in binary_str)
    return sign + ws_binary + "L"

def generate_hello_world():
    text = "Hello, World!\n"
    
    ws_code = ""
    annotated = []
    
    for char in text:
        ascii_val = ord(char)
        push_num = to_ws_num(ascii_val)
        
        # S S is the push command
        push_inst = "SS" + push_num
        # T L S S is output character
        print_inst = "TLSS"
        
        ws_code += push_inst + print_inst
        
        # Add to annotated output
        char_repr = repr(char)
        annotated.append(f"# Push ASCII {ascii_val} ({char_repr})")
        annotated.append(f"SS {push_num.replace('S', ' ').replace('T', '\\t').replace('L', '\\n')} -> PUSH {ascii_val}")
        annotated.append(f"# Print Character")
        annotated.append(f"TLSS -> PRINT_CHAR")
        annotated.append("")
        
    # Exit instruction: L L L (Flow control: End program)
    ws_code += "LLL"
    annotated.append("# Exit program")
    annotated.append("LLL -> EXIT")
    
    # Translate S -> Space, T -> Tab, L -> Newline
    ws_binary = ws_code.replace("S", " ").replace("T", "\t").replace("L", "\n")
    
    return ws_binary, "\n".join(annotated)

if __name__ == "__main__":
    os.makedirs("d:/Programming/Github Projects/PythonLearning/WhitespaceHelloWorld", exist_ok=True)
    
    ws_binary, ws_annotated = generate_hello_world()
    
    # Save the raw whitespace program
    ws_path = "d:/Programming/Github Projects/PythonLearning/WhitespaceHelloWorld/helloworld.ws"
    with open(ws_path, "wb") as f:
        f.write(ws_binary.encode('utf-8'))
    print(f"Generated raw Whitespace program at: {ws_path}")
    
    # Save the annotated version
    annotated_path = "d:/Programming/Github Projects/PythonLearning/WhitespaceHelloWorld/helloworld_annotated.txt"
    with open(annotated_path, "w", encoding="utf-8") as f:
        f.write(ws_annotated)
    print(f"Generated annotated text at: {annotated_path}")
