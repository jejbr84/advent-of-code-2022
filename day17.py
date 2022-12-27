import numpy
import statsmodels.api as sm
import matplotlib.pyplot as plt

file = open('day17-input.txt', 'r')
gas_jets = file.read().strip()

rocks = list()
rocks.append([numpy.array([0, 0]), numpy.array([1, 0]), numpy.array([2, 0]), numpy.array([3, 0])])
rocks.append([numpy.array([0, 1]), numpy.array([1, 0]), numpy.array([1, 1]), numpy.array([1, 2]), numpy.array([2, 1])])
rocks.append([numpy.array([0, 0]), numpy.array([1, 0]), numpy.array([2, 0]), numpy.array([2, 1]), numpy.array([2, 2])])
rocks.append([numpy.array([0, 0]), numpy.array([0, 1]), numpy.array([0, 2]), numpy.array([0, 3])])
rocks.append([numpy.array([0, 0]), numpy.array([0, 1]), numpy.array([1, 0]), numpy.array([1, 1])])

rocks_x_max = list()
rocks_y_max = list()
for rock in rocks:
    rocks_x_max.append(max(rock, key=lambda x: x[0])[0])
    rocks_y_max.append(max(rock, key=lambda x: x[1])[1])


def does_hit_rock(rock, rock_pos, stopped_rock_rows):
    hit_rock = False
    for rock_part in rock:
        x = rock_pos[0] + rock_part[0]
        y = rock_pos[1] + rock_part[1]
        if stopped_rock_rows[y][x] == '#' or stopped_rock_rows[y][x] == 'O':
            hit_rock = True
            break
    return hit_rock


def determine_tower_height(rock_count):
    stopped_rock_rows = list()
    highest_rock = -1
    jet_count = 0
    for i in range(rock_count):
        rock_index = i % len(rocks)
        rock = rocks[rock_index]
        rock_pos = numpy.array([2, 4 + highest_rock])
        while len(stopped_rock_rows) <= rock_pos[1] + rocks_y_max[rock_index]:
            stopped_rock_rows.append(['.'] * 7)

        is_falling = True
        while is_falling:
            # Try to push rock.
            direction = 1 if gas_jets[jet_count % len(gas_jets)] == '>' else -1
            jet_count += 1
            new_rock_pos = rock_pos + (direction, 0)
            if new_rock_pos[0] >= 0 and new_rock_pos[0] + rocks_x_max[rock_index] < 7:
                if not does_hit_rock(rock, new_rock_pos, stopped_rock_rows):
                    # Can move sideways.
                    rock_pos = new_rock_pos

            # Try to move down.
            new_rock_pos = rock_pos + (0, -1)
            if new_rock_pos[1] < 0:
                # Reached floor
                is_falling = False
            elif does_hit_rock(rock, new_rock_pos, stopped_rock_rows):
                is_falling = False
            else:
                # Can move down.
                rock_pos = new_rock_pos

        # Add rock to stopped rocks.
        previous_highest_rock = highest_rock
        highest_rock = max(highest_rock, rock_pos[1] + rocks_y_max[rock_index])
        height_diffs.append(highest_rock - previous_highest_rock)
        char = 'O' if rock_index == 0 else '#'
        for rock_part in rock:
            stopped_rock_rows[rock_pos[1] + rock_part[1]][rock_pos[0] + rock_part[0]] = char

    return highest_rock + 1


height_diffs = list()
height = determine_tower_height(2022)
print(f"Height of the tower is {height}")

# Part 2
height_diffs = list()
determine_tower_height(10001)
# Autocorrelation shows the pattern repeats every 1725 rocks.
height_per_1725 = determine_tower_height(2725) - determine_tower_height(1000)
height = (1000000000000 // 1725)
height = height * height_per_1725  # This overflows, so gives wrong answer...
height = 1584927533696  # Windows calculator...
height += determine_tower_height(1000000000000 % 1725)
print(f"Height of the tower is {height}")

sm.graphics.tsa.plot_acf(height_diffs, lags=10000)
plt.show()

# Sample data:
# Pattern herhaalt zich elke 1400 iteraties, 2120 erbij. (eigenlijk elke 35)
# In 1.000.000.000.000 past 714.285.714x 1400, rest 400.
# 400 -> hoogte 608, plus 1.514.285.713.680 is 1.514.285.714.288
