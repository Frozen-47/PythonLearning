str = input()
chars = list(str)
print(chars)
vowel = "aeiouAEIOU"
l = 0
r = len(str)-1
while l < r:
    while chars[l] not in vowel:
        l += 1
    while chars[r] not in vowel:
        r -= 1
    chars[l],chars[r] = chars[r],chars[l] 
    l += 1
    r -= 1
print(chars)