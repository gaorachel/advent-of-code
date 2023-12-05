import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file("dummy2.txt")

part_number_sum = 0
for j in range(len(lines)):
    prev_line = lines[j - 1] if j > 0 else ""
    next_line = lines[j + 1] if j < len(lines) - 1 else ""

    three_lines = prev_line + lines[j] + next_line

    digits = re.findall(r"\d+", lines[j])
    print("digits", digits)

    for digit in digits:
        i = lines[j].index(digit)

        pre_digit_index = i - 1 if i > 0 else 0
        post_digit_index = (
            i + len(digit) + 1 if i < len(lines[j]) - 1 else len(lines[j]) - 1
        )

        eligible_area = (
            [prev_line[pre_digit_index:post_digit_index]]
            + [lines[j][pre_digit_index:post_digit_index]]
            + [next_line[pre_digit_index:post_digit_index]]
        )

        # print("eligible_area", eligible_area, "-----------------")

        symbols = re.findall(r"[^\d.\n]", "".join(eligible_area))

        print(symbols, eligible_area)

        if len(symbols) > 0:
            part_number_sum += int(digit)

print("Part 1 Sum of Part Numbers is: ", part_number_sum)
