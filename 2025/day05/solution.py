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
