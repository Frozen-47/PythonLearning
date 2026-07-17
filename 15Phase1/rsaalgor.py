# RSA Encryption and Decryption

# Function to find GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find modular inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d

# Step 1: Choose two prime numbers
p = 3
q = 11

# Step 2: Compute n and phi
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose e
e = 3

if gcd(e, phi) != 1:
    print("Choose another value for e")
    exit()

# Step 4: Compute d
d = mod_inverse(e, phi)

print("Public Key:", (e, n))
print("Private Key:", (d, n))

# Message
message = 4

# Encryption
cipher = pow(message, e, n)
print("Encrypted Message:", cipher)

# Decryption
decrypted = pow(cipher, d, n)
print("Decrypted Message:", decrypted)