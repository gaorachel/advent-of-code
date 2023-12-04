import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()

    return lines


template = {
    "id": 0,
    "set1": {
        "red": 0,
        "green": 0,
        "blue": 0,
    },
    "set2": {
        "red": 0,
        "green": 0,
        "blue": 0,
    },
    "set3": {
        "red": 0,
        "green": 0,
        "blue": 0,
    },
}

id_pattern = r"Game (/d+):"


lines = read_text_file("dummy.txt")


rule = {"red": 12, "green": 13, "blue": 14}

id_sum = 0
for line in lines:
    [game_id, sets] = line.split(":")

    splitted_sets = sets.split(";")

    for set in splitted_sets:
        colours = re.findall("red|green|blue", set)
        values = list(map(int, re.findall(r"\d+", set)))

        max_colour_value = max(values)
        max_value_colour = colours[values.index(max_colour_value)]

        max_colour_value <= rule[max_value_colour]

        id = re.findall(r"\d+", game_id)[0]

        id_sum += int(id)

    #   for colour in rule.keys():
    #       if colour in colours:
    #           colour_value = values[colours.index(colour)]

    #           if int(colour_value) <= rule[colour]:
    #               id = re.findall(r"\d+", game_id)[0]

    #               # print(id)
    #               id_sum += int(id)

    #           else:
    #               None
print(id_sum)
