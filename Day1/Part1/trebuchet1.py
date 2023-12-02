def line_process(line):
    digit1 = -1
    digit2 = -1
    for index in range(len(line)):
        c = line[index]
        if c.isdigit() and digit1 == -1:
            digit1 = int(c)
        elif c.isdigit():
            digit2 = int(c)

    if digit2 == -1:
        digit2 = digit1

    res = digit1 * 10 + digit2
    return res


with open('input', 'r') as input_file:
    total = 0
    lines = input_file.readlines()
    for line in lines:
        total += line_process(line)
print("Total: ", total)
input_file.close()