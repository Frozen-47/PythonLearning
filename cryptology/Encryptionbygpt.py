message = input("Enter Message: ")
key = int(input("Enter Key (0-255): "))

blocks = [ord(ch) for ch in message]
blocks.reverse()

encrypted = "".join(chr((b + key) % 256) for b in blocks)

print("Encrypted:", encrypted)