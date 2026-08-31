# Python program: Perfect Number Checker
# Date: 2026-08-31

def is_perfect_number(n: int) -> bool:
    if n <= 1:
        return False
    divisors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sum(divisors) == n

if __name__ == "__main__":
    test_cases = [6, 28, 496, 12, 100]
    for num in test_cases:
        print(f"{num} is perfect: {is_perfect_number(num)}")
