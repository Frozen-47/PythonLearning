# Python program: Anonymous Lambda Functions and Higher-Order Functions
# Date: 2026-08-30

def demo_lambdas():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Map with lambda
    squares = list(map(lambda x: x**2, nums))
    print("Squares:", squares)
    
    # Filter with lambda
    evens = list(filter(lambda x: x % 2 == 0, nums))
    print("Evens:", evens)
    
    # Sort tuples with lambda key
    pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
    pairs.sort(key=lambda item: item[0])
    print("Sorted pairs:", pairs)

if __name__ == "__main__":
    demo_lambdas()
