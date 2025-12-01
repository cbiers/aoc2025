file = open("1/1/in.txt", "r")

moves = [(line[0], int(line[1:])) for line in file]

dial = 50
count = 0

for move in moves:
    direction, steps = move
    dial = (dial + (-steps if direction == 'L' else steps)) % 100
    if dial == 0:
        count += 1

print(count)
file.close()