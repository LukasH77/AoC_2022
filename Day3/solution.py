import string

data = open("aoc_day3_input.txt", "r")

line1 = data.readline()
line2 = data.readline()
line3 = data.readline()
sum = 0
while line1:
    found = False
    for letter in line1:
        if found:
            continue
        if letter in line2 and letter in line3:
            if letter.isupper():
                add = string.ascii_lowercase.index(letter.lower()) + 27
                sum += add
                # print(f"{line}found: {line[i]}\nadd {add}\n")
            else:
                add = string.ascii_lowercase.index(letter) + 1
                sum += add
                # print(f"{line}found: {line[i]}\nadd {add}\n")
            found = True
    line1 = data.readline()
    line2 = data.readline()
    line3 = data.readline()

print(sum)
