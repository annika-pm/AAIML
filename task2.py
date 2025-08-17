

ascii_grid = [
    ['-', '-', 'S', '-', '-'],
    ['-', 'T', '-', '-', '-'],
    ['-', '-', '-', 'T', '-'],
    ['-', '-', '-', '-', '-'],
    ['T', '-', '-', '-', '-']
]


start = None
tasks = []

for i in range(len(ascii_grid)):
    for j in range(len(ascii_grid[i])):
        if ascii_grid[i][j] == 'S':
            start = (i, j)
        elif ascii_grid[i][j] == 'T':
            tasks.append((i, j))


print("Start position (S):", start)
print("Task cells (T):", tasks)
