import re
import math


def read_text_file(file_path="dummy.txt"):
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
    node for node in range(row_len) if node not in [t[0] for t in galaxy_locations]
]
empty_space_col_locs = [
    node for node in range(col_len) if node not in [t[1] for t in galaxy_locations]
]

new_row_len = row_len + len(empty_space_row_locs)
new_col_len = col_len + len(empty_space_col_locs)


matrix = splitted_lines

for row in matrix:
    for i in empty_space_col_locs:
        row.insert(i, ".")

for i in empty_space_row_locs:
    matrix.insert(i, ["."] * new_row_len)
# new_galaxy_locations = []
# for i, row in enumerate(matrix):
#     for j, node in enumerate(row):
#         matrix.insert(matrix[i][j], ["."])

# # print(1, node)
# if node == "#":
#     new_galaxy_locations.append((i, j))

print(matrix)
