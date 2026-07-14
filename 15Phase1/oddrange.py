f = int(input())
l = int(input())
c = 0
for i in range(f,l+1):
    if(i % 2 != 0):
        c+=1
print (c)