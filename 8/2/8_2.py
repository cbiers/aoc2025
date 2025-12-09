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

example = False
lim = 10 if example else 1000
with open("8/2/ex.txt" if example else "8/2/in.txt") as f: points = [tuple(map(int, line.strip().split(","))) for line in f]

distances = [{"p1": points[i], "p2": points[j], "dist": distance(points[i], points[j])} for i in range(len(points)) for j in range(i + 1, len(points))]
distances.sort(key=lambda x: x["dist"])
circuits = [[point] for point in points]

i = 0
while len(circuits) > 1:
    p1, p2 = distances[i]["p1"], distances[i]["p2"]
    circuit1 = get_circuit(circuits, p1)
    circuit2 = get_circuit(circuits, p2)
    if circuit1 != circuit2:
        circuits.remove(circuit1)
        circuits.remove(circuit2)
        circuits.append(circuit1 + circuit2)
    i += 1

print(p1[0] * p2[0])