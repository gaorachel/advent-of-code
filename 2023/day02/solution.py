import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

################ Part1 ################

rule = {"red": 12, "green": 13, "blue": 14}

id_sum = 0
for line in lines:
    [game_id, sets] = line.split(":")

    colours = re.findall("red|green|blue", sets)
    values = list(map(int, re.findall(r"\d+", sets)))

    max_colour_value = max(values)
    max_value_colour = colours[values.index(max_colour_value)]

    if max_colour_value <= rule[max_value_colour]:
        id = re.findall(r"\d+", game_id)[0]

        id_sum += int(id)

print("Part1 Sum of IDs is: ", id_sum)

################ Part2 ################

power_sum = 0
for line in lines:
    [game_id, sets] = line.split(":")

    set_power = 1
    for colour in ["red", "green", "blue"]:
        single_colour_values = list(map(int, re.findall(rf"(\d+) {colour}", sets)))
        max_single_colour_value = max(single_colour_values)

        set_power *= max_single_colour_value

    power_sum += set_power

print("Part2 Sum of Power is: ", power_sum)
