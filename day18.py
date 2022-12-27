import numpy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file = open('day18-input.txt', 'r')
lines = file.readlines()

cubes = list()
for line in lines:
    split_line = line.strip().split(',')
    cubes.append((int(split_line[0]), int(split_line[1]), int(split_line[2])))

connection_count = 0

# Connections in z-direction.
cubes_sort = sorted(cubes, key=lambda cube: (cube[0], cube[1], cube[2]))
# print(cubes_sort)
for cube_index in range(len(cubes_sort) - 1):
    this_cube = cubes_sort[cube_index]
    next_cube = cubes_sort[cube_index + 1]
    if this_cube[0] == next_cube[0] and this_cube[1] == next_cube[1] and next_cube[2] - this_cube[2] == 1:
        connection_count += 1
print(connection_count)

# Connections in y-direction.
cubes_sort = sorted(cubes, key=lambda cube: (cube[0], cube[2], cube[1]))
# print(cubes_sort)
for cube_index in range(len(cubes_sort) - 1):
    this_cube = cubes_sort[cube_index]
    next_cube = cubes_sort[cube_index + 1]
    if this_cube[0] == next_cube[0] and this_cube[2] == next_cube[2] and next_cube[1] - this_cube[1] == 1:
        connection_count += 1
print(connection_count)

# Connections in x-direction.
cubes_sort = sorted(cubes, key=lambda cube: (cube[2], cube[1], cube[0]))
# print(cubes_sort)
for cube_index in range(len(cubes_sort) - 1):
    this_cube = cubes_sort[cube_index]
    next_cube = cubes_sort[cube_index + 1]
    if this_cube[1] == next_cube[1] and this_cube[2] == next_cube[2] and next_cube[0] - this_cube[0] == 1:
        connection_count += 1
print(connection_count)

surface_area = 6 * len(cubes) - 2 * connection_count
print(f"Surface area is {surface_area}")

# Part 2


def interior_faces_z(x, y, z) -> int:
    interior_face = 0
    x_range = [cube[0] for cube in cubes_sort_x if cube[1] == y and cube[2] == z]
    y_range = [cube[1] for cube in cubes_sort_y if cube[0] == x and cube[2] == z]
    if x_range and x_range[0] < x < x_range[-1] and y_range and y_range[0] < y < y_range[-1]:
        interior_face = 1
        cubes_interior.add((x, y, z))
    return interior_face


def interior_faces_y(x, y, z) -> int:
    interior_face = 0
    x_range = [cube[0] for cube in cubes_sort_x if cube[1] == y and cube[2] == z]
    z_range = [cube[2] for cube in cubes_sort_z if cube[0] == x and cube[1] == y]
    if x_range and x_range[0] < x < x_range[-1] and z_range and z_range[0] < z < z_range[-1]:
        interior_face = 1
        cubes_interior.add((x, y, z))
    return interior_face


def interior_faces_x(x, y, z) -> int:
    interior_face = 0
    y_range = [cube[1] for cube in cubes_sort_y if cube[0] == x and cube[2] == z]
    z_range = [cube[2] for cube in cubes_sort_z if cube[0] == x and cube[1] == y]
    if y_range and y_range[0] < y < y_range[-1] and z_range and z_range[0] < z < z_range[-1]:
        interior_face = 1
        cubes_interior.add((x, y, z))
    return interior_face


connection_count = 0
interior_faces = 0
cubes_interior = set()
cubes_sort_z = sorted(cubes, key=lambda cube: (cube[0], cube[1], cube[2]))
cubes_sort_y = sorted(cubes, key=lambda cube: (cube[0], cube[2], cube[1]))
cubes_sort_x = sorted(cubes, key=lambda cube: (cube[2], cube[1], cube[0]))

# Connections in z-direction.
for cube_index in range(len(cubes_sort_z) - 1):
    this_cube = cubes_sort_z[cube_index]
    next_cube = cubes_sort_z[cube_index + 1]
    if this_cube[0] == next_cube[0] and this_cube[1] == next_cube[1]:
        distance_to_next = next_cube[2] - this_cube[2]
        if distance_to_next == 1:
            connection_count += 1
        elif distance_to_next > 1:
            # Check if empty space after this cube and just before next cube is surrounded in other directions.
            interior_faces += interior_faces_z(this_cube[0], this_cube[1], this_cube[2] + 1)
            interior_faces += interior_faces_z(next_cube[0], next_cube[1], next_cube[2] - 1)
print(connection_count)
print(interior_faces)


# Connections in y-direction.
for cube_index in range(len(cubes_sort_y) - 1):
    this_cube = cubes_sort_y[cube_index]
    next_cube = cubes_sort_y[cube_index + 1]
    if this_cube[0] == next_cube[0] and this_cube[2] == next_cube[2]:
        distance_to_next = next_cube[1] - this_cube[1]
        if distance_to_next == 1:
            connection_count += 1
        elif distance_to_next > 1:
            # Check if empty space after this cube and just before next cube is surrounded in other directions.
            interior_faces += interior_faces_y(this_cube[0], this_cube[1] + 1, this_cube[2])
            interior_faces += interior_faces_y(next_cube[0], next_cube[1] - 1, next_cube[2])
print(connection_count)
print(interior_faces)


# Connections in x-direction.
for cube_index in range(len(cubes_sort_x) - 1):
    this_cube = cubes_sort_x[cube_index]
    next_cube = cubes_sort_x[cube_index + 1]
    if this_cube[1] == next_cube[1] and this_cube[2] == next_cube[2]:
        distance_to_next = next_cube[0] - this_cube[0]
        if distance_to_next == 1:
            connection_count += 1
        elif distance_to_next > 1:
            # Check if empty space after this cube and just before next cube is surrounded in other directions.
            interior_faces += interior_faces_x(this_cube[0] + 1, this_cube[1], this_cube[2])
            interior_faces += interior_faces_x(next_cube[0] - 1, next_cube[1], next_cube[2])

print(connection_count)
print(interior_faces)

surface_area = 6 * len(cubes) - 2 * connection_count - interior_faces
print(f"Surface area is {surface_area}, (connections: {connection_count}, interior faces: {interior_faces})")
# This is not the correct answer (2480), because there are 3 holes that are seen as interior, while exterior.
# Just manually counted the faces in these holes (14), giving the correct answer (2494).
# Apparently should have used 'flood flow' algorithm.

space_size = 25
cubes_plot = cubes
# cubes_plot = [cube for cube in cubes if cube[2] <= 4]
space_cubes = numpy.zeros(space_size * space_size * space_size, dtype=bool).reshape((space_size, space_size, space_size))
for cube in cubes_plot:
    space_cubes[cube] = True

space_interior = numpy.zeros(space_size * space_size * space_size, dtype=bool).reshape((space_size, space_size, space_size))
for cube in cubes_interior:
    space_interior[cube] = True

# combine the objects into a single boolean array
voxels = space_cubes | space_interior

# set the colors of each object
colors = numpy.empty(voxels.shape, dtype=object)
colors[space_cubes] = 'blue'
colors[space_interior] = 'red'

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.voxels(voxels, facecolors=colors, edgecolors='grey')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
