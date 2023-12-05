import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

part_number_sum = 0
for j in range(len(lines)):
    prev_line = lines[j - 1] if j > 0 else ""
    next_line = lines[j + 1] if j < len(lines) - 1 else ""

    three_lines = prev_line + lines[j] + next_line

    digits = re.finditer(r"\d+", lines[j])

    for digit in digits:
        pre_digit_index = digit.start() - 1 if digit.start() > 0 else 0
        post_digit_index = (
            digit.end() + 1 if digit.end() < len(lines[j]) - 1 else digit.end()
        )

        eligible_area = (
            [prev_line[pre_digit_index:post_digit_index]]
            + [lines[j][pre_digit_index:post_digit_index]]
            + [next_line[pre_digit_index:post_digit_index]]
        )

        symbols = re.findall(r"[^\d.\n]", "".join(eligible_area))

        if len(symbols) > 0:
            part_number_sum += int(digit.group())

print("Part 1 Sum of Part Numbers is: ", part_number_sum)
