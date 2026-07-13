c = int(input())
answer = []

if c <= 26:
    print(chr(64 + c))
else:
    while c != 0:
        c -= 1
        temp = c % 26
        answer.append(chr(65 + temp))
        c = c // 26

    ans = "".join(answer[::-1])
    print(ans)