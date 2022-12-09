import numpy
import matplotlib.pyplot

file = open('day9-input.txt', 'r')
lines = file.readlines()


def get_head_move_distance(direction: str):
    distance = [0, 0]
    if direction == 'L':
        distance = [-1, 0]
    elif direction == 'R':
        distance = [1, 0]
    elif direction == 'D':
        distance = [0, -1]
    elif direction == 'U':
        distance = [0, 1]

    return distance


tail_visited = {(0, 0)}
head_pos = numpy.array([0, 0])
tail_pos = numpy.array([0, 0])
for line in lines:
    direction, steps = line.strip().split()
    head_move_distance = get_head_move_distance(direction)
    for step in range(int(steps)):
        head_pos += head_move_distance
        diff = head_pos - tail_pos
        if numpy.linalg.norm(diff) > 1.5:
            tail_pos += numpy.sign(diff)
            tail_visited.add(tuple(tail_pos))

print(head_pos)
print(tail_pos)
print(len(tail_visited))

# Part 2
tail_visited = {(0, 0)}
knots_pos = list()
knot_count = 10
for _ in range(knot_count):
    knots_pos.append(numpy.array([0, 0]))

head_pos = knots_pos[0]
tail_pos = knots_pos[-1]
for line in lines:
    direction, steps = line.strip().split()
    head_move_distance = get_head_move_distance(direction)
    for step in range(int(steps)):
        head_pos += head_move_distance
        for knot_index in range(1, knot_count):
            diff = knots_pos[knot_index - 1] - knots_pos[knot_index]
            if numpy.linalg.norm(diff) > 1.5:
                knots_pos[knot_index] += numpy.sign(diff)
        tail_visited.add(tuple(tail_pos))

print(head_pos)
print(tail_pos)
print(len(tail_visited))

tail_matrix = numpy.zeros((300, 450))
for tail_visited_pos in tail_visited:
    tail_matrix[tail_visited_pos[0] + 250, tail_visited_pos[1] + 100] = 1

matplotlib.pyplot.matshow(tail_matrix)
matplotlib.pyplot.show()
