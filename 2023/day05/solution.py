import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")

    text = text_file.read()

    text_file.close()

    return text


text = read_text_file("dummy.txt")

almanac = [section.strip() for section in text.strip().split("\n\n")]

seeds = re.findall(r"\d+", almanac[0])

for map in almanac[1:]:
    lines = map.split("\n")

    for line in lines[1:]:
        data = re.findall(r"\d+", line)

        print(data)
        print("-" * 20)
