def replace_text_to_digit(text):
    text_numbers_to_digits = {
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

    new_text = ''  # Initialize new_text with the original text

    for key, value in text_numbers_to_digits.items():
        new_text = new_text.replace(key, value)  # Perform replacements and update new_text

    return new_text

print(replace_text_to_digit('two1nine'))