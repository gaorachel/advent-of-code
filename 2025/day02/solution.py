def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


raw_products = read_text_file()

splitted_products = [product.split(",") for product in raw_products]
products = [
    product for sublist in splitted_products for product in sublist if product != "\n"
]

################ Part1 ################
invalid_id_sum = 0
for product in products:
    [first, last] = product.split("-")
    for i in range(int(first), int(last) + 1):
        str_i = str(i)
        half = len(str_i) // 2
        if str_i[:half] == str_i[half:]:
            invalid_id_sum += i

print("First part answer:", invalid_id_sum)
