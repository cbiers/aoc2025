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
with open("8/2/ex.txt" if example else "8/2/in.txt") as f: points = [tuple(map(int, line.strip().split(","))) for line in f]

distances = [{"p1": points[i], "p2": points[j], "dist": distance(points[i], points[j])} for i in range(len(points)) for j in range(i + 1, len(points))]
distances.sort(key=lambda x: x["dist"])
circuits = [[point] for point in points]

i = 0
while len(circuits) > 1:
    circuit1 = get_circuit(circuits, distances[i]["p1"])
    circuit2 = get_circuit(circuits, distances[i]["p2"])
    if circuit1 != circuit2:
        circuits.remove(circuit1)
        circuits.remove(circuit2)
        circuits.append(circuit1 + circuit2)
    i += 1

print(distances[i-1]["p1"][0] * distances[i-1]["p2"][0])