import re
from collections import Counter


def read_text_file(file_path="input.txt"):
    text_file = open(file_path, "r")
    lines = text_file.readlines()
    text_file.close()

    return lines


lines = read_text_file()

################ Part1 ################


def score_hand_value(hand):
    label_scores = list(map("23456789TJQKA".index, hand))

    sorted_label_scores = []
    for label_score in label_scores:
        if label_score < 10:
            sorted_label_scores.append("0" + str(label_score))
        else:
            sorted_label_scores.append(str(label_score))

    return "".join(sorted_label_scores)


scored_hands = []
for line in lines:
    hand, bid = line.replace("\n", "").split(" ")

    hand_type = sorted(list(Counter(hand).values()), reverse=True)

    if hand_type == [5]:  # five of a kind
        scored_hands.append([hand, int(bid), "7" + score_hand_value(hand)])
    if hand_type == [4, 1]:  # four of a kind
        scored_hands.append([hand, int(bid), "6" + score_hand_value(hand)])
    if hand_type == [3, 2]:  # full house
        scored_hands.append([hand, int(bid), "5" + score_hand_value(hand)])
    if hand_type == [3, 1, 1]:  # three of a kind
        scored_hands.append([hand, int(bid), "4" + score_hand_value(hand)])
    if hand_type == [2, 2, 1]:  # two pair
        scored_hands.append([hand, int(bid), "3" + score_hand_value(hand)])
    if hand_type == [2, 1, 1, 1]:  # one pair
        scored_hands.append([hand, int(bid), "2" + score_hand_value(hand)])
    if hand_type == [1, 1, 1, 1, 1]:  # high card
        scored_hands.append([hand, int(bid), "1" + score_hand_value(hand)])

ranked_hands = sorted(scored_hands, key=lambda x: x[2])

total_winnings = 0
for i, hand in enumerate(ranked_hands):
    total_winnings += hand[1] * (i + 1)

print("Part1 Total Winnings are: ", total_winnings)


################ Part2 ################


def new_score_hand_value(hand):
    label_scores = list(map("J23456789TQKA".index, hand))

    sorted_label_scores = []
    for label_score in label_scores:
        if label_score < 10:
            sorted_label_scores.append("0" + str(label_score))
        else:
            sorted_label_scores.append(str(label_score))

    return "".join(sorted_label_scores)


scored_hands2 = []
for line in lines:
    hand, bid = line.replace("\n", "").split(" ")

    hand_counter = Counter(hand)
    del hand_counter["J"]
    hand_type = sorted(list(hand_counter.values()), reverse=True)

    j_count = len(re.findall("J", hand))

    if hand_type != []:
        hand_type[0] = hand_type[0] + j_count
    else:
        hand_type = [5]  ## this means the hand is like 'JJJJJ'

    if hand_type == [5]:  # five of a kind
        scored_hands2.append([hand, int(bid), "7" + new_score_hand_value(hand)])
    if hand_type == [4, 1]:  # four of a kind
        scored_hands2.append([hand, int(bid), "6" + new_score_hand_value(hand)])
    if hand_type == [3, 2]:  # full house
        scored_hands2.append([hand, int(bid), "5" + new_score_hand_value(hand)])
    if hand_type == [3, 1, 1]:  # three of a kind
        scored_hands2.append([hand, int(bid), "4" + new_score_hand_value(hand)])
    if hand_type == [2, 2, 1]:  # two pair
        scored_hands2.append([hand, int(bid), "3" + new_score_hand_value(hand)])
    if hand_type == [2, 1, 1, 1]:  # one pair
        scored_hands2.append([hand, int(bid), "2" + new_score_hand_value(hand)])
    if hand_type == [1, 1, 1, 1, 1]:  # high card
        scored_hands2.append([hand, int(bid), "1" + new_score_hand_value(hand)])

ranked_hands2 = sorted(scored_hands2, key=lambda x: x[2])

total_winnings2 = 0
for i, hand in enumerate(ranked_hands2):
    total_winnings2 += hand[1] * (i + 1)

print("Part2 Total Winnings are: ", total_winnings2)
