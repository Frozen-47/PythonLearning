'''def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def mod(a,b):
    return a%b

a = int(input("Enter A : "))
b = int(input("Enter B : "))
operation = input("Enter operations [+,-,*,/,%] : ")
match operation:
    case '+':
        print(add(a,b))
    case '-':
        print(sub(a,b))
    case '*':
        print(mul(a,b))
    case '/':
        print(div(a,b))
    case '%':
        print(mod(int(input("Enter  : ")),int(input("Enter divisor : "))))
    case _ :
        print("Invalid Operator")'''


'''def sabareesh():
    print("Name  : Sabareesh G")
    print("Age   : 19")
    print("Class : Third CT")
    return

def passingDetails(a,d,c):
    print(a,d,c)
    return
def directAllocation(a,c ,d ="sf"):
    print(a,c,d)
    return

sabareesh()
a = "paras"
b = 99
c = "Third CT"
print("="*20)
passingDetails(a,b,c)
print("="*200)
directAllocation(a="Mame",c = 5012,d="japan")'''


def name(n,text):
    if n <= 0:
        return
    print(text)
    return name(n-1,text)
name(10,"sabareesh")