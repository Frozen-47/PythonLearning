print("# RightAngle Triangle")
n = int(input("Enter the size of the Triangle: "))
for i in range(n+1):
    for j in range(i):
        print("*", end= " ")
    print()
