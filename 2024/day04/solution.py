def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

splitted_lines = [line.split() for line in lines]

grid = [[letter for letter in word] for line in splitted_lines for word in line]

################ Part1 ################

word = "XMAS"
directions = [
    (0, 1),
    (0, -1),
    (1, 0),
    (-1, 0),
    (1, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
]

rows = len(grid)
cols = len(grid[0])

appearing_times = 0
for i in range(rows):
    for j in range(cols):

        for x, y in directions:
            is_match = True

            for k in range(len(word)):
                moving_direction_row = i + k * x
                moving_direction_col = j + k * y

                if (
                    not (
                        0 <= moving_direction_row < rows
                        and 0 <= moving_direction_col < cols
                    )
                    or grid[moving_direction_row][moving_direction_col] != word[k]
                ):
                    is_match = False
                    break

            if is_match:
                appearing_times += 1

print("First part answer: ", appearing_times)


################ Part2 ################

appearing_times2 = 0
for i in range(1, rows - 1):
    for j in range(1, cols - 1):

        if grid[i][j] == "A":
            backward_letter1 = grid[i + 1][j - 1]
            backward_letter2 = grid[i - 1][j + 1]
            forward_letter1 = grid[i + 1][j + 1]
            forward_letter2 = grid[i - 1][j - 1]

            if (
                sorted(
                    [
                        backward_letter1,
                        backward_letter2,
                        forward_letter1,
                        forward_letter2,
                    ]
                )
                == ["M", "M", "S", "S"]
                and backward_letter1 != backward_letter2
            ):
                appearing_times2 += 1

print("Second part answer: ", appearing_times2)
