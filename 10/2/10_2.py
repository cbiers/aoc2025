example = True
machines = []
with open("10/2/ex.txt" if example else "10/2/in.txt") as file:
    for line in file:
        current = {}
        parts = line.strip().split()
        lights = []
        for c in parts[0][1:-1]:
            lights.append(1 if c == "#" else 0)
        current["lights"] = lights
        buttons = []
        for p in parts[1:-1]:
            button = []
            for b in p[1:-1].split(","):
                button.append(int(b))
            buttons.append(button)
        current["buttons"] = buttons
        joltage = []
        for j in parts[-1][1:-1].split(","):
            joltage.append(int(j))
        current["joltage"] = joltage
        machines.append(current)

for machine in machines:
    for i in range(len(machine["joltage"])):

        for button in machine["buttons"]:
            if i in button:
                machine["joltage"][i] -= 1
def min_button_presses_bfs(machine, init_joltages, presses):
    from collections import deque

    queue = deque()
    queue.append((init_joltages, presses))
    visited = set()
    visited.add(tuple(init_joltages))

    while queue:
        current_joltages, current_presses = queue.popleft()

        if current_joltages == machine["joltage"]:
            return current_presses

        for button in machine["buttons"]:
            new_joltages = press_button(current_joltages, button)
            jolt_tuple = tuple(new_joltages)
            if jolt_tuple not in visited:
                visited.add(jolt_tuple)
                queue.append((new_joltages, current_presses + 1))

    return float("inf")

def press_button(joltages, button):
    new_joltages = joltages[:]
    for idx in button:
        new_joltages[idx] += 1
    return new_joltages

res = 0
for machine in machines:
    print("machine No.:", machines.index(machine) + 1)
    init_joltages = [0] * len(machine["joltage"])
    res += min_button_presses_bfs(machine, init_joltages, 0)

print(res)
