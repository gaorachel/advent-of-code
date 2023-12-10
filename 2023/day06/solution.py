import re
import math


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

################ Part1 ################

times = list(map(int, re.findall(r"\d+", lines[0])))
distance_records = list(map(int, re.findall(r"\d+", lines[1])))


def get_valid_ways(time, distance_record):
    ways = 0
    for charging_time in range(1, time):
        speed = charging_time
        traveling_time = time - charging_time

        travel_distance = speed * traveling_time

        # x * (time - x) => x*time - x^2

        if travel_distance > distance_record:
            ways += 1

    return ways


total_ways = 1
for i in range(len(times)):
    ways = get_valid_ways(times[i], distance_records[i])

    total_ways *= ways

print("Part1 multiply value is: ", total_ways)

################ Part1 ################

actual_time = int("".join(re.findall(r"\d+", lines[0])))
actual_distance_record = int("".join(re.findall(r"\d+", lines[1])))

print("actual_time: ", actual_time, "actual_distance_record: ", actual_distance_record)

# use the quadratic inequality
# inequality = x * (actual_time - x) > actual_distance_record
# -x^2 + actual_time * x - actual_distance_record > 0

x1 = math.ceil(
    (actual_time - math.sqrt(actual_time**2 - 4 * actual_distance_record)) / 2
)
x2 = math.floor(
    (actual_time + math.sqrt(actual_time**2 - 4 * actual_distance_record)) / 2
)

actual_total_ways = x2 - x1 + 1


print("Part2 actual total ways are:", actual_total_ways)
