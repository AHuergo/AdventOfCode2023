import re


def process_line(line):
    pattern = re.compile(r'(\d+|\b\w+\b)')
    matches = pattern.findall(line)
    result_array = [int(match) if match.isdigit() else match for match in matches]
    return result_array[1:]


blueMax = 14
redMax = 12
greenMax = 13

with open('input', 'r') as input_file:
    total = 0
    lines = input_file.readlines()

    for line in lines:
        colors = {"red": 0, "green": 0, "blue": 0}
        game = -1
        data = process_line(line)

        for value in data:
            if game == -1:
                game = value
            elif game != 0:
                if isinstance(value, int):
                    cubes = value
                else:
                    colors[value] = cubes
                    if colors['red'] > redMax or colors['green'] > greenMax or colors['blue'] > blueMax:
                        game = 0
        total += game

print("Total: ", total)
input_file.close()
