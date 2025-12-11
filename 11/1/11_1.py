example = False
with open("11/1/ex.txt" if example else "11/1/in.txt") as file: devices = {name: outputs.split() for name, outputs in (line.strip().split(": ") for line in file)}

def count_paths(device, output_device):
    if device == output_device:
        return 1
    return sum(count_paths(output, output_device) for output in devices[device])

print(count_paths("you", "out"))