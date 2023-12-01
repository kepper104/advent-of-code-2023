total_sum = 0
with open("input_1", "r") as f:
    lines = list(map(str.strip, f.readlines()))
# print(lines)

for line in lines:
    res = ""
    for symbol in line:
        if symbol.isdigit():
            res += symbol
    total_sum += int(res[0] + res[-1])
print(total_sum)
