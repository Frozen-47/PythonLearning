str = input("Enter a String : ")
k = int(input("Enter Substring size : "))
n = len(str)
vowels = "aeiou"
max_count = 0
for i in range(0,n-k+1):
    print(str[i:i+3])
    count = 0
    for j in range(i,k+i):
        if str[j] in vowels:
            count+=1
    max_count = max(max_count,count)
print(max_count)