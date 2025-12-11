from functools import cache

example = False
with open("11/2/ex.txt" if example else "11/1/in.txt") as file: devices = {name: outputs.split() for name, outputs in (line.strip().split(": ") for line in file)}

@cache
def find_paths_to(device, output_device):
    if output_device != "out" and device == "out":
        return 0
    elif device == output_device:
        return 1
    paths = 0
    for output in devices[device]:
        paths += find_paths_to(output, output_device)
    return paths

print(find_paths_to("svr", "fft") * find_paths_to("fft", "dac") * find_paths_to("dac", "out"))