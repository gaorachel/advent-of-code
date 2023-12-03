import re

def read_text_file(file_path='input.txt'):
    text_file = open(file_path, 'r')
    lines = text_file.readlines()

    return lines


examples = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f','treb7uchet']

def sum_first_last_digit(arr):
    total = 0
    for i in arr:
        all_int = re.findall(r'\d+', i)
        answer = f'{all_int[0][0]}{all_int[-1][-1]}'

        total += int(answer)

    return total

print(sum_first_last_digit(read_text_file()))



    

