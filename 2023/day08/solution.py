import re
from collections import Counter


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file("dummy.txt")

instruction = lines[0]
nodes = lines[2:]


def sort_nodes(nodes):
    node_list = []
    following_nodes = []
    for node in nodes:
        sorted_node = re.findall(r"\b[A-Z]+\b", node)
        node_list.append(sorted_node[0])
        following_nodes.append(sorted_node[1:])

    return node_list, following_nodes


node_list, following_nodes = sort_nodes(nodes)

print(1, node_list)

steps = 1
i = 1
if instruction[0] == "L":
    start = following_nodes[0][0]
else:
    start = following_nodes[0][1]

while i < len(instruction):
    next_node_index = node_list.index(start)
    next_node = node_list[next_node_index]

    print(next_node)
    if next_node != "ZZZ":
        if instruction[i] == "L":
            start = following_nodes[next_node_index][0]
        else:
            start = following_nodes[next_node_index][1]

        steps += 1
        i += 1 if i != len(instruction) - 1 else 0
    else:
        break

print(steps)
