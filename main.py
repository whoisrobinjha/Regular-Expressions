import re

patterns = re.compile(r'\d{3}.\d{3}.\d{4}')

with open('Data.txt', "r") as f:
    contents = f.read()
    matches = re.finditer(patterns, contents)
    print(matches)
    for match in matches:
        print(match)


