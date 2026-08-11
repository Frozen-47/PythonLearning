str = input("Enter a string : ")
substr  = ""
splited = []
for ch in str:
    if ch != ' ':
        substr += ch
    else:
        splited.append(substr)
        substr=""
splited.append(substr)
for i in splited:
    if(i == i[::-1]):
        print(f"${i}$ ",end=" ")
    else:
        print(i," ",end=" ")