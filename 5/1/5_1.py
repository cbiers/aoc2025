example = False
with open("5/1/ex.txt" if example else "5/1/in.txt") as file: ranges = [tuple(map(int, line.strip().split("-"))) for line in file]
with open("5/1/ex_2.txt" if example else "5/1/in_2.txt") as file: ingredients = [int(line.strip()) for line in file]

count = 0
for ing in ingredients:
    for ra in ranges:
        low, hi = ra
        if low <= ing <= hi:
            count += 1
            break

print(count)