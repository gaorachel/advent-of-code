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

invalid_id_sum1 = 0
invalid_id_sum2 = 0
for product in products:
    [first, last] = product.split("-")
    for i in range(int(first), int(last) + 1):
        str_i = str(i)
        len_i = len(str_i)

        ################ Part1 ################
        mid = len_i // 2
        if str_i[:mid] == str_i[mid:]:
            invalid_id_sum1 += i

        ################ Part2 ################
        for j in range(1, len_i):
            if str_i[:j] * (len_i // j) == str_i:
                invalid_id_sum2 += i
                break

print("First part answer:", invalid_id_sum1)
print("Second part answer:", invalid_id_sum2)
