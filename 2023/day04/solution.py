import re


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

################ Part1 ################

worth_point_sum = 0
for line in lines:
    [card_id, all_numbers] = line.split(": ")

    [winning_numbers, having_numbers] = all_numbers.split("|")

    winning_numbers = re.findall(r"\d+", winning_numbers)
    having_numbers = re.findall(r"\d+", having_numbers)

    matching_numbers = set(winning_numbers).intersection(set(having_numbers))

    if len(matching_numbers) >= 2:
        worth_points = 2 ** (len(matching_numbers) - 1)
    elif len(matching_numbers) == 1:
        worth_points = 1
    else:
        worth_points = 0

    worth_point_sum += worth_points

print("Part 1 Sum of Worth Points is: ", worth_point_sum)

################ Part2 ################

# {
#     'card_num': 1,
#     'matching_numbers': 4,
#     "wining_copy": [2,3,4,5]
# }


def summarise_card_info():
    cards_info = []
    for line in lines:
        [card_id, all_numbers] = line.split(": ")
        [winning_numbers, having_numbers] = all_numbers.split("|")

        winning_numbers = re.findall(r"\d+", winning_numbers)
        having_numbers = re.findall(r"\d+", having_numbers)

        matching_numbers = set(winning_numbers).intersection(set(having_numbers))

        id = re.findall(r"\d+", card_id)

        card_num = int(id[0])

        card_info = {"card_num": 0, "matching_numbers": 0, "wining_copy": []}

        card_info["card_num"] = card_num
        card_info["matching_numbers"] = len(matching_numbers)
        card_info["wining_copy"] = [
            card_num
            for card_num in range(card_num + 1, card_num + 1 + len(matching_numbers))
        ]

        cards_info.append(card_info)

    return cards_info


cards = summarise_card_info()

for card in cards:
    for copy in card["wining_copy"]:
        cards.append(cards[copy - 1])

print("Part 2 Total Number of Scratchcards is : ", len(cards))
