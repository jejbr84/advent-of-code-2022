file = open('day15-input.txt', 'r')
lines = file.readlines()

sensors = dict()
for line in lines:
    instruction = line.strip().split()
    x = instruction[2][2:-1]
    y = instruction[3][2:-1]
    sensor = (int(x), int(y))
    x = instruction[8][2:-1]
    y = instruction[9][2:]
    beacon = (int(x), int(y))
    sensors[sensor] = beacon

y_eval = 2000000
y_no_beacon = set()
for sensor, beacon in sensors.items():
    distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    y_distance = abs(sensor[1] - y_eval)
    if y_distance <= distance:
        # In range of y to evaluate, add all x-positions.
        x_diff = distance - y_distance
        y_no_beacon = y_no_beacon.union(range(sensor[0] - x_diff, sensor[0] + x_diff + 1))

# Remove beacons on the y to evaluate.
for beacon in sensors.values():
    if beacon[1] == y_eval:
        y_no_beacon.discard(beacon[0])

print(len(y_no_beacon))

# Part 2
xy_max = 4000000
for y_eval in range(0, xy_max + 1):
    print(f"y_eval = {y_eval}")
    y_no_beacon_ranges = list()
    for sensor, beacon in sensors.items():
        distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
        y_distance = abs(sensor[1] - y_eval)
        if y_distance <= distance:
            # In range of y to evaluate, add all x-positions.
            x_diff = distance - y_distance
            x_start = max(sensor[0] - x_diff, 0)
            x_end = min(sensor[0] + x_diff, xy_max)
            # Using a set is way too slow.
            # y_no_beacon = y_no_beacon.union(range(x_start, x_end + 1))
            y_no_beacon_ranges.append([x_start, x_end])

    y_no_beacon_ranges.sort(key=lambda item: item[0])
    is_found = False
    x_hidden = -1
    if y_no_beacon_ranges[0][0] != 0:
        # x = 0 is empty, hidden beacon is here.
        is_found = True
        x_hidden = 0
    else:
        x_max = 0
        for range_index in range(0, len(y_no_beacon_ranges) - 1):
            x_max = max(x_max, y_no_beacon_ranges[range_index][1])
            if x_max < y_no_beacon_ranges[range_index + 1][0]:
                # Empty position, hidden beacon is here.
                is_found = True
                x_hidden = y_no_beacon_ranges[range_index][1] + 1

        if x_max != xy_max and y_no_beacon_ranges[-1][1] != xy_max:
            # x = xy_max is empty, hidden beacon is here.
            is_found = True
            x_hidden = xy_max

    if is_found:
        print((x_hidden, y_eval))
        print(x_hidden * 4000000 + y_eval)
        break
