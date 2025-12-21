def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

splitted_lines = [line.split() for line in lines]

################ Part1 & 2 ################
size = 100
start = 50
pointing_zero_times1 = 0
pointing_zero_times2 = 0

for line in splitted_lines:
    direction = line[0][0]
    distance = int(line[0][1:])

    if direction == "R":
        next = start + distance
        pointing_zero_times2 += (next // size) - (start // size)
    if direction == "L":
        next = start - distance
        pointing_zero_times2 += ((start - 1) // size) - ((next - 1) // size)

    end = next % size

    if end == 0:
        pointing_zero_times1 += 1

    start = end

print("First part answer:", pointing_zero_times1)
print("Second part answer:", pointing_zero_times2)
