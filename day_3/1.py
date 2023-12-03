with open("input_1", "r") as f:
    lines = list(map(str.strip, f.readlines()))

grid = []

for line in lines:
    to_append = list()
    for sym in line:
        if sym.isdigit():
            to_append.append(sym)
        elif sym == ".":
            to_append.append("P")
        else:
            to_append.append("S")

    grid.append(to_append)


def check_adj_cells(grid, x, y):
    # print("checking", x, y)
    if x == len(grid[0])-1 and y == len(grid)-1:
        to_check = [grid[y - 1][x - 1], grid[y - 1][x],  grid[y][x - 1]]
    elif x == len(grid[0])-1:
        to_check = [grid[y - 1][x - 1], grid[y - 1][x], grid[y + 1][x], grid[y + 1][x - 1], grid[y][x - 1]]
    elif y == len(grid)-1:
        to_check = [grid[y - 1][x - 1], grid[y - 1][x], grid[y - 1][x + 1], grid[y][x + 1], grid[y][x - 1]]
    else:
        to_check = [grid[y - 1][x - 1], grid[y - 1][x], grid[y - 1][x + 1], grid[y][x + 1],
                    grid[y + 1][x + 1], grid[y + 1][x], grid[y + 1][x - 1], grid[y][x - 1]]
        if x == 0 and y == 0:
            to_check = [grid[y][x + 1], grid[y + 1][x + 1], grid[y + 1][x]]
        elif y == 0:
            to_check = [grid[y][x + 1], grid[y + 1][x + 1], grid[y + 1][x], grid[y + 1][x - 1], grid[y][x - 1]]
        elif x == 0:
            to_check = [grid[y - 1][x], grid[y - 1][x + 1], grid[y][x + 1], grid[y + 1][x + 1], grid[y + 1][x]]
    for check in to_check:
        if check == "S":
            return True

    return False


res = 0
on_num = "NO"
# "YES"
# "FOUND"
num_start_ind = 0
num_count = 0
for y in range(len(grid)):
    for x in range(len(grid[0])):
        sym = grid[y][x]
        if sym.isdigit():
            if on_num == "FOUND":
                continue

            if on_num == "NO":
                num_start_ind = x
                on_num = "YES"
            if check_adj_cells(grid, x, y):
                on_num = "FOUND"

        else:
            if on_num == "FOUND":
                num = grid[y][num_start_ind:x]
                on_num = "NO"
                res += int("".join(num))
                num_count += 1
            elif on_num == "YES":
                on_num = "NO"
    if on_num == "FOUND":
        num = grid[y][num_start_ind:x+1]
        on_num = "NO"
        res += int("".join(num))
        num_count += 1
    on_num = "NO"
    num_start_ind = 0


# print(num_count)
print(res)
