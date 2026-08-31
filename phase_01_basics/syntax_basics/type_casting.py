# Python program: Implicit and Explicit Type Casting
# Date: 2026-08-31

def demo_type_casting():
    # Implicit conversion
    int_val = 100
    float_val = 12.5
    res = int_val + float_val
    print(f"Result: {res}, Type: {type(res)}")

    # Explicit conversion
    str_num = "456"
    converted = int(str_num)
    print(f"Converted: {converted}, Type: {type(converted)}")

if __name__ == "__main__":
    demo_type_casting()
