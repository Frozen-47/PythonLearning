data = []
rows = 4

for i in range(rows):
    row = input(f"Sender - Enter row {i+1}: ")
    data.append(row)

lrc = ""
for col in zip(*data):
    if col.count('1') % 2 == 0:
        lrc += '0'
    else:
        lrc += '1'

print("Sender - LRC generated:", lrc)

print("\nReceiver - Enter received data:")

received = []
for i in range(rows):
    row = input(f"Receiver - Enter row {i+1}: ")
    received.append(row)

actual_lrc = input("Receiver - Enter received LRC: ")

expected_lrc = ""
for col in zip(*received):
    if col.count('1') % 2 == 0:
        expected_lrc += '0'
    else:
        expected_lrc += '1'

print("Expected LRC:", expected_lrc)

if expected_lrc == actual_lrc:
    print("No error detected")
else:
    print("Error detected")
