text = input("Enter words: ")

words = text.split()

for i in words:
    rev = i[::-1]
    if(i == rev):
        print(f"*{i}* ",end = " ")
    else:
        print(i," ")