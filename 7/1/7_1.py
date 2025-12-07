example = False
with open("7/1/ex.txt" if example else "7/1/in.txt") as file: grid = [line.strip() for line in file]

beams = [False for i in range(len(grid[0]))]
beams[grid[0].index('S')] = True

splits = 0
curr_line = 0

while curr_line < len(grid) - 1:
    curr_line += 1
    for i in range(len(grid[0])):
        if beams[i] and grid[curr_line][i] == '^':
            beams[i-1] = True
            beams[i+1] = True
            beams[i] = False
            splits += 1

print(splits)