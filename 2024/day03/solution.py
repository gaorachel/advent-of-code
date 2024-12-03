import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


def find_valid_sections(text):
    return re.findall(r"mul\((\d+),\s*(\d+)\)", text)


def sum_sections(sections):
    return sum(int(x) * int(y) for x, y in sections)


def find_index(text, substring):
    indices = []
    start = 0
    skip_step = len(substring)

    while start < len(text):
        start = text.find(substring, start)

        if start == -1:
            break

        indices.append(start)
        start += skip_step

    return indices


lines = read_text_file()

text = "".join([line for line in lines])

################ Part1 ################

valid_sections = find_valid_sections(text)

total = sum_sections(valid_sections)

print("First part answer is ", total)

################ Part2 ################

dont_indices = find_index(text, "don't()")
do_indices = find_index(text, "do()")

combined_indices = []
i, j = 0, 0
while i < len(dont_indices) and j < len(do_indices):
    if dont_indices[i] < do_indices[j]:
        combined_indices.append((0, dont_indices[i]))
        i += 1
    else:
        combined_indices.append((1, do_indices[j]))
        j += 1

combined_indices.extend(
    [(0, dont_indices[rest]) for rest in range(i, len(dont_indices))]
)
combined_indices.extend([(1, do_indices[rest]) for rest in range(j, len(do_indices))])


valid_sections2 = []
is_do = True
start = 0
end = 0
k = 0
while k < len(combined_indices):
    if is_do and combined_indices[k][0] == 0:
        end = combined_indices[k][1]
        valid_sections2 += find_valid_sections(text[start:end])
        is_do = False
    elif not is_do and combined_indices[k][0] == 1:
        is_do = True
        start = combined_indices[k][1]

    k += 1

if combined_indices[-1][0] == 1:
    valid_sections2 += find_valid_sections(text[combined_indices[-1][1] :])

total2 = sum_sections(valid_sections2)

print("Second part answer is ", total2)
