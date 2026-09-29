import sys

m, n = map(int, input("Enter row and col: ").split())

matrix = []

for _ in range(m):
    row = list(map(int, input().split()))

    if len(row) == n:
        matrix.append(row)
    else:
        sys.exit(f"Row should contain {n} values , ReRUN with proper inputs !!!")

result = []
row = col = 0

for _ in range(m * n):
    result.append(matrix[row][col])

    # Moving upward-right ↗
    if (row + col) % 2 == 0:
        if col == n - 1:
            row += 1
        elif row == 0:
            col += 1
        else:
            row -= 1
            col += 1

    # Moving downward-left ↙
    else:
        if row == m - 1:
            col += 1
        elif col == 0:
            row += 1
        else:
            row += 1
            col -= 1

print("Diagonal order:", result)