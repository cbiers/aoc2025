example = False
with open("5/2/ex.txt" if example else "5/2/in.txt") as file: ranges = sorted([tuple(map(int, line.strip().split("-"))) for line in file])

merged = [ranges[0]]
for start, end in ranges[1:]:
    if merged[-1][1] >= start - 1:
        merged[-1] = (merged[-1][0], max(merged[-1][1], end))
    else:
        merged.append((start, end))

print(sum(range[1] - range[0] + 1 for range in merged))