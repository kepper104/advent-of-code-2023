with open("input_1", "r") as f:
    lines = list(map(str.strip, f.readlines()))

grid = []
storage = []

for line in lines:
    to_append = list()
    to_app_storage = list()
    for sym in line:
        to_app_storage.append(list())
        if sym.isdigit():
            to_append.append(sym)
        elif sym == ".":
            to_append.append("P")
        elif sym == "*":
            to_append.append("*")
        else:
            to_append.append("P")

    grid.append(to_append)
    storage.append(to_app_storage)


def handle_adj_cells(grid, x, y, storage):
    # print("checking", x, y)
    if x == len(grid[0])-1 and y == len(grid)-1:
        to_check = [(-1, -1), (-1, 0),  (0, -1)]
    elif y == len(grid[0])-1:
        to_check = [(-1, -1), (-1, 0), (+1, 0), (+1, -1), (0, -1)]
    elif x == len(grid)-1:
        to_check = [(-1, -1), (-1, 0), (-1, +1), (0, +1), (0, -1)]
    else:
        to_check = [(-1, -1), (-1, 0), (-1, +1), (0, +1),
                    (+1, +1), (+1, 0), (+1, -1), (0, -1)]
        if x == 0 and y == 0:
            to_check = [(0, +1), (+1, +1), (+1, 0)]
        elif x == 0:
            to_check = [(0, +1), (+1, +1), (+1, 0), (+1, -1), (0, -1)]
        elif y == 0:
            to_check = [(-1, 0), (-1, +1), (0, +1), (+1, +1), (+1, 0)]

    for check in to_check:
        # print(check, x, y)
        star_y = y+check[1]
        star_x = x+check[0]
        sym = grid[star_y][star_x]
        if sym == "*":
            if (x, y) not in storage[star_y][star_x]:
                storage[star_y][star_x] += [(x, y)]
            add_number_to_left(grid, storage, star_x, star_y, x-1, y)
            add_number_to_right(grid, storage, star_x, star_y, x+1, y)
            # return True


def add_number_to_left(grid, storage, star_x, star_y, x, y):
    if x >= 0:
        if grid[y][x].isdigit():
            if (x, y) not in storage[star_y][star_x]:
                storage[star_y][star_x] += [(x, y)]
            add_number_to_left(grid, storage, star_x, star_y, x - 1, y)


def add_number_to_right(grid, storage, star_x, star_y, x, y):
    if x < len(grid[0]):
        if grid[y][x].isdigit():
            if (x, y) not in storage[star_y][star_x]:
                storage[star_y][star_x] += [(x, y)]
            add_number_to_right(grid, storage, star_x, star_y, x + 1, y)
    # return False


res = 0


for y in range(len(grid)):
    for x in range(len(grid[0])):
        sym = grid[y][x]
        if sym.isdigit():
            handle_adj_cells(grid, x, y, storage)


for line in storage:
    # print(line)
    # continue
    for cell in line:
        if not cell:
            continue
        # print(cell, end=", ")
        cell = sorted(cell, key=lambda x: (x[1], x[0]))
#         print(cell)
        all_y_are_same = all(list(map(lambda x: x[1] == cell[0][1], cell)))
        # print(all_y_are_same)

        if all_y_are_same:
            # print("SAME LEVEL")
            num_1 = ""
            num_2 = ""
            num_n = "1"
            for ind, num in enumerate(cell):
                if ind == 0:
                    num_1 += grid[num[1]][num[0]]
                else:
                    if num_n == "1":
                        if cell[ind][0] == cell[ind-1][0] + 1:
                            num_1 += grid[num[1]][num[0]]
                        else:
                            num_n = "2"
                            num_2 += grid[num[1]][num[0]]
                    elif num_n == "2":
                        num_2 += grid[num[1]][num[0]]

        elif not all_y_are_same:
            # print("DIFF LEVEL")

            # print(cell)
            prev_y = -1
            num_1 = ""
            num_2 = ""
            num_n = "1"
            for ind, num in enumerate(cell):
                # print(num)
                if ind == 0:
                    prev_y = num[1]
                    num_1 += grid[num[1]][num[0]]
                else:
                    if num_n == "1":
                        if num[1] == prev_y:
                            num_1 += grid[num[1]][num[0]]
                        else:
                            num_n = "2"
                            num_2 += grid[num[1]][num[0]]
                    elif num_n == "2":
                        num_2 += grid[num[1]][num[0]]

        if num_2:
            res += int(num_1) * int(num_2)
            # print(num_1, num_2)

# print(num_count)
print(res)
