file = open('day11-input.txt', 'r')
lines = file.readlines()


class Monkey:
    def __init__(self, start_items: list, operation: list, modulus: int, monkey_true: int, monkey_false: int):
        self.items = start_items
        self.operation = operation
        self.modulus = modulus
        self.monkey_true = monkey_true
        self.monkey_false = monkey_false
        self.inspected_count = 0

    def calc_worry_level(self, item):
        if self.operation[1] == 'old':
            value = item
        else:
            value = int(self.operation[1])

        result = 0
        if self.operation[0] == '*':
            result = item * value
        elif self.operation[0] == '+':
            result = item + value
        else:
            print("error")
            exit(1)

        self.inspected_count += 1
        return result // BORED_FACTOR

    def get_next_monkey(self, item):
        if item % self.modulus == 0:
            return self.monkey_true
        else:
            return self.monkey_false


def parse_monkeys(monkeys):
    current_monkey = -1
    current_start_items = []
    current_operation = []
    current_modulus = 0
    current_monkey_true = 0
    current_monkey_false = 0
    for line in lines:
        line = line.strip()
        if line.startswith("Monkey"):
            if current_monkey != -1:
                monkeys.append(Monkey(current_start_items, current_operation, current_modulus, current_monkey_true,
                                      current_monkey_false))
            current_monkey = int(line.split()[1][0:-1])
        elif line.startswith("Starting items:"):
            line = line.replace(',', '')
            items_text = line.split()[2:]
            current_start_items = list(int(item) for item in items_text)
        elif line.startswith("Operation:"):
            current_operation = line[line.find('= ') + 2:].split()[1:]
        elif line.startswith("Test:"):
            current_modulus = int(line.split()[-1])
        elif line.startswith("If true:"):
            current_monkey_true = int(line.split()[-1])
        elif line.startswith("If false:"):
            current_monkey_false = int(line.split()[-1])
    monkeys.append(
        Monkey(current_start_items, current_operation, current_modulus, current_monkey_true, current_monkey_false))


def run_game(inspected_counts, num_rounds, worry_level_modulus):
    for _ in range(num_rounds):
        for monkey in monkeys:
            item_count = len(monkey.items)
            for _ in range(item_count):
                inspected_item = monkey.items.pop(0)
                inspected_item = monkey.calc_worry_level(inspected_item) % worry_level_modulus
                next_monkey = monkey.get_next_monkey(inspected_item)
                monkeys[next_monkey].items.append(inspected_item)

    for monkey in monkeys:
        inspected_counts.append(monkey.inspected_count)

    inspected_counts.sort()


def calc_worry_level_modulus():
    worry_level_modulus = 1
    for monkey in monkeys:
        worry_level_modulus *= monkey.modulus
    return worry_level_modulus


BORED_FACTOR = 3
monkeys = []
parse_monkeys(monkeys)
inspected_counts = []
run_game(inspected_counts, 20, calc_worry_level_modulus())
monkey_business = inspected_counts[-1] * inspected_counts[-2]
print(monkey_business)

# Part 2
BORED_FACTOR = 1
monkeys = []
parse_monkeys(monkeys)

inspected_counts = []
run_game(inspected_counts, 10000, calc_worry_level_modulus())
monkey_business = inspected_counts[-1] * inspected_counts[-2]
print(monkey_business)
