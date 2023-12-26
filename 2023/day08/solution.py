import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

instruction = lines[0]
nodes = lines[2:]

node_list = []
next_notes = []
for node in nodes:
    sorted_node = re.findall(r"\b[A-Z]+\b", node)
    node_list.append(sorted_node[0])
    next_notes.append(sorted_node[1:])

steps = 0
i = 0
current_node = "AAA"
while current_node != "ZZZ":
    current_node_index = node_list.index(current_node)

    current_node = (
        next_notes[current_node_index][0]
        if instruction[i] == "L"
        else next_notes[current_node_index][1]
    )

    steps += 1
    i = (i + 1) % (len(instruction) - 1)


print("Part 1 number of steps required is", steps)
