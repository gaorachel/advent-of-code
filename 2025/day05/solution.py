def read_text_file(file_path="dummy.txt"):
    with open(file_path, "r") as f:
        return f.read().splitlines()


lines = read_text_file()

################ Part1 ################
blank_index = lines.index("")

range_ids = [tuple(map(int, line.split("-"))) for line in lines[:blank_index]]
ids = [int(line) for line in lines[blank_index + 1 :]]

fresh_ids = [id for id in ids if any(start <= id <= end for start, end in range_ids)]

print("First part answer:", len(fresh_ids))

################ Part1 ################
range_ids.sort(key=lambda x: x[0])

merged_ranges = []
for start, end in range_ids:
    if not merged_ranges or start > merged_ranges[-1][1]:
        merged_ranges.append([start, end])
    else:
        merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
        print(merged_ranges[-1][1])

total_unique_fresh_id_count = sum(end - start + 1 for start, end in merged_ranges)
print("Second part answer:", total_unique_fresh_id_count)
