# Python program: GCD and LCM Calculation using Euclidean Algorithm
# Date: 2026-08-28

import math

def compute_gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def compute_lcm(a: int, b: int) -> int:
    return abs(a * b) // compute_gcd(a, b)

if __name__ == "__main__":
    num1, num2 = 36, 60
    print(f"Numbers: {num1}, {num2}")
    print(f"GCD: {compute_gcd(num1, num2)}")
    print(f"LCM: {compute_lcm(num1, num2)}")
