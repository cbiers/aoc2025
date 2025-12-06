example = False
with open("6/1/ex.txt" if example else "6/1/in.txt") as file: lines = [line.strip() for line in file]
nums = [[int(x) for x in lines[i].split(" ") if x != ""] for i in range(len(lines) - 1)]
ops = [o for o in lines[-1].split(" ") if o != ""]

res = 0
for i in range(len(ops)):
    op = ops[i]
    curr = 0 if op == "+" else 1
    for j in range(len(nums)):
        curr = curr + nums[j][i] if op == "+" else curr * nums[j][i]
    res += curr

print(res)