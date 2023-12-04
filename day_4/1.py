with open("input_1", "r") as f:
    lines = list(map( str.strip, f.readlines()))

# print(lines)
res = 0
for line in lines:
    # print(line)
    header, body = line.split(":")
    winning, current = body.split("|")
    winning = set(map(int, winning.strip().split()))
    current = set(map(int, current.strip().split()))

    guessed = winning.intersection(current)
    # print(guessed)
    if guessed:
        points = 2**(len(guessed) - 1)
        # print(guessed, points)
        res += points
    # print(winning, current)

print(res)