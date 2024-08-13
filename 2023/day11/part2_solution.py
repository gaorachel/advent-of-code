from itertools import combinations


def read_text_file(file_path="dummy.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()


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

################ Part2 ################

repeat_times = 1
empty_col = ["."] * repeat_times
matrix = splitted_lines
# for j, row in enumerate(matrix):
#     additional_cols = 1
#     for i in empty_space_col_locs:
#         matrix[j] = (
#             row[: i + additional_cols] + empty_col + row[i + 1 + additional_cols :]
#         )
#         additional_cols += repeat_times
# print(1111111, matrix)

for row in matrix:
    additional_cols = 1
    for i in empty_space_col_locs:
        row.insert(i + additional_cols, ".")
        additional_cols += 1

new_row_len = row_len + len(empty_space_row_locs)
empty_row = ["."] * new_row_len

additional_rows = 0
for i in empty_space_row_locs:
    matrix.insert(i + additional_rows, [empty_row for _ in range(repeat_times)])
    additional_rows += repeat_times

new_galaxy_locations = []
for i, row in enumerate(matrix):
    for j, node in enumerate(row):
        if node == "#":
            new_galaxy_locations.append((i, j))

pairs = list(combinations(new_galaxy_locations, 2))

total_distance = 0
for (x1, y1), (x2, y2) in pairs:
    distance = abs(x2 - x1) + abs(y2 - y1)
    total_distance += distance

print("Part2: ", total_distance)
# print(matrix)
