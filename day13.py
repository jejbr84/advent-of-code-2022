import ast
import functools

file = open('day13-input.txt', 'r')
lines = file.readlines()


def compare(left, right) -> int:
    if type(left) == list and type(right) == list:
        has_looped = False
        for i in range(min(len(left), len(right))):
            has_looped = True
            result = compare(left[i], right[i])
            if result == -1 or result == 1:
                return result

        if has_looped:
            length = i + 1
        else:
            length = 0

        if len(left) == length and len(right) == length:
            return 0
        elif len(left) == length:
            return -1
        elif len(right) == length:
            return 1
        else:
            print("Should not get here")
            exit(1)
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    elif type(left) == int and type(right) == int:
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    else:
        print("Not supported")
        exit(1)

    print("Should not get here")
    exit(1)


pairs = list()
current_pair = list()
for line in lines:
    stripped_line = line.strip()
    if stripped_line == '':
        pairs.append(tuple(current_pair))
        current_pair = list()
    else:
        current_pair.append(ast.literal_eval(line.strip()))
else:
    pairs.append(tuple(current_pair))

right_pair_sum = 0
for pair_index in range(len(pairs)):
    pair_number = pair_index + 1
    left = pairs[pair_index][0]
    right = pairs[pair_index][1]
    result = compare(left, right)
    if result == -1:
        right_pair_sum += pair_number
    # print(f"Pair {pair_number}: {'right' if result == -1 else 'wrong'} order")

print(right_pair_sum)

# Part 2
packets = [[[2]], [[6]]]
for pair in pairs:
    packets.append(pair[0])
    packets.append(pair[1])

packets.sort(key=functools.cmp_to_key(compare))
print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
