def find_max(l, start, end):
    max, max_index = l[start], start
    max_index = start
    for i in range(start + 1, end + 1):
        if l[i] > max:
            max, max_index = l[i], i
    return max_index

with open("3/1/in.txt", "r") as file: lines = [list(line.strip())for line in file.readlines()]

sum = 0

for line in lines:
    max_i = find_max(line, 0, len(line) - 1)
    if max_i != len(line) - 1:
        max_i_2 = find_max(line, max_i + 1, len(line) - 1)
    else:
        max_i_2 = max_i
        max_i = find_max(line, 0, len(line) - 2)
    sum += int(line[max_i]) * 10 + int(line[max_i_2])

print(sum)