file = open('day20-input.txt', 'r')
lines = file.readlines()


def calculate_coordinate(key: int, mix_count: int) -> int:
    values = [int(line.strip()) * key for line in lines]
    indices = [i for i in range(len(values))]

    for _ in range(mix_count):
        for index in range(len(indices)):
            source_index = indices.index(index)
            destination_index = (source_index + values[source_index]) % (len(values) - 1)

            index_pop = indices.pop(source_index)
            value_pop = values.pop(source_index)

            indices.insert(destination_index, index_pop)
            values.insert(destination_index, value_pop)

            # print(values)

    coordinates = 0
    value_0_index = values.index(0)
    for index in range(value_0_index + 1000, value_0_index + 4000, 1000):
        coordinates += values[index % len(values)]

    return coordinates


print(f"Coordinates is {calculate_coordinate(1, 1)}")

# Part 2
print(f"Coordinates is {calculate_coordinate(811589153, 10)}")
