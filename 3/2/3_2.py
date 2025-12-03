from functools import reduce

def find_first_ascending_index(l, indices):
    for i in range(len(indices) - 1):
        if l[indices[i]] < l[indices[i + 1]]:
            return indices[i]
    return -1

def find_12_max_indices(line):
    max_indices = [i for i in range(12)]
    for i in range(12, len(line)):
        first_asc = find_first_ascending_index(line, max_indices)
        if first_asc != -1:
            max_indices.remove(first_asc)
            max_indices.append(i)
            continue
        min_index = min(max_indices, key=lambda x: line[x])
        if line[i] >= line[min_index]:
            max_indices.remove(min_index)
            max_indices.append(i)
    return [line[i] for i in max_indices]
        
with open("3/2/in.txt", "r") as file: lines = [list(line.strip())for line in file.readlines()]

print(sum([reduce(lambda x, y: x * 10 + y, map(int, find_12_max_indices(line))) for line in lines]))