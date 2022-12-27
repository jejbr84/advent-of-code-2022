import copy

file = open('day21-input.txt', 'r')
lines = file.readlines()

yelled_monkeys = dict()
waiting_monkeys = dict()
for line in lines:
    line_split = line.strip().split()
    if len(line_split) == 2:
        yelled_monkeys[line_split[0][0:-1]] = int(line_split[1])
    else:
        waiting_monkeys[line_split[0][0:-1]] = (line_split[1], line_split[2], line_split[3])

is_root_waiting = True
while is_root_waiting:
    for name in waiting_monkeys:
        operation = waiting_monkeys[name]
        if operation[0] in yelled_monkeys.keys() and operation[2] in yelled_monkeys.keys():
            if operation[1] == '+':
                yelled_monkeys[name] = yelled_monkeys[operation[0]] + yelled_monkeys[operation[2]]
            elif operation[1] == '-':
                yelled_monkeys[name] = yelled_monkeys[operation[0]] - yelled_monkeys[operation[2]]
            elif operation[1] == '*':
                yelled_monkeys[name] = yelled_monkeys[operation[0]] * yelled_monkeys[operation[2]]
            elif operation[1] == '/':
                yelled_monkeys[name] = yelled_monkeys[operation[0]] / yelled_monkeys[operation[2]]
            break

    waiting_monkeys.pop(name)
    if name == 'root':
        is_root_waiting = False

print(f"root number: {yelled_monkeys['root']}")

# Part 2

yelled_monkeys_start = dict()
waiting_monkeys_start = dict()
for line in lines:
    line_split = line.strip().split()
    if len(line_split) == 2:
        yelled_monkeys_start[line_split[0][0:-1]] = int(line_split[1])
    else:
        waiting_monkeys_start[line_split[0][0:-1]] = (line_split[1], line_split[2], line_split[3])

waiting_monkeys_start['root'] = (waiting_monkeys_start['root'][0], '=', waiting_monkeys_start['root'][2])

root_equals = False
root_difference = 0
human_number = 1
human_boundaries = [1, 10000000000000]
while not root_equals:
    yelled_monkeys = copy.deepcopy(yelled_monkeys_start)
    waiting_monkeys = copy.deepcopy(waiting_monkeys_start)

    # Binary search
    human_number = sum(human_boundaries) // 2
    yelled_monkeys['humn'] = human_number

    is_root_waiting = True
    while is_root_waiting:
        for name in waiting_monkeys:
            operation = waiting_monkeys[name]
            if operation[0] in yelled_monkeys.keys() and operation[2] in yelled_monkeys.keys():
                if operation[1] == '+':
                    yelled_monkeys[name] = yelled_monkeys[operation[0]] + yelled_monkeys[operation[2]]
                elif operation[1] == '-':
                    yelled_monkeys[name] = yelled_monkeys[operation[0]] - yelled_monkeys[operation[2]]
                elif operation[1] == '*':
                    yelled_monkeys[name] = yelled_monkeys[operation[0]] * yelled_monkeys[operation[2]]
                elif operation[1] == '/':
                    yelled_monkeys[name] = yelled_monkeys[operation[0]] / yelled_monkeys[operation[2]]
                elif operation[1] == '=':
                    root_difference = yelled_monkeys[operation[0]] - yelled_monkeys[operation[2]]
                    if root_difference == 0:
                        root_equals = True
                break

        waiting_monkeys.pop(name)
        if name == 'root':
            is_root_waiting = False

    if root_difference > 0:
        human_boundaries[0] = human_number
    else:
        human_boundaries[1] = human_number

    print(f"human: {human_number}, root difference: {root_difference}")
