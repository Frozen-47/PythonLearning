"""
Python User-Defined Functions Basics
------------------------------------
This script demonstrates:
1. Basic function definition & calling
2. Positional and Keyword arguments
3. Default parameter values
4. Variable-length arguments (*args, **kwargs)
5. Return values (single & multiple)
6. Lambda (anonymous) functions
"""

# 1. Basic Function Definition & Calling
def greet(name: str) -> None:
    """Prints a greeting message for the given name."""
    print(f"Hello, {name}! Welcome to Python Functions.")

# 2. Positional & Keyword Arguments + Default Parameters
def calculate_total(price: float, tax_rate: float = 0.05, discount: float = 0.0) -> float:
    """Calculates final total price after tax and discount."""
    subtotal = price - discount
    total = subtotal * (1 + tax_rate)
    return round(total, 2)

# 3. Variable-length Arguments (*args and **kwargs)
def print_student_info(name: str, *subjects: str, **details: str) -> None:
    """
    *args captures additional positional arguments as a tuple.
    **kwargs captures additional keyword arguments as a dictionary.
    """
    print(f"\nStudent Name: {name}")
    print(f"Enrolled Subjects: {', '.join(subjects) if subjects else 'None'}")
    print("Additional Details:")
    for key, value in details.items():
        print(f"  - {key.capitalize()}: {value}")

# 4. Multiple Return Values
def get_min_max_sum(numbers: list[int]) -> tuple[int, int, int]:
    """Returns minimum, maximum, and total sum of a list of numbers."""
    if not numbers:
        return 0, 0, 0
    return min(numbers), max(numbers), sum(numbers)

# 5. Lambda (Anonymous) Function
square = lambda x: x ** 2
add_numbers = lambda a, b: a + b


if __name__ == "__main__":
    print("=== 1. Basic Function ===")
    greet("Sabareesh")

    print("\n=== 2. Default & Keyword Arguments ===")
    print("Total (default tax & discount):", calculate_total(100.0))
    print("Total (custom tax & discount):", calculate_total(100.0, tax_rate=0.10, discount=10.0))

    print("\n=== 3. *args & **kwargs ===")
    print_student_info("Sabareesh", "Python", "Data Structures", "Math", age="19", grade="A", city="Coimbatore")

    print("\n=== 4. Multiple Return Values ===")
    nums = [10, 25, 5, 40, 15]
    minimum, maximum, total_sum = get_min_max_sum(nums)
    print(f"Numbers: {nums}")
    print(f"Min: {minimum}, Max: {maximum}, Sum: {total_sum}")

    print("\n=== 5. Lambda Functions ===")
    print(f"Square of 7: {square(7)}")
    print(f"Sum of 12 and 8: {add_numbers(12, 8)}")
