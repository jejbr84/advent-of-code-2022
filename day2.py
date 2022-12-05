file = open('day2-input.txt', 'r')
lines = file.readlines()

score = 0

for line in lines:
    data = line.split()
    if data[1] == 'X':
        score += 1
        if data[0] == 'A':
            score += 3
        elif data[0] == 'C':
            score += 6
    elif data[1] == 'Y':
        score += 2
        if data[0] == 'A':
            score += 6
        elif data[0] == 'B':
            score += 3
    elif data[1] == 'Z':
        score += 3
        if data[0] == 'B':
            score += 6
        elif data[0] == 'C':
            score += 3

print(score)

score = 0
for line in lines:
    data = line.split()
    if data[1] == 'X':
        if data[0] == 'A':
            score += 3
        elif data[0] == 'B':
            score += 1
        elif data[0] == 'C':
            score += 2
    elif data[1] == 'Y':
        score += 3
        if data[0] == 'A':
            score += 1
        elif data[0] == 'B':
            score += 2
        elif data[0] == 'C':
            score += 3
    elif data[1] == 'Z':
        score += 6
        if data[0] == 'A':
            score += 2
        elif data[0] == 'B':
            score += 3
        elif data[0] == 'C':
            score += 1

print(score)
