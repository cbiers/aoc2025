file = open("1/1/in.txt", "r")

moves = [(line[0], int(line[1:])) for line in file]

dial = 50
count = 0
was = False

for move in moves:
    direction, steps = move
    dial = dial + (-steps if direction == 'L' else steps)
    if dial < 0 or dial >= 100:
        count += abs(dial // 100)
        if was and dial < 0:
            count -= 1
        if dial < 0 and dial % 100 == 0:
            count += 1
    elif dial == 0 and not was:
        count += 1
    dial %= 100
    was = dial == 0

print(count)
file.close()