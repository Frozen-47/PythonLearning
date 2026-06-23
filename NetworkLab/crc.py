def xor(a, b):
    result = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"
    return result
def crc_division(data, generator):
    padded = data + "0"*(len(generator)-1)
    remainder = padded[:len(generator)]
    for i in range(len(data)):
        if remainder[0] == "1":
            remainder = xor(remainder, generator)
        else:
            remainder = xor(remainder, "0"*len(generator))
        if i + len(generator) < len(padded):
            remainder = remainder[1:] + padded[i + len(generator)]
        else:
            remainder = remainder[1:]
    return remainder
data = input("Enter data: ")
generator = input("Enter generator: ")
remainder = crc_division(data, generator)
print("CRC Remainder:", remainder)
codeword = data + remainder
print("Transmitted data:", codeword)
