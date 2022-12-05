file = open('day1-input.txt', 'r')
lines = file.readlines()

elves = [0]
elf_index = 0
calories = 0

for line in lines:
    if line == "\n":
        elf_index += 1
        elves.append(0)
        calories = 0
    else:
        elves[elf_index] += int(line)

elves.sort(reverse=True)
print(elves[0])

print(elves[0] + elves[1] + elves[2])
