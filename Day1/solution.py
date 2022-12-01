data = open("aoc_day1_input.txt", "r")

calories = []
max = 0
sum = 0
line = data.readline()
while line:
    sum += int(line)
    line = data.readline()
    if line == '\n':
        calories.append(sum)
        if sum > max:
            max = sum
        sum = 0
        line = data.readline()

sum = max
calories.sort(reverse=True)
sum += calories[1]
sum += calories[2]
print(sum)
