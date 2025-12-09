from shapely.geometry import Point
from shapely.geometry.polygon import Polygon

example = False
with open("ex.txt" if example else "in.txt") as file: points = [Point(p[0], p[1]) for p in [list(map(int, line.strip().split(","))) for line in file]]
poly = Polygon(points)

best = 0

for pa in points:
    for pb in points:
        xmin = min(pa.x, pb.x)
        xmax = max(pa.x, pb.x)
        ymin = min(pa.y, pb.y)
        ymax = max(pa.y, pb.y)
        poly2 = Polygon([Point(xmin, ymin), Point(xmin, ymax), Point(xmax, ymax), Point(xmax, ymin)])
        rect_size = (xmax - xmin + 1) * (ymax - ymin + 1)
        if poly.contains(poly2) and rect_size > best:
            best = rect_size
print(best)