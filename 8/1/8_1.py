from math import sqrt
from functools import cache

@cache
def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def find_smallest_distance(points, chosen):
    min_dist = float('inf')
    closest_pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            if (points[i], points[j]) in chosen or (points[j], points[i]) in chosen:
                continue
            dist = distance(points[i], points[j])
            if dist < min_dist:
                min_dist = dist
                closest_pair = (points[i], points[j])
    return closest_pair

def get_circuit(circuits, point):
    for circuit in circuits:
        if point in circuit:
            return circuit
    return None

def product_of_3_largest_lengths(circuits):
    lengths = sorted([len(circuit) for circuit in circuits], reverse=True)
    return lengths[0] * lengths[1] * lengths[2] if len(lengths) >= 3 else 0

example = False
lim = 10 if example else 1000
with open("8/1/ex.txt" if example else "8/1/in.txt") as f: points = [tuple(map(int, line.strip().split(","))) for line in f]

circuits = []
for point in points:
    circuits.append([point])

chosen = []
for i in range(lim):
    print(f"Iteration {i}")
    p1, p2 = find_smallest_distance(points, chosen)
    chosen.append((p1, p2))
    for circuit in circuits:
        c1 = get_circuit(circuits, p1)
        c2 = get_circuit(circuits, p2)
        if p1 in c2 or p2 in c1:
            continue
        c1.extend(c2)
        circuits.remove(c2)

print(product_of_3_largest_lengths(circuits))