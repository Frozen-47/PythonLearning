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
    reverse = i[::-1]
    if(i == reverse):
        print(f"${i}$ ",end=" ")
    else:
        print(i," ",end=" ")