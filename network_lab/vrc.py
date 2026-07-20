data = input("Enter binary data: ")
count = data.count('1')

if count % 2 == 0:
    parity = '0'
else:
    parity = '1'

transmitted = data + parity
print("Transmitted data:", transmitted)

received = input("Enter received data: ")
if received.count('1') % 2 == 0:
    print("No error detected")
else:
    print("Error detected")
