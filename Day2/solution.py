
data = open("aoc_day2_input.txt", "r")

sum = 0
line = data.readline()
while line:
    if line[0] == 'A':
        if line[2] == 'X':
            sum += 3
        elif line[2] == 'Y':
            sum += 4
        elif line[2] == 'Z':
            sum += 8
    elif line[0] == 'B':
        if line[2] == 'X':
            sum += 1
        elif line[2] == 'Y':
            sum += 5
        elif line[2] == 'Z':
            sum += 9
    elif line[0] == 'C':
        if line[2] == 'X':
            sum += 2
        elif line[2] == 'Y':
            sum += 6
        elif line[2] == 'Z':
            sum += 7
    line = data.readline()

print(sum)
