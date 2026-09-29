m,n = map(int,input("Enter row and col :").split())
matrix = []
for _ in range(m):
    row = list(map(int,input().split()))
    matrix.append(row)

result = []
row = col = 0

for _ in range(m*n):
    result.append(matrix[row][col])
    if (row+col)%2 == 0:
        if col == n-1:
            row += 1
        elif row == 0:
            col += 1
        else:
            row -= 1
            col += 1
    else:
        if row == m-1:
            col += 1
        elif col == 0:
            row += 1
        else:
            row += 1
            col -= 1

print(result)