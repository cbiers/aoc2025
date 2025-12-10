example = False
with open("9/1/ex.txt" if example else "9/1/in.txt") as file: points = [list(map(int, line.strip().split(","))) for line in file]

best = 0

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        xmin = min(points[i][0], points[j][0])
        xmax = max(points[i][0], points[j][0])
        ymin = min(points[i][1], points[j][1])
        ymax = max(points[i][1], points[j][1])
        rect_size = (xmax - xmin + 1) * (ymax - ymin + 1)
        if rect_size > best:
            best = rect_size
            
print(best)