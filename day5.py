file = open('day5-input.txt', 'r')
lines = file.readlines()

crates = list()


def move_crates(line: str):
    task = line.strip().split(' ')
    move_count = int(task[1])
    source = int(task[3]) - 1
    destination = int(task[5]) - 1
    for _ in range(move_count):
        crate = crates[source].pop()
        crates[destination].append(crate)


def move_crates_at_once(line: str):
    task = line.strip().split(' ')
    move_count = int(task[1])
    source = int(task[3]) - 1
    destination = int(task[5]) - 1
    crane_crates = []
    for _ in range(move_count):
        crate = crates[source].pop()
        crane_crates.append(crate)
    for _ in range(move_count):
        crate = crane_crates.pop()
        crates[destination].append(crate)


def find_crates(line: str):
    is_finding = True
    index = -1
    while is_finding:
        index = line.find('[', index + 1)
        if index == -1:
            is_finding = False
        else:
            stack_index = index // 4
            while stack_index >= len(crates):
                crates.append(list())
            crates[stack_index].append(line[index + 1])


for line in lines:
    if line[0] == 'm':
        move_crates(line)
    elif line[0] == '\n':
        for stack in crates:
            stack.reverse()
    else:
        find_crates(line)

print(crates)
answer = ''
for stack in crates:
    answer += stack[-1]

print(answer)

# Part 2
file = open('day5-input.txt', 'r')
lines = file.readlines()

crates = list()

for line in lines:
    if line[0] == 'm':
        move_crates_at_once(line)
    elif line[0] == '\n':
        for stack in crates:
            stack.reverse()
    else:
        find_crates(line)

print(crates)
answer = ''
for stack in crates:
    answer += stack[-1]

print(answer)
