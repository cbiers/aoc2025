example = True
with open("6/2/ex.txt" if example else "6/2/in.txt") as file: lines = [line.strip() for line in file]
nums = [[x[::-1] for x in lines[i].split(" ") if x != ""] for i in range(len(lines) - 1)]
ops = [o for o in lines[-1].split(" ") if o != ""]

lim = 3 if example else 4

nums2 = [[[0 for _ in range(lim)] for _ in range(lim)] for _ in range(len(nums[0]))] 

for i in range(len(nums)):
    for j in range(len(nums[i])):
        for k in range(lim):
            if len(nums[i][j]) > k:
                nums2[j][k][i] = int(nums[i][j][k])

res = 0
for i in range(len(nums2)):
    curr = 0 if ops[i] == "+" else 1
    for j in range(len(nums2[i])):
        num = 0
        for k in range(lim - 1, -1, -1):
            if nums2[i][j][k] != 0:
                num += nums2[i][j][k]
                num *= 10
        num = int(str(num)[::-1])
        if num != 0:
            curr = curr + num if ops[i] == "+" else curr * num
    res += curr

print(res)