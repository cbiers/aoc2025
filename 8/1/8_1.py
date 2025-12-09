from math import sqrt

def distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

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

distances = [{"p1": points[i], "p2": points[j], "dist": distance(points[i], points[j])} for i in range(len(points)) for j in range(i + 1, len(points))]
distances.sort(key=lambda x: x["dist"])

circuits = [[point] for point in points]

for i in range(lim):
    circuit1 = get_circuit(circuits, distances[i]["p1"])
    circuit2 = get_circuit(circuits, distances[i]["p2"])
    if circuit1 != circuit2:
        circuits.remove(circuit1)
        circuits.remove(circuit2)
        circuits.append(circuit1 + circuit2)

print(product_of_3_largest_lengths(circuits))