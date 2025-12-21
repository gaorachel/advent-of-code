def read_text_file(file_path="dummy.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

splitted_lines = [line.split() for line in lines]

################ Part1 ################
