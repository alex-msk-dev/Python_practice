'''
1 2 3 4
2 4 6 8
3 6 9 12
4 8 12 16
'''

N = [[i**j for j in range(1, 5)]
     for i in range(1, 5)]

print("Original Matrix")
for i in range(0, 4):
    row = ''
    for j in range(0, 4):
        cell = N[i][j]
        cell_formated = f'{cell: <3}'
        if row:
            row = row + ', '
        row = row + cell_formated
    print(row)

M = 3

for i in range(0, 4):
    for j in range(0, 4):
        cell = N[i][j]
        cell = cell * M
        N[i][j] = cell

print(f"Matrix multiplied by (n)")

for i in range(0, 4):
    row = ''
    for j in range(0, 4):
        cell = N[i][j]
        cell_formated = f'{cell: <3}'
        if row:
            row = row + ', '
        row = row + cell_formated
    print(row)