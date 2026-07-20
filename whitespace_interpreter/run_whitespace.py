import sys

class Instruction:
    def __init__(self, opcode, arg=None, label=None):
        self.opcode = opcode
        self.arg = arg
        self.label = label

    def __repr__(self):
        return f"{self.opcode}(arg={self.arg}, label={repr(self.label)})"

def compile_whitespace(code_str):
    code = [c for c in code_str if c in (' ', '\t', '\n')]
    instructions = []
    
    ip = 0
    n = len(code)
    
    def read_number(curr_ip):
        if curr_ip >= n:
            raise ValueError("EOF reading number")
        sign_char = code[curr_ip]
        if sign_char not in (' ', '\t'):
            raise ValueError("Invalid sign char")
        sign = 1 if sign_char == ' ' else -1
        curr_ip += 1
        bits = []
        while curr_ip < n and code[curr_ip] != '\n':
            bits.append('1' if code[curr_ip] == '\t' else '0')
            curr_ip += 1
        if curr_ip >= n:
            raise ValueError("EOF reading number terminator")
        curr_ip += 1  # consume '\n'
        val = 0
        if bits:
            val = int("".join(bits), 2)
        return sign * val, curr_ip

    def read_label(curr_ip):
        label_chars = []
        while curr_ip < n and code[curr_ip] != '\n':
            label_chars.append(code[curr_ip])
            curr_ip += 1
        if curr_ip >= n:
            raise ValueError("EOF reading label terminator")
        curr_ip += 1  # consume '\n'
        return "".join(label_chars), curr_ip

    while ip < n:
        char = code[ip]
        ip += 1
        
        if char == ' ':  # Stack Manipulation (IMP: Space)
            if ip >= n: raise ValueError("EOF in stack manipulation IMP")
            cmd = code[ip]
            ip += 1
            if cmd == ' ':  # Push
                val, ip = read_number(ip)
                instructions.append(Instruction("PUSH", arg=val))
            elif cmd == '\n':
                if ip >= n: raise ValueError("EOF in stack manipulation [Space][LF]")
                sub = code[ip]
                ip += 1
                if sub == ' ':
                    instructions.append(Instruction("DUP"))
                elif sub == '\t':
                    instructions.append(Instruction("SWAP"))
                elif sub == '\n':
                    instructions.append(Instruction("DISCARD"))
                else:
                    raise ValueError(f"Invalid sub-command {repr(sub)} after [Space][LF]")
            elif cmd == '\t':
                if ip >= n: raise ValueError("EOF in stack manipulation [Space][Tab]")
                sub = code[ip]
                ip += 1
                if sub == ' ':
                    val, ip = read_number(ip)
                    instructions.append(Instruction("COPY", arg=val))
                elif sub == '\n':
                    val, ip = read_number(ip)
                    instructions.append(Instruction("SLIDE", arg=val))
                else:
                    raise ValueError(f"Invalid sub-command {repr(sub)} after [Space][Tab]")
            else:
                raise ValueError(f"Invalid command {repr(cmd)} after Space IMP")
                
        elif char == '\t':  # Arithmetic, Heap, or I/O
            if ip >= n: raise ValueError("EOF after Tab")
            next_char = code[ip]
            ip += 1
            
            if next_char == ' ':  # Arithmetic (IMP: [Tab][Space])
                if ip + 1 >= n: raise ValueError("EOF in arithmetic command")
                cmd = code[ip:ip+2]
                ip += 2
                cmd_str = "".join(cmd)
                if cmd_str == '  ':
                    instructions.append(Instruction("ADD"))
                elif cmd_str == ' \t':
                    instructions.append(Instruction("SUB"))
                elif cmd_str == ' \n':
                    instructions.append(Instruction("MUL"))
                elif cmd_str == '\t ':
                    instructions.append(Instruction("DIV"))
                elif cmd_str == '\t\t':
                    instructions.append(Instruction("MOD"))
                else:
                    raise ValueError(f"Invalid arithmetic command {repr(cmd_str)}")
                    
            elif next_char == '\t':  # Heap access (IMP: [Tab][Tab])
                if ip >= n: raise ValueError("EOF in heap command")
                cmd = code[ip]
                ip += 1
                if cmd == ' ':
                    instructions.append(Instruction("STORE"))
                elif cmd == '\t':
                    instructions.append(Instruction("RETRIEVE"))
                else:
                    raise ValueError(f"Invalid heap command {repr(cmd)}")
                    
            elif next_char == '\n':  # I/O (IMP: [Tab][LF])
                if ip + 1 >= n: raise ValueError("EOF in I/O command")
                cmd = code[ip:ip+2]
                ip += 2
                cmd_str = "".join(cmd)
                if cmd_str == '  ':
                    instructions.append(Instruction("PRINT_CHAR"))
                elif cmd_str == ' \t':
                    instructions.append(Instruction("PRINT_NUM"))
                elif cmd_str == '\t ':
                    instructions.append(Instruction("READ_CHAR"))
                elif cmd_str == '\t\t':
                    instructions.append(Instruction("READ_NUM"))
                else:
                    raise ValueError(f"Invalid I/O command {repr(cmd_str)}")
            else:
                raise ValueError(f"Invalid char {repr(next_char)} after Tab IMP")
                
        elif char == '\n':  # Flow Control (IMP: LF)
            if ip + 1 >= n: raise ValueError("EOF in flow control")
            cmd = code[ip:ip+2]
            ip += 2
            cmd_str = "".join(cmd)
            
            if cmd_str == '  ':  # Mark label
                lbl, ip = read_label(ip)
                instructions.append(Instruction("LABEL", label=lbl))
            elif cmd_str == ' \t':  # Call subroutine
                lbl, ip = read_label(ip)
                instructions.append(Instruction("CALL", label=lbl))
            elif cmd_str == ' \n':  # Jump unconditionally
                lbl, ip = read_label(ip)
                instructions.append(Instruction("JUMP", label=lbl))
            elif cmd_str == '\t ':  # Jump if zero
                lbl, ip = read_label(ip)
                instructions.append(Instruction("JUMP_ZERO", label=lbl))
            elif cmd_str == '\t\t':  # Jump if negative
                lbl, ip = read_label(ip)
                instructions.append(Instruction("JUMP_NEG", label=lbl))
            elif cmd_str == '\t\n':  # Return
                instructions.append(Instruction("RETURN"))
            elif cmd_str == '\n\n':  # Exit
                instructions.append(Instruction("EXIT"))
            else:
                raise ValueError(f"Invalid flow control command {repr(cmd_str)}")
                
    return instructions

def execute_whitespace(instructions):
    labels = {}
    for idx, inst in enumerate(instructions):
        if inst.opcode == "LABEL":
            if inst.label in labels:
                raise ValueError(f"Duplicate label: {repr(inst.label)}")
            labels[inst.label] = idx

    stack = []
    heap = {}
    call_stack = []
    ip = 0
    n = len(instructions)
    
    while ip < n:
        inst = instructions[ip]
        opcode = inst.opcode
        
        if opcode == "PUSH":
            stack.append(inst.arg)
            ip += 1
        elif opcode == "DUP":
            if not stack: raise ValueError("Stack underflow in DUP")
            stack.append(stack[-1])
            ip += 1
        elif opcode == "SWAP":
            if len(stack) < 2: raise ValueError("Stack underflow in SWAP")
            stack[-1], stack[-2] = stack[-2], stack[-1]
            ip += 1
        elif opcode == "DISCARD":
            if not stack: raise ValueError("Stack underflow in DISCARD")
            stack.pop()
            ip += 1
        elif opcode == "COPY":
            idx = inst.arg
            if idx < 0 or idx >= len(stack):
                raise ValueError(f"Index {idx} out of stack range in COPY")
            stack.append(stack[-1 - idx])
            ip += 1
        elif opcode == "SLIDE":
            num_to_slide = inst.arg
            if len(stack) < num_to_slide + 1:
                raise ValueError("Stack underflow in SLIDE")
            top = stack.pop()
            for _ in range(num_to_slide):
                stack.pop()
            stack.append(top)
            ip += 1
        elif opcode == "ADD":
            if len(stack) < 2: raise ValueError("Stack underflow in ADD")
            b = stack.pop()
            a = stack.pop()
            stack.append(a + b)
            ip += 1
        elif opcode == "SUB":
            if len(stack) < 2: raise ValueError("Stack underflow in SUB")
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)
            ip += 1
        elif opcode == "MUL":
            if len(stack) < 2: raise ValueError("Stack underflow in MUL")
            b = stack.pop()
            a = stack.pop()
            stack.append(a * b)
            ip += 1
        elif opcode == "DIV":
            if len(stack) < 2: raise ValueError("Stack underflow in DIV")
            b = stack.pop()
            a = stack.pop()
            if b == 0: raise ZeroDivisionError("Whitespace division by zero")
            stack.append(a // b)
            ip += 1
        elif opcode == "MOD":
            if len(stack) < 2: raise ValueError("Stack underflow in MOD")
            b = stack.pop()
            a = stack.pop()
            if b == 0: raise ZeroDivisionError("Whitespace modulo by zero")
            stack.append(a % b)
            ip += 1
        elif opcode == "STORE":
            if len(stack) < 2: raise ValueError("Stack underflow in STORE")
            val = stack.pop()
            addr = stack.pop()
            heap[addr] = val
            ip += 1
        elif opcode == "RETRIEVE":
            if not stack: raise ValueError("Stack underflow in RETRIEVE")
            addr = stack.pop()
            if addr not in heap:
                raise ValueError(f"Heap address {addr} not initialized")
            stack.append(heap[addr])
            ip += 1
        elif opcode == "LABEL":
            ip += 1
        elif opcode == "CALL":
            if inst.label not in labels:
                raise ValueError(f"Undefined label {repr(inst.label)} in CALL")
            call_stack.append(ip + 1)
            ip = labels[inst.label]
        elif opcode == "JUMP":
            if inst.label not in labels:
                raise ValueError(f"Undefined label {repr(inst.label)} in JUMP")
            ip = labels[inst.label]
        elif opcode == "JUMP_ZERO":
            if not stack: raise ValueError("Stack underflow in JUMP_ZERO")
            val = stack.pop()
            if val == 0:
                if inst.label not in labels:
                    raise ValueError(f"Undefined label {repr(inst.label)} in JUMP_ZERO")
                ip = labels[inst.label]
            else:
                ip += 1
        elif opcode == "JUMP_NEG":
            if not stack: raise ValueError("Stack underflow in JUMP_NEG")
            val = stack.pop()
            if val < 0:
                if inst.label not in labels:
                    raise ValueError(f"Undefined label {repr(inst.label)} in JUMP_NEG")
                ip = labels[inst.label]
            else:
                ip += 1
        elif opcode == "RETURN":
            if not call_stack:
                raise ValueError("Call stack underflow in RETURN")
            ip = call_stack.pop()
        elif opcode == "EXIT":
            break
        elif opcode == "PRINT_CHAR":
            if not stack: raise ValueError("Stack underflow in PRINT_CHAR")
            val = stack.pop()
            sys.stdout.write(chr(val))
            sys.stdout.flush()
            ip += 1
        elif opcode == "PRINT_NUM":
            if not stack: raise ValueError("Stack underflow in PRINT_NUM")
            val = stack.pop()
            sys.stdout.write(str(val))
            sys.stdout.flush()
            ip += 1
        elif opcode == "READ_CHAR":
            if not stack: raise ValueError("Stack underflow in READ_CHAR")
            addr = stack.pop()
            char = sys.stdin.read(1)
            heap[addr] = ord(char) if char else 0
            ip += 1
        elif opcode == "READ_NUM":
            if not stack: raise ValueError("Stack underflow in READ_NUM")
            addr = stack.pop()
            num_str = ""
            while True:
                char = sys.stdin.read(1)
                if not char or char == '\n':
                    break
                if char.isdigit() or (char == '-' and not num_str):
                    num_str += char
            heap[addr] = int(num_str) if num_str else 0
            ip += 1
        else:
            raise ValueError(f"Unknown instruction {opcode}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_whitespace.py <path_to_ws_file>")
        sys.exit(1)
        
    filepath = sys.argv[1]
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            code_str = f.read()
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        sys.exit(1)
        
    try:
        instructions = compile_whitespace(code_str)
        execute_whitespace(instructions)
    except Exception as e:
        print(f"\nExecution error: {e}", file=sys.stderr)
        sys.exit(1)
