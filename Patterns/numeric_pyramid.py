# Numeric Pyramid Pattern
# Prints an aligned pyramid of numbers, where each row i consists of the number i repeated (2*i - 1) times.

for i in range(1, 6):
    print(" " * (5 - i), end="")
    print(f"{i}" * (2 * i - 1))
