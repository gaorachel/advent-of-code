import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()


refined_lines = []
for line in lines:
    str_num_line = line.strip().split()
    int_num_line = [int(num) for num in str_num_line]

    refined_lines.append(int_num_line)

################ Part1 ################


def find_sequence_dff(list):
    list_diff = [list[i + 1] - list[i] for i in range(len(list) - 1)]

    return list_diff


total_history_value = 0
for line in refined_lines:

    list = line
    matrix_sequence_diff = []
    while sum(list) != 0:
        list = find_sequence_dff(list)
        matrix_sequence_diff.append(list)

    next_sequence_value = sum(row[-1] for row in matrix_sequence_diff)

    total_history_value += line[-1] + next_sequence_value


print("Part 1: ", total_history_value)
