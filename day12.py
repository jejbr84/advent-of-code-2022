import sys

file = open('day12-input.txt', 'r')
lines = file.readlines()

MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def process_node(position: tuple, steps_map: list, unvisited_set: dict):
    steps_to_node = steps_map[position[0]][position[1]]
    if steps_to_node == sys.maxsize:
        print(f"Error, node {position} has no steps assigned yet")
        exit(1)

    row = position[0]
    column = position[1]
    # steps_map[row][column] = steps_to_node
    height = ord(height_map[row][column])
    for move in MOVES:
        next_row = row + move[0]
        next_column = column + move[1]
        if 0 <= next_row < len(height_map) and 0 <= next_column < len(height_map[0]):
            # Next node is within map.
            next_height = ord(height_map[next_row][next_column])
            if (next_height - height) <= 1:
                # Next node is not to steep.
                if (next_row, next_column) in unvisited_set:
                    # Next node is not visited yet.
                    steps_to_next = steps_map[next_row][next_column]
                    if (steps_to_node + 1) < steps_to_next:
                        # Found a better path to node, assign the steps.
                        steps_map[next_row][next_column] = steps_to_node + 1
                        unvisited_set[(next_row, next_column)] = steps_to_node + 1

    # Done with node, mark as visited.
    unvisited_set.pop(position)


def find_shortest_path_to_end(start_pos: tuple) -> int:
    # Use Dijkstra's algorithm.
    steps_map = [[sys.maxsize] * len(height_map[0]) for _ in range(len(height_map))]
    unvisited_set = dict()
    reached_end = False
    for row in range(len(height_map)):
        for column in range(len(height_map[0])):
            unvisited_set[(row, column)] = sys.maxsize

    current_node = start_pos
    steps_map[start_pos[0]][start_pos[1]] = 0
    while end_pos in unvisited_set:
        process_node(current_node, steps_map, unvisited_set)

        # Select next node: the one with the smallest distance among the unvisited nodes.
        if len(unvisited_set) > 0:
            next_unvisited = min(unvisited_set.items(), key=lambda item: item[1])
            if next_unvisited[1] == sys.maxsize:
                break
            else:
                current_node = next_unvisited[0]
    else:
        reached_end = True

    return steps_map[end_pos[0]][end_pos[1]] if reached_end else sys.maxsize


height_map = []
start_pos = ()
end_pos = ()
for line in lines:
    start_token = line.find('S')
    if start_token != -1:
        start_pos = (len(height_map), start_token)

    end_token = line.find('E')
    if end_token != -1:
        end_pos = (len(height_map), end_token)

    map_row = list(line.strip())
    height_map.append(map_row)

height_map[start_pos[0]][start_pos[1]] = 'a'
height_map[end_pos[0]][end_pos[1]] = 'z'

print(find_shortest_path_to_end(start_pos))

# Part 2
possible_start_pos = set()
for row in range(len(height_map)):
    for column in range(len(height_map[0])):
        if height_map[row][column] == 'a':
            possible_start_pos.add((row, column))

print(possible_start_pos)

# Calculation takes a few minutes, but hey, what's that in a lifetime?
min_steps = sys.maxsize
best_start_pos = (-1, -1)
i = 0
for start_pos in possible_start_pos:
    i += 1
    print(f"At {i} of {len(possible_start_pos)}. Current minimum steps: {min_steps}")
    steps = find_shortest_path_to_end(start_pos)
    if steps < min_steps:
        min_steps = steps
        best_start_pos = start_pos

print(best_start_pos)
print(min_steps)
