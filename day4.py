file = open('day4-input.txt', 'r')
lines = file.readlines()

fully = 0
for line in lines:
    pair = line.strip().split(',')
    elf1 = [int(string) for string in pair[0].split('-')]
    elf2 = [int(string) for string in pair[1].split('-')]
    if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
        fully += 1
    elif elf2[0] >= elf1[0] and elf2[1] <= elf1[1]:
        fully += 1

print(fully)

# Part 2
not_overlapping = 0
for line in lines:
    pair = line.strip().split(',')
    elf1 = [int(string) for string in pair[0].split('-')]
    elf2 = [int(string) for string in pair[1].split('-')]
    if elf2[0] > elf1[1] or elf1[0] > elf2[1]:
        not_overlapping += 1

print(len(lines) - not_overlapping)
