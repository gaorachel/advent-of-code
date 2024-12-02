def read_text_file(file_path="dummy.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

reports = [line.split() for line in lines]

################ Part1 ################

safe_report_count = 0
for report in reports:
    level_diff_list = [
        int(report[i + 1]) - int(report[i]) for i in range(len(report) - 1)
    ]

    safe_diff_list = [1, 2, 3, -1, -2, -3]
    unsafe_diff_list = set(level_diff_list) - set(safe_diff_list)

    if not unsafe_diff_list:
        if (max(level_diff_list) > 0 and min(level_diff_list) > 0) or (
            max(level_diff_list) < 0 and min(level_diff_list) < 0
        ):  # the diff values should be either all positive or all negative, so if not, that means a report have both increased level and decreased level.
            safe_report_count += 1

print("First part answer: ", safe_report_count)
