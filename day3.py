file = open('day3-input.txt', 'r')
lines = file.readlines()


def priority(char: str) -> int:
    ordinality = ord(char)
    if ordinality >= ord('a'):
        offset = ord('a') - 1
    else:
        offset = ord('A') - 1 - 26
    ordinality -= offset
    return ordinality


priority_sum = 0
for line in lines:
    length = len(line)
    sack1 = list(line[0:int(length / 2)])
    sack2 = list(line[int(length / 2):])
    intersect = set(sack1).intersection(sack2)
    priority_sum += priority(*intersect)

print(priority_sum)

# Part 2
priority_sum = 0
for group in range(len(lines) // 3):
    elf1 = lines[3 * group].strip()
    elf2 = lines[3 * group + 1].strip()
    elf3 = lines[3 * group + 2].strip()
    intersect = set(list(elf1)).intersection(elf2)
    intersect = intersect.intersection(elf3)
    priority_sum += priority(*intersect)

print(priority_sum)
