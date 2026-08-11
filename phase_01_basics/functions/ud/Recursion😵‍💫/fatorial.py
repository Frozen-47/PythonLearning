def factorial(n):
    if n <= 0:
        return 1
    return n*factorial(n-1)
n = int(input("Enter a Num to find its Factorial: "))
print("Factorial of ",n," : ",factorial(n))