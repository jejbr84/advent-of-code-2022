import sys

import numpy

file = open('day14-input.txt', 'r')
lines = file.readlines()

x_min = sys.maxsize
x_max = 0
y_min = sys.maxsize
y_max = 0
paths = list()
for line in lines:
    path_string = line.strip().split(" -> ")
    path = list()
    for point_string in path_string:
        x_string, y_string = point_string.split(',')
        x = int(x_string)
        y = int(y_string)
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
        path.append(numpy.array([y, x]))
    paths.append(path)

cave = numpy.zeros((y_max + 1, x_max + 1), dtype=str)
for row in range(len(cave)):
    for column in range(len(cave[0])):
        cave[row, column] = '.'

for path in paths:
    for line_index in range(len(path) - 1):
        start = path[line_index]
        end = path[line_index + 1]
        row_start = min(start[0], end[0])
        row_end = max(start[0], end[0])
        for row_index in range(row_start, row_end + 1):
            cave[row_index, start[1]] = '#'
        column_start = min(start[1], end[1])
        column_end = max(start[1], end[1])
        for column_index in range(column_start, column_end + 1):
            cave[start[0], column_index] = '#'

sand_count = 0
to_abyss = False
while not to_abyss:
    sand_pos = numpy.array([0, 500])
    is_falling = True
    while is_falling:
        next_sand_pos = sand_pos + [1, 0]
        try:
            if cave[tuple(next_sand_pos)] == '.':
                # Straight down
                pass
            elif cave[tuple(sand_pos + (1, -1))] == '.':
                # Diagonally left
                next_sand_pos = sand_pos + (1, -1)
            elif cave[tuple(sand_pos + (1, 1))] == '.':
                # Diagonally right
                next_sand_pos = sand_pos + (1, 1)
            else:
                # Steady, new sand
                cave[tuple(sand_pos)] = 'o'
                is_falling = False

            if cave[tuple(next_sand_pos)] != '.':
                pass

            sand_pos = next_sand_pos
        except IndexError:
            to_abyss = True
            is_falling = False

    sand_count += 1
    print(f"Sand count is {sand_count}")

print(sand_count - 1)

# Part 2
y_max += 2
x_min = 0
x_max = 1000
paths.append([numpy.array([y_max, x_min]), numpy.array([y_max, x_max])])
cave = numpy.zeros((y_max + 1, x_max + 1), dtype=str)
for row in range(len(cave)):
    for column in range(len(cave[0])):
        cave[row, column] = '.'

for path in paths:
    for line_index in range(len(path) - 1):
        start = path[line_index]
        end = path[line_index + 1]
        row_start = min(start[0], end[0])
        row_end = max(start[0], end[0])
        for row_index in range(row_start, row_end + 1):
            cave[row_index, start[1]] = '#'
        column_start = min(start[1], end[1])
        column_end = max(start[1], end[1])
        for column_index in range(column_start, column_end + 1):
            cave[start[0], column_index] = '#'

sand_count = 0
while cave[0, 500] == '.':
    sand_pos = numpy.array([0, 500])
    is_falling = True
    while is_falling:
        next_sand_pos = sand_pos + [1, 0]
        try:
            if cave[tuple(next_sand_pos)] == '.':
                # Straight down
                pass
            elif cave[tuple(sand_pos + (1, -1))] == '.':
                # Diagonally left
                next_sand_pos = sand_pos + (1, -1)
            elif cave[tuple(sand_pos + (1, 1))] == '.':
                # Diagonally right
                next_sand_pos = sand_pos + (1, 1)
            else:
                # Steady, new sand
                cave[tuple(sand_pos)] = 'o'
                is_falling = False

            if cave[tuple(next_sand_pos)] != '.':
                pass

            sand_pos = next_sand_pos
        except IndexError:
            to_abyss = True
            is_falling = False

    sand_count += 1
    print(f"Sand count is {sand_count}")

print(sand_count)

