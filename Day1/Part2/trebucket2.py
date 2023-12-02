def wordsToNumber(word1, word2, digits):
    res = 0
    if word1.isdigit():
        res = 10 * int(word1)
    else:
        word1 = word1.lower()
        for index, digit in enumerate(digits):
            if digit == word1:
                res += (index + 1) * 10

    if word2.isdigit():
        res += int(word2)
    else:
        word2 = word2.lower()
        for index, digit in enumerate(digits):
            if digit == word2:
                res += (index + 1)

    return res

def line_process(line, digits):
    digit1 = "-1"
    digit2 = "-1"

    for i in range(len(line)):
        c = line[i]
        if c.isdigit() and digit1 == "-1":
            digit1 = c
        elif c.isdigit() and digit1 != "-1":
            digit2 = c
        for j in range(i+1, len(line)+1):
           current = line[i:j].strip().lower()
           if current in digits and digit1 == "-1":
               digit1 = current
           if current in digits and digit1 != "-1":
               digit2 = current

    if digit2 == "-1":
        digit2 = digit1

    return wordsToNumber(digit1, digit2, digits)


digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

with open('input', 'r') as input_file:
    total = 0
    lines = input_file.readlines()
    for line in lines:
        partial = line_process(line, digits)
        total += partial

print("Total: ", total)
input_file.close()
