def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

splitted_lines = [line.split() for line in lines]

################ Part1 ################

sorted_left_list = sorted([int(line[0]) for line in splitted_lines])
sorted_right_list = sorted([int(line[1]) for line in splitted_lines])

total_distance = 0
for i in range(len(sorted_left_list)):
    total_distance += abs(sorted_left_list[i] - sorted_right_list[i])

    i += 1

print("First part answer: ", total_distance)

################ Part2 ################

similarity_score = 0
for l in sorted_left_list:
    common_number_list = set([l]) & set(sorted_right_list)

    if common_number_list:
        for r in sorted_right_list:
            appearing_times = 0
            if r == l:
                appearing_times += 1

            similarity_score += l * appearing_times

print("Second part answer: ", similarity_score)
