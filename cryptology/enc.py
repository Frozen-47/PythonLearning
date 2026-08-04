message = input("Enter Message to encrypt : ")
lstmsg = list(map(str,(map(ord,list(message)))))
strmsg = list("".join(lstmsg))[::-1]
pairmsg = [strmsg[i] + strmsg[i+1] for i in range(0, len(strmsg), 2)]
pairmsg = list(map(chr,(map(int,pairmsg))))
print("".join(pairmsg))