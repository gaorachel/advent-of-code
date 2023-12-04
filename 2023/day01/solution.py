import re

def read_text_file(file_path='input.txt'):
    text_file = open(file_path, 'r')
    lines = text_file.readlines()

    return lines

##############################################################################

lines = read_text_file()
##############################################################################
################ Part1 ################ 

total1 = 0
for line in lines:
    all_int = re.findall(r'\d+', line)

    calibration_value = all_int[0][0] + all_int[-1][-1]

    total1 += int(calibration_value)

print('Part 1 answer: ', total1)

################ Part2 ################ 

def replace_text_to_digit(line):
    numbers_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

    number_word = '|'.join(numbers_dict.keys())
    all_numbers = re.findall(rf'(?=(\d|{number_word}))', line)

    first_number = all_numbers[0]
    last_number = all_numbers[-1]

    if not first_number.isdigit():
        first_number_digit = numbers_dict[first_number]
        all_numbers[0] = first_number_digit
    
    if not last_number.isdigit():
        last_number_digit = numbers_dict[last_number]
        all_numbers[-1] = last_number_digit

    return all_numbers

total2 = 0
for line in lines: 
    all_numbers = replace_text_to_digit(line)

    calibration_value = all_numbers[0] + all_numbers[-1]

    total2 += int(calibration_value)

print('Part 2 answer: ', total2)



    

