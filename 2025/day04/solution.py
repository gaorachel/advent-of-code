def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

grid = [list(line.strip()) for line in lines]

directions = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]
rows, cols = len(grid), len(grid[0])


################ Part1 ################
x_count = 0
removed_paper_rolls = 0
round = 0
for i in range(rows):
    for j in range(cols):

        if grid[i][j] != "@":
            continue

        accessible_count = 0
        for dx, dy in directions:
            ni, nj = i + dx, j + dy

            if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "@":
                accessible_count += 1

        if accessible_count < 4:
            x_count += 1

print("First answer is ", x_count)


################ Part2 ################
total_removed_count = 0
while True:

    to_remove = []
    for i in range(rows):
        for j in range(cols):

            if grid[i][j] != "@":
                continue

            accessible_count = 0
            for dx, dy in directions:
                ni, nj = i + dx, j + dy

                if 0 <= ni < rows and 0 <= nj < cols and grid[ni][nj] == "@":
                    accessible_count += 1

            if accessible_count < 4:
                to_remove.append((i, j))

    if not to_remove:
        break

    for ri, rj in to_remove:
        total_removed_count += 1
        grid[ri][rj] = "."

print("Second answer is ", total_removed_count)
