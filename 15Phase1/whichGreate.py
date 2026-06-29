a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))
print("#"* 30)
if a > b and a > c:
    print(f"a : {a} > than b : {b} and c : {c}")
elif b > a and b > c:
    print(f"b : {b} > than a : {a} and c : {c}")
elif c > a and c > b:
    print(f"c : {c} > than a : {a} and b : {b}")
elif a == b == c:
    print("all are equal")
elif a == b:
    print("a and b are equal and larger")
elif b == c:
    print("b and c are equal and larger")
elif a == c:
    print("a and c are equal and larger")
else:
    print("invalid input")
print("#"*30) 