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
    bad = False
    for game in game_moves:
        game = game.strip()
        cubes = game.split(",")

        for cube in cubes:
            cube = cube.strip()
            if "green" in cube:
                greens = int(cube.split(" ")[0])
                if greens > max_green:
                    bad = True
                    break
            elif "blue" in cube:
                blues = int(cube.split(" ")[0])
                if blues > max_blue:
                    bad = True
                    break
            elif "red" in cube:
                reds = int(cube.split(" ")[0])
                if reds > max_red:
                    bad = True
                    break
        if bad:
            break

    if not bad:
        res += int(game_id)


print(res)
