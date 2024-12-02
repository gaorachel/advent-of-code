def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

reports = [line.split() for line in lines]


def is_safe(report):
    level_diff_list = [
        int(report[i + 1]) - int(report[i]) for i in range(len(report) - 1)
    ]

    if all(1 <= abs(diff) <= 3 for diff in level_diff_list) and (
        all(diff > 0 for diff in level_diff_list)
        or all(diff < 0 for diff in level_diff_list)
    ):

        return True


safe_report_count = 0
tolerated_report_count = 0
for report in reports:
    ################ Part1 ################
    if is_safe(report):
        safe_report_count += 1

    ################ Part2 ################
    else:
        for i in range(len(report)):
            modified_report = report[:i] + report[i + 1 :]
            if is_safe(modified_report):
                tolerated_report_count += 1
                break


print("First part answer: ", safe_report_count)
print("Second part answer: ", safe_report_count + tolerated_report_count)
