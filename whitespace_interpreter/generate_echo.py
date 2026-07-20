import os

def to_ws_num(n):
    """Convert integer n to Whitespace binary representation."""
    if n == 0:
        return "SL"
    sign = "S" if n > 0 else "T"
    binary_str = bin(abs(n))[2:]
    ws_binary = "".join("T" if b == "1" else "S" for b in binary_str)
    return sign + ws_binary + "L"

def generate_echo_program():
    # We will use the following labels:
    # label_read = "SL"
    # label_end_read = "TL"
    # label_print = "SSL"
    # label_end_print = "TTL"
    
    ws_code = ""
    annotated = []
    
    # --- Helper to append instructions ---
    def add_inst(code, desc):
        nonlocal ws_code
        ws_code += code
        annotated.append(f"{code} -> {desc}")
        
    def add_comment(comment):
        annotated.append(f"\n# {comment}")

    # Prompt user for input: "Enter text: "
    prompt = "Enter text: "
    add_comment("Print prompt: 'Enter text: '")
    for char in prompt:
        val = ord(char)
        add_inst("SS" + to_ws_num(val), f"PUSH {val} ({repr(char)})")
        add_inst("TLSS", "PRINT_CHAR")

    # Read logic
    add_comment("Initialize target heap address to 0")
    add_inst("SS" + to_ws_num(0), "PUSH 0 (start address)")
    
    add_comment("Mark label READ_LOOP")
    add_inst("LSS" + "S" + "L", "LABEL READ_LOOP")
    
    add_comment("Duplicate current address for reading")
    add_inst("SLS", "DUP")
    
    add_comment("Read character from stdin into current heap address")
    add_inst("TLTS", "READ_CHAR")
    
    add_comment("Duplicate address again to retrieve and check the char")
    add_inst("SLS", "DUP")
    add_inst("TTT", "RETRIEVE")
    
    add_comment("Push 10 (newline ASCII) to compare")
    add_inst("SS" + to_ws_num(10), "PUSH 10")
    
    add_comment("Subtract to see if char == newline")
    add_inst("TSST", "SUB")
    
    add_comment("If char - 10 == 0, jump to END_READ")
    add_inst("LTS" + "T" + "L", "JUMP_ZERO END_READ")
    
    add_comment("Else: increment target heap address by 1")
    add_inst("SS" + to_ws_num(1), "PUSH 1")
    add_inst("TSSS", "ADD")
    
    add_comment("Loop back to READ_LOOP")
    add_inst("LSL" + "S" + "L", "JUMP READ_LOOP")
    
    # End read logic
    add_comment("Mark label END_READ")
    add_inst("LSS" + "T" + "L", "LABEL END_READ")
    
    add_comment("Overwrite the newline character with a 0 sentinel")
    add_inst("SLS", "DUP")
    add_inst("SS" + to_ws_num(0), "PUSH 0 (sentinel value)")
    add_inst("TTS", "STORE")
    
    add_comment("Discard address from stack")
    add_inst("SLL", "DISCARD")

    # Print response prefix: "You entered: "
    prefix = "You entered: "
    add_comment("Print response prefix: 'You entered: '")
    for char in prefix:
        val = ord(char)
        add_inst("SS" + to_ws_num(val), f"PUSH {val} ({repr(char)})")
        add_inst("TLSS", "PRINT_CHAR")
        
    # Print logic
    add_comment("Initialize print address pointer to 0")
    add_inst("SS" + to_ws_num(0), "PUSH 0 (start address)")
    
    add_comment("Mark label PRINT_LOOP")
    add_inst("LSS" + "SS" + "L", "LABEL PRINT_LOOP")
    
    add_comment("Duplicate address to retrieve character")
    add_inst("SLS", "DUP")
    add_inst("TTT", "RETRIEVE")
    
    add_comment("Duplicate character to check for sentinel 0")
    add_inst("SLS", "DUP")
    add_inst("LTS" + "TT" + "L", "JUMP_ZERO END_PRINT")
    
    add_comment("Print character")
    add_inst("TLSS", "PRINT_CHAR")
    
    add_comment("Increment address pointer by 1")
    add_inst("SS" + to_ws_num(1), "PUSH 1")
    add_inst("TSSS", "ADD")
    
    add_comment("Loop back to PRINT_LOOP")
    add_inst("LSL" + "SS" + "L", "JUMP PRINT_LOOP")
    
    # End print logic
    add_comment("Mark label END_PRINT")
    add_inst("LSS" + "TT" + "L", "LABEL END_PRINT")
    
    add_comment("Clean up stack: discard char (0) and address")
    add_inst("SLL", "DISCARD (pop 0)")
    add_inst("SLL", "DISCARD (pop final address)")
    
    add_comment("Print a final newline")
    add_inst("SS" + to_ws_num(10), "PUSH 10")
    add_inst("TLSS", "PRINT_CHAR")
    
    # Exit
    add_comment("Exit program")
    add_inst("LLL", "EXIT")
    
    # Translate S -> Space, T -> Tab, L -> Newline
    ws_binary = ws_code.replace("S", " ").replace("T", "\t").replace("L", "\n")
    
    # Translate representation for annotated text file
    annotated_text = []
    for line in annotated:
        if line.strip().startswith("#") or not line.strip():
            annotated_text.append(line)
        else:
            parts = line.split(" -> ")
            inst_code = parts[0].replace("S", " ").replace("T", "\\t").replace("L", "\\n")
            desc = parts[1]
            annotated_text.append(f"{inst_code:<30} -> {desc}")
            
    return ws_binary, "\n".join(annotated_text)

if __name__ == "__main__":
    os.makedirs("d:/Programming/Github Projects/PythonLearning/WhitespaceHelloWorld", exist_ok=True)
    
    ws_binary, ws_annotated = generate_echo_program()
    
    # Save the raw whitespace program
    ws_path = "d:/Programming/Github Projects/PythonLearning/WhitespaceHelloWorld/echo.ws"
    with open(ws_path, "wb") as f:
        f.write(ws_binary.encode('utf-8'))
    print(f"Generated raw Whitespace echo program at: {ws_path}")
    
    # Save the annotated version
    annotated_path = "d:/Programming/Github Projects/PythonLearning/WhitespaceHelloWorld/echo_annotated.txt"
    with open(annotated_path, "w", encoding="utf-8") as f:
        f.write(ws_annotated)
    print(f"Generated annotated text at: {annotated_path}")
