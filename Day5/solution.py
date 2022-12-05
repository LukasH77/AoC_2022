
data = open("aoc_day5_input.txt", "r")

one = ['D', 'L', 'J', 'R', 'V', 'G', 'F']
two = ['T', 'P', 'M', 'B', 'V', 'H', 'J', 'S']
three = ['V', 'H', 'M', 'F', 'D', 'G', 'P', 'C']
four = ['M', 'D', 'P', 'N', 'G', 'Q']
five = ['J', 'L', 'H', 'N', 'F']
six = ['N', 'F', 'V', 'Q', 'D', 'G', 'T', 'Z']
seven = ['F', 'D', 'B', 'L']
eight = ['M', 'J', 'B', 'S', 'V', 'D', 'N']
nine = ['G', 'L', 'D']
stacks = [one, two, three, four, five, six, seven, eight, nine]
for i in range(11):
    line = data.readline()
while line:
    words = line.split(' ')
    words[5] = words[5].replace('\n', '')
    words = [int(words[1]), int(words[3]), int(words[5])]
    tmp = []
    for i in range(words[0]):
        crate = stacks[words[1] - 1].pop()
        tmp.append(crate)
    tmp.reverse()
    stacks[words[2] - 1].extend(tmp)
    line = data.readline()

for i in range(9):
    print(stacks[i][len(stacks[i]) - 1])
