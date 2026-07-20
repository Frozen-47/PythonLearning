v = int(input())

while v > 9:
    s = 0
    while(v != 0):
        s += v % 10
        v = v // 10
    v = s
print(int(v))
