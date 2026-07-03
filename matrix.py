for i in range(9,0,-1):
    for j in range(i):
        print(j,end=" ")
        
    print()

for i in range(1, 6):
    print(" " * (5 - i), end="")
    print(f"{i}" * (2 * i - 1))

list =[]
list.append("leo")
print(list)