from functools import cache

example = False
with open("11/2/ex.txt" if example else "11/1/in.txt") as file: devices = {name: outputs.split() for name, outputs in (line.strip().split(": ") for line in file)}

@cache
def count_paths(device, output_device):
    if output_device != "out" and device == "out":
        return 0
    elif device == output_device:
        return 1
    return sum(count_paths(output, output_device) for output in devices[device])

print(count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"))