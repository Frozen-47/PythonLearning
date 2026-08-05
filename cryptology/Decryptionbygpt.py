cipher = input("Enter Cipher: ")
key = int(input("Enter Key (0-255): "))

blocks = [(ord(ch) - key) % 256 for ch in cipher]
blocks.reverse()

message = "".join(chr(b) for b in blocks)

print("Decrypted:", message)