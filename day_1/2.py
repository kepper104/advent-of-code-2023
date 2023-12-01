total_sum = 0
with open("input_1", "r") as f:
    lines = list(map(str.strip, f.readlines()))
# print(lines)
digits = ("one", "two", "three", "four", "five", "six", "seven", "eight", "nine")
for line in lines:
    first = ''
    cur_word = ''
    for symbol in line:
        if symbol.isdigit():
            first = symbol
            break
        cur_word += symbol
        digits_in_current_string = list(map(lambda x: x in cur_word, digits))
        # print(digits_in_current_string, cur_word)
        if any(digits_in_current_string):
            first = str(digits_in_current_string.index(True) + 1)
            break
    # print(first)

    last = ''
    cur_word = ''
    for symbol in line[::-1]:
        if symbol.isdigit():
            last = symbol
            break

        cur_word += symbol
        cur_word = "".join(list(list(cur_word).__reversed__()))
        digits_in_current_string = list(map(lambda x: x in cur_word, digits))
        # print(digits_in_current_string, cur_word)
        if any(digits_in_current_string):
            last = str(digits_in_current_string.index(True) + 1)
            break
        cur_word = "".join(list(list(cur_word).__reversed__()))

    total_sum += int(first + last)
    print(line, first + last)

print(total_sum)
