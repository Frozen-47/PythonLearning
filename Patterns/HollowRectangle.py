print("# Hollow Rectangle")
l = int(input("Enter the length of the rectangle: "))
b = int(input("Enter the breadth of the rectangle: "))
for i in range(b):
    for j in range(l):
        if(i == 0 or j == 0 or i == b-1 or j == l-1):
            print("#",end = " " )
        else:
            print(" ",end = " ")
    print()
