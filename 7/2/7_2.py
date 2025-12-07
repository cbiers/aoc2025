example = False
with open("7/2/ex.txt" if example else "7/2/in.txt") as file: grid = [[c for c in line.strip()] for line in file]

grid[0][grid[0].index('S')] = 1

for i in range(1, len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == ".":
            if grid[i - 1][j] not in [".", "^"]:
                grid[i][j] = grid[i - 1][j]
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            if grid[i - 1][j] not in [".", "^"]:
                if j > 0:
                    if grid[i][j - 1] == ".":
                        grid[i][j - 1] = grid[i - 1][j]
                    else:
                        grid[i][j - 1] += grid[i - 1][j]
                if j < len(grid[i]) - 1:
                    if grid[i][j + 1] == ".":
                        grid[i][j + 1] = grid[i - 1][j]
                    else:
                        grid[i][j + 1] += grid[i - 1][j]

print(sum(el for el in grid[-1] if el != "." and el != "^"))
         