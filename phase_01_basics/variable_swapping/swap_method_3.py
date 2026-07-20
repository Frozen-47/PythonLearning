a = 10
b = 20 
print("Before Swaping : ")
print(f"A : {a} || B : {b}")
a = b ^ a
b = a ^ b
a = b ^ a
print("After Swaping : ")
print(f"A : {a} || B : {b}")