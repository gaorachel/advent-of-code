import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")

    text = text_file.read()

    text_file.close()

    return text


text = read_text_file()

almanac = [section.strip() for section in text.strip().split("\n\n")]

seeds = re.findall(r"\d+", almanac[0])


def map_numbers(seed_number):
    destination_number = None
    source_number = seed_number if destination_number == None else destination_number
    for map in almanac[1:]:
        lines = map.split("\n")

        destination_numbers = []
        source_numbers = []
        for line in lines[1:]:
            [destination, source, range_len] = re.findall(r"\d+", line)

            for d in range(int(destination), int(destination) + int(range_len)):
                destination_numbers.append(d)

            for s in range(int(source), int(source) + int(range_len)):
                source_numbers.append(s)

        if source_number in source_numbers:
            source_number_index = source_numbers.index(source_number)
            destination_number = destination_numbers[source_number_index]
        else:
            destination_number = source_number

        source_number = destination_number

        # print(source_number, destination_number)

    return destination_number


location_numbers = []
for seed in seeds:
    location_number = map_numbers(int(seed))

    location_numbers.append(location_number)
print(location_numbers)

print("Part1 lowest location number is: ", min(location_numbers))
