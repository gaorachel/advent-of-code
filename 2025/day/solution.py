def read_text_file(file_path="dummy.txt"):
    with open(file_path, "r") as f:
        return f.read().splitlines()


lines = read_text_file()

################ Part1 ################
