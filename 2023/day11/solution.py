from itertools import combinations


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

################ Part1 ################


splitted_lines = []
galaxy_locations = []
for i, line in enumerate(lines):
    refined_line = list(line.split()[0])
    splitted_lines.append(refined_line)

    for j, node in enumerate(refined_line):
        if node == "#":
            galaxy_locations.append((i, j))

row_len = len(splitted_lines[0])
col_len = len(splitted_lines)

empty_space_row_locs = [
    node for node in range(row_len) if node not in [x for x, _ in galaxy_locations]
]
empty_space_col_locs = [
    node for node in range(col_len) if node not in [y for _, y in galaxy_locations]
]

new_row_len = row_len + len(empty_space_row_locs)

matrix = splitted_lines
for row in matrix:
    additional_cols = 1
    for i in empty_space_col_locs:
        row.insert(i + additional_cols, ".")
        additional_cols += 1

additional_rows = 0
for i in empty_space_row_locs:
    matrix.insert(i + additional_rows, ["."] * new_row_len)
    additional_rows += 1

new_galaxy_locations = []
for i, row in enumerate(matrix):
    for j, node in enumerate(row):
        if node == "#":
            new_galaxy_locations.append((i, j))

pairs = list(combinations(new_galaxy_locations, 2))

total_distance = 0
i = 1
for (x1, y1), (x2, y2) in pairs:
    distance = abs(x2 - x1) + abs(y2 - y1)
    total_distance += distance

print("Part1: ", total_distance)
