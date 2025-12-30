def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()
lines = [line.strip() for line in lines]

total1 = 0
total2 = 0
for line in lines:
    ################ Part1 ################
    first_value1 = max(line[:-1])
    first_index1 = line.index(first_value1)

    second_value = max(line[first_index1 + 1 :])

    total1 += int(first_value1 + second_value)

    ################ Part2 ################
    start_index = 0
    digits = ""
    for i in range(11, 0, -1):
        sub_line = line[start_index:-i]
        digit = max(sub_line)

        start_index += sub_line.index(digit) + 1
        digits += digit

    last_digit = max(line[start_index:])

    total2 += int(digits + last_digit)


print("First part answer:", total1)
print("Second part answer:", total2)
