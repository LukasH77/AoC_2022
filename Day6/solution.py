
data = open("aoc_day5_input.txt", "r")

line = data.readline()
letters = list(line[0:14])
count = 14
while count < len(line):
    nondups = 0
    for letter in letters:
        if not letters.count(letter) > 1:
            nondups += 1
    if nondups == 14:
        print(count)
    count += 1
    letters.remove(letters[0])
    letters.append(line[count - 1])
