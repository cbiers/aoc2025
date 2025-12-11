example = False
with open("11/1/ex.txt" if example else "11/1/in.txt") as file: devices = {name: outputs.split() for name, outputs in (line.strip().split(": ") for line in file)}

def number_of_paths_to_out(device):
    if device == "out":
        return 1
    total_paths = 0
    for output in devices[device]:
        total_paths += number_of_paths_to_out(output)
    return total_paths

print(number_of_paths_to_out("you"))