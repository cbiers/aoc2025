with open("4/1/in.txt") as f: grid = [[el for el in line.strip()] for line in f.readlines()]

def fewer_4_adjacent(x, y):
    count = 0
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (1, -1), (1, 0), (1, 1), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == '@':
                count += 1
    return count < 4

count = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '@':
            if fewer_4_adjacent(i, j):
                count += 1
print(count)