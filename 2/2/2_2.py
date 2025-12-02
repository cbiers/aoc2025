with open("2/1/ex.txt", "r") as file: ranges = [map(int, part.split("-")) for part in file.readline().strip().split(',')]

sum = 0

for (start, end) in ranges:
    for i in range(start, end + 1):
        s = str(i)
        for j in range(1, len(s) // 2 + 1):
            if len(s) % j == 0:
                substrings = [s[k:k + j] for k in range(0, len(s), j)]
                if all(sub == substrings[0] for sub in substrings):
                    sum += i
                    break

print(sum)