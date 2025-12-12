example = False
problems = []
sizes = [7] * 6 if example else [6, 7, 7, 7, 6, 7]
with open("12/1/ex_2.txt" if example else "12/1/in_2.txt") as file:
    for line in file:
        parts = line.strip().split()
        size = list(map(int, parts[0][:-1].split("x")))
        coefficients = list(map(int, parts[1:]))
        problems.append({"size": size, "coefficients": coefficients})

count = 0
for problem in problems:
    area = problem["size"][0] * problem["size"][1]
    total = 0
    for i in range(len(problem["coefficients"])):
        total += problem["coefficients"][i] * sizes[i]
    if total <= area:
        count += 1

print(count)