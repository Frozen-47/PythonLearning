inp = int(input())
for i in range(10,inp+1):
    count = 0
    for j in range(2,(i//2)+1):
        if i % j == 0:
            count += 1
    if(count == 0):
        print(i,end=" ")