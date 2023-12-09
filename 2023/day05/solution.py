import re


def read_text_file(file_path="input.txt"):
    with open(file_path, "r") as text_file:
        return text_file.read()


text = read_text_file()

almanac = [section.strip().split("\n") for section in text.strip().split("\n\n")]

seeds = map(int, re.findall(r"\d+", almanac[0][0]))


def get_ranges(map_section):
    ranges = []
    for line in map_section[1:]:
        destination, source, range_len = map(int, re.findall(r"\d+", line))

        ranges.append((destination, source, source + range_len))

    return ranges


maps = [get_ranges(section) for section in almanac[1:]]


def map_numbers(seed_number):
    destination_number = None
    source_number = seed_number if destination_number is None else destination_number

    for map in maps:
        for destination_start, source_start, source_end in map:
            if source_start <= source_number < source_end:
                destination_number = destination_start + (source_number - source_start)
                break
        else:
            destination_number = source_number

        source_number = destination_number

    return destination_number


location_numbers = [map_numbers(seed) for seed in seeds]

print("Part 1 lowest location number is:", min(location_numbers))
