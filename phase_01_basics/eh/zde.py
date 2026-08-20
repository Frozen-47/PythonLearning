try:
    a = int(input())
    b = int(input())
    c = a/b

except ZeroDivisionError:
    print("Cannot Divide by Zero")
except ValueError:
    print("Enter a valid data")