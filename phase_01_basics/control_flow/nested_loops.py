# Python program: Nested Loops and Pattern Generation
# Date: 2026-08-29

def print_pyramid(n: int):
    for i in range(1, n + 1):
        print(" " * (n - i) + "* " * i)

def print_number_triangle(n: int):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

if __name__ == "__main__":
    print("Pyramid Pattern:")
    print_pyramid(5)
    print("\nNumber Triangle:")
    print_number_triangle(5)
