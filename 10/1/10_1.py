example = False
machines = []
with open("10/1/ex.txt" if example else "10/1/in.txt") as file:
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

def min_button_presses_bfs(machine, init_lights, presses):
    from collections import deque

    target_lights = machine["lights"]
    buttons = machine["buttons"]

    queue = deque()
    queue.append((init_lights, presses))
    visited = set()
    visited.add(tuple(init_lights))

    while queue:
        current_lights, current_presses = queue.popleft()

        if current_lights == target_lights:
            return current_presses

        for button in buttons:
            new_lights = press_button(current_lights, button)
            lights_tuple = tuple(new_lights)
            if lights_tuple not in visited:
                visited.add(lights_tuple)
                queue.append((new_lights, current_presses + 1))

    return float("inf")

def press_button(lights, button):
    new_lights = lights[:]
    for idx in button:
        new_lights[idx] ^= 1
    return new_lights

res = 0
for machine in machines:
    init_lights = [0] * len(machine["lights"])
    res += min_button_presses_bfs(machine, init_lights, 0)

print(res)
