import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

################ Part1 ################

worth_point_sum = 0
for line in lines:
    [card_id, all_numbers] = line.split(": ")

    [winning_numbers, having_numbers] = all_numbers.split("|")

    winning_numbers = re.findall(r"\d+", winning_numbers)
    having_numbers = re.findall(r"\d+", having_numbers)

    matching_numbers = set(winning_numbers).intersection(set(having_numbers))

    if len(matching_numbers) >= 2:
        worth_points = 2 ** (len(matching_numbers) - 1)
    elif len(matching_numbers) == 1:
        worth_points = 1
    else:
        worth_points = 0

    worth_point_sum += worth_points

print("Part 1 Sum of Worth Points is: ", worth_point_sum)
