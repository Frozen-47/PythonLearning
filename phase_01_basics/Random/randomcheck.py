import random

key = int(input("Enter a three digit number: "))

while key < 100 or key > 999:
    print("Just three digits!")
    key = int(input("Enter a three digit number: "))

guessed = set()
attempts = 0

while True:
    find = random.randint(100, 999)


    if find in guessed:
        continue

    guessed.add(find)
    attempts += 1

    if key == find:
        print(f"{key} == {find}")
        break

    print(f"{key} != {find}")

print(f"Found after {attempts} attempts!")