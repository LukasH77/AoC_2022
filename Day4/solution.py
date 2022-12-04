
data = open("aoc_day4_input.txt", "r")

line = data.readline().replace('\n', '')
sum = 0
while line:
    pairs = line.split(',')
    pairs = pairs[0].split('-') + pairs[1].split('-')
    s1 = int(pairs[0])
    e1 = int(pairs[1])
    s2 = int(pairs[2])
    e2 = int(pairs[3])
    r1 = range(s1, e1 + 1)
    r2 = range(s2, e2 + 1)
    intersect = set(r1).intersection(r2)

    if intersect:
        sum += 1
    line = data.readline().replace('\n', '')

print(sum)
