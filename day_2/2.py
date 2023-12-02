with open("input_1", "r") as f:
    lines = list(map(str.strip, f.readlines()))

max_red = 12
max_green = 13
max_blue = 14
res = 0

for line in lines:
    game_name, game_moves = line.split(":")
    game_id = game_name.split(" ")[1]
    game_moves = game_moves.split(";")
    min_green = min_blue = min_red = -1
    for game in game_moves:
        game = game.strip()
        cubes = game.split(",")

        for cube in cubes:
            cube = cube.strip()
            if "green" in cube:
                greens = int(cube.split(" ")[0])
                min_green = max(greens, min_green)
            elif "blue" in cube:
                blues = int(cube.split(" ")[0])
                min_blue = max(blues, min_blue)
            elif "red" in cube:
                reds = int(cube.split(" ")[0])
                min_red = max(reds, min_red)
    power = min_green * min_blue * min_red
    res += power
    # print(min_green, min_blue, min_red)


print(res)
