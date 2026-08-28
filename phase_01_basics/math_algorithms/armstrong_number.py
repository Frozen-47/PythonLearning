# Python program: Armstrong Number Checker
# Date: 2026-08-28

def is_armstrong(num: int) -> bool:
    s = str(num)
    n = len(s)
    return sum(int(digit) ** n for digit in s) == num

if __name__ == "__main__":
    test_nums = [153, 370, 371, 407, 123]
    for n in test_nums:
        print(f"{n} is Armstrong: {is_armstrong(n)}")
