import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

times = list(map(int, re.findall(r"\d+", lines[0])))
distance_records = list(map(int, re.findall(r"\d+", lines[1])))


def get_valid_ways(time, distance_record):
    ways = 0
    for charging_time in range(1, time):
        speed = charging_time
        traveling_time = time - charging_time

        travel_distance = speed * traveling_time

        if travel_distance > distance_record:
            ways += 1

    return ways


total_ways = 1
for i in range(len(times)):
    ways = get_valid_ways(times[i], distance_records[i])

    total_ways *= ways

print("Part1 multiply value is: ", total_ways)
