import re

def extract_numbers_from_text(text):
    numbers = re.findall(r'\b\d+\b', text)
    return numbers

def sum_of_numbers_in_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        numbers = extract_numbers_from_text(text)
        sum = 0
        for number in numbers:
            sum += int(number)
        return sum
    
filename = 'problem.txt'
print("Sum of numbers in file '{}': {}".format(filename, sum_of_numbers_in_file(filename)))
