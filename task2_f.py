

maze = [
    ['.', '.', 'S', '.', '.'],
    ['.', 'T', '.', '.', '.'],
    ['.', '.', '.', 'T', '.'],
    ['.', '.', '.', '.', '.'],
    ['T', '.', '.', '.', '.']
]

start_pos = None
task_positions = []

for row in range(len(maze)):
    for col in range(len(maze[row])):
        if maze[row][col] == 'S':
            start_pos = (row, col)
        if maze[row][col] == 'T':
            task_positions.append((row, col))

print("Start found at:", start_pos)
print("Tasks found at:", task_positions)
