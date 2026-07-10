str = input("Enter a String : ")
k = int(input("Enter Substring size : "))
n = len(str)
print("Substrings : ")
    #Method 1
'''
    for i in range(0,n-k+1):
    for j in range(i,k+i):
        print(str[j],end="")
    print()'''
    #Method 2
for i in range(0,n-k+1):
    print(str[i:i+3])