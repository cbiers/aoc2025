file = open("1/1/in.txt", "r")

moves = []

for line in file:
    line = line.strip()
    moves.append((line[0], int(line[1:])))

dial = 50
count = 0

for move in moves:
    direction, steps = move
    if direction == 'L':
        dial -= steps
    elif direction == 'R':
        dial += steps
    dial %= 100  # Wrap around the dial
    if dial == 0:
        count += 1

print(count)
file.close()