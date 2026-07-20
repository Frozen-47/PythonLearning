# Inverted Numeric Triangle Pattern
# Prints numbers from 0 up to i-1, decreasing the length of the row on each step.

for i in range(9, 0, -1):
    for j in range(i):
        print(j, end=" ")
    print()
