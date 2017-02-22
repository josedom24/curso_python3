import itertools

line = '-' * 49
print(line)
print("|    №   | isdigit | isdecimal |  isnumeric | chr")
print(line)
for number in itertools.chain(range(1000), range(4969, 4978), range(8304, 11000)):
    char = chr(number)
    if (char.isdigit() or char.isdecimal() or char.isnumeric()):
        print('| {0:>6} | {1:^7} | {2:^9} | {3:^10} | {4:3} '.format(
            number,
            '+' if char.isdigit() else '-',
            '+' if char.isdecimal() else '-',
            '+' if char.isnumeric() else '-',
            char
        )
    )