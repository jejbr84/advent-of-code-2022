import numpy

file = open('day8-input.txt', 'r')
lines = file.readlines()

trees_array = []
for line in lines:
    trees_array.append(list(line.strip()))
trees = numpy.array(trees_array)

row_count = len(trees)
column_count = len(trees[0])
visible_count = 2 * row_count + 2 * column_count - 4
for row_index in range(1, row_count - 1):
    for column_index in range(1, column_count - 1):
        tree = trees[row_index, column_index]
        north = max(trees[0:row_index, column_index])
        south = max(trees[row_index + 1:row_count, column_index])
        west = max(trees[row_index, 0:column_index])
        east = max(trees[row_index, column_index + 1:column_count])
        if tree > north or tree > south or tree > west or tree > east:
            visible_count += 1

print(visible_count)


# Part 2
def calc_view_distance(height: int, neighbours: list):
    view_distance = len(neighbours)
    for index in range(len(neighbours)):
        if height <= int(neighbours[index]):
            view_distance = index + 1
            break
    return view_distance


scenic_score_max = 0
for row_index in range(1, row_count - 1):
    for column_index in range(1, column_count - 1):
        tree = int(trees[row_index, column_index])
        north = calc_view_distance(tree, trees[0:row_index, column_index][::-1])
        south = calc_view_distance(tree, trees[row_index + 1:row_count, column_index])
        west = calc_view_distance(tree, trees[row_index, 0:column_index][::-1])
        east = calc_view_distance(tree, trees[row_index, column_index + 1:column_count])
        scenic_score = north * south * west * east
        scenic_score_max = max(scenic_score_max, scenic_score)

print(scenic_score_max)
