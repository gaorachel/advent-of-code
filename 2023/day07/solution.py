import re
from collections import Counter


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

################ Part1 ################


def is_pattern_matched(counter, pattern):
    if pattern == sorted(list(counter.values()), reverse=True):
        return True
    else:
        False


def rank_hand_value(hand):
    label_ranks = list(map("_23456789TJQKA".index, hand))

    new_label_ranks = []
    for label_rank in label_ranks:
        if label_rank < 10:
            new_label_ranks.append("0" + str(label_rank))
        else:
            new_label_ranks.append(str(label_rank))

    return "".join(new_label_ranks)


ranked_hand = []
for line in lines:
    hand, bid = line.replace("\n", "").split(" ")

    counter_hand = Counter(hand)

    hand_type = sorted(list(counter_hand.values()), reverse=True)

    five_of_a_kind = is_pattern_matched(counter_hand, [5])
    four_of_a_kind = is_pattern_matched(counter_hand, [4, 1])
    full_house = is_pattern_matched(counter_hand, [3, 2])
    three_of_a_kind = is_pattern_matched(counter_hand, [3, 1, 1])
    two_pair = is_pattern_matched(counter_hand, [2, 2, 1])
    one_pair = is_pattern_matched(counter_hand, [2, 1, 1, 1])
    high_card = is_pattern_matched(counter_hand, [1, 1, 1, 1, 1])

    if five_of_a_kind:
        ranked_hand.append([hand, int(bid), "7" + rank_hand_value(hand)])
    if four_of_a_kind:
        ranked_hand.append([hand, int(bid), "6" + rank_hand_value(hand)])
    if full_house:
        ranked_hand.append([hand, int(bid), "5" + rank_hand_value(hand)])
    if three_of_a_kind:
        ranked_hand.append([hand, int(bid), "4" + rank_hand_value(hand)])
    if two_pair:
        ranked_hand.append([hand, int(bid), "3" + rank_hand_value(hand)])
    if one_pair:
        ranked_hand.append([hand, int(bid), "2" + rank_hand_value(hand)])
    if high_card:
        ranked_hand.append([hand, int(bid), "1" + rank_hand_value(hand)])

sorted_hands = sorted(ranked_hand, key=lambda x: x[2])

total_winnings = 0
for i, hand in enumerate(sorted_hands):
    total_winnings += hand[1] * (i + 1)

print("Part1 Total Winings are: ", total_winnings)
