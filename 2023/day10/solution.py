import re


def read_text_file(file_path="dummy.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

splitted_lines = [line.split() for line in lines]
grid = [[el for el in line[0]] for line in splitted_lines]


def find_location(grid, check_value="S"):
    location = []
    for i, row in enumerate(grid):
        if check_value in row:
            location = (i, row.index(check_value))

    return location


s_loc = find_location(grid)

s_left_tile = grid[s_loc[0]][s_loc[1] - 1]
s_top_tile = grid[s_loc[0] - 1][s_loc[1]]
s_right_tile = grid[s_loc[0]][s_loc[1] + 1]
s_bottom_tile = grid[s_loc[0] + 1][s_loc[1]]

tiles_near_s = [s_left_tile, s_top_tile, s_right_tile, s_bottom_tile]
sorted_tiles_near_s = [0 if tile == "." else 1 for tile in tiles_near_s]

s_value = None
if sorted_tiles_near_s == [1, 1, 0, 0]:
    s_value = "J"
if sorted_tiles_near_s == [0, 1, 1, 0]:
    s_value = "L"
if sorted_tiles_near_s == [0, 0, 1, 1]:
    s_value = "F"
if sorted_tiles_near_s == [1, 0, 0, 1]:
    s_value = "7"

grid[s_loc[0]][s_loc[1]] = s_value  # replace S to its actual value

pipe_direction = {
    "north": ["|", "7", "F"],
    "south": ["|", "L", "J"],
    "east": ["-", "J", "7"],
    "west": ["-", "L", "F"],
}

pipe_grid = grid
potential_s_values = []
for i, row in enumerate(grid):
    for j, tile in enumerate(row):

        if tile == ".":
            pipe_grid[i][j] = 0

        elif tile == "|" and grid[i + 1][j] in pipe_direction["south"]:
            pipe_grid[i + 1][j] = 1
        elif tile == "|" and grid[i - 1][j] in pipe_direction["north"]:
            pipe_grid[i - 1][j] = 1
        elif tile == "-" and grid[i][j + 1] in pipe_direction["east"]:
            pipe_grid[i][j + 1] = 1
        elif tile == "-" and grid[i][j - 1] in pipe_direction["west"]:
            pipe_grid[i][j - 1] = 1
        elif tile == "L" and grid[i - 1][j] in pipe_direction["north"]:
            pipe_grid[i - 1][j] = 1
        elif tile == "L" and grid[i][j + 1] in pipe_direction["east"]:
            pipe_grid[i][j + 1] = 1
        elif tile == "J" and grid[i - 1][j] in pipe_direction["north"]:
            pipe_grid[i - 1][j] = 1
        elif tile == "J" and grid[i][j - 1] in pipe_direction["west"]:
            pipe_grid[i][j - 1] = 1
        elif tile == "7" and grid[i + 1][j] in pipe_direction["south"]:
            pipe_grid[i + 1][j] = 1
        elif tile == "7" and grid[i][j - 1] in pipe_direction["west"]:
            pipe_grid[i][j - 1] = 1
        elif tile == "F" and grid[i + 1][j] in pipe_direction["south"]:
            pipe_grid[i + 1][j] = 1
        elif tile == "F" and grid[i][j + 1] in pipe_direction["east"]:
            pipe_grid[i][j + 1] = 1


print(pipe_grid)
