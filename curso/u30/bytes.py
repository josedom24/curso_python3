line = '-' * 28
print(line)
print("|    №   | char  |   byte ")
print(line)
for number in range(256):
    char = chr(number)
    print('| {0:>6} | {1:^7} | {2:x}'.format(number,char,number))
