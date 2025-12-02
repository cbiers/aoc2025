with open("2/1/in.txt", "r") as file: ranges = [map(int, part.split("-")) for part in file.readline().strip().split(',')]

sum = 0

for (start, end) in ranges:
    for i in range(start, end + 1):
        s = str(i)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            if s[:mid] == s[mid:]:
                sum += i

print(sum)