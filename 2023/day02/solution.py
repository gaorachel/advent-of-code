from utils import read_text_file
import re

lines = read_text_file()

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
