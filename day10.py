file = open('day10-input.txt', 'r')
lines = file.readlines()

x_reg = 1
total_cycle_count = 0
signal_strength_sum = 0
for line in lines:
    instruction = line.strip().split()
    cycle_count = 1
    value = 0
    if instruction[0] == 'addx':
        cycle_count = 2
        value = int(instruction[1])

    for _ in range(cycle_count):
        total_cycle_count += 1
        if total_cycle_count in [20, 60, 100, 140, 180, 220]:
            signal_strength_sum += total_cycle_count * x_reg

    x_reg += value

print(signal_strength_sum)

# Part 2
x_reg = 1
total_cycle_count = 0
pixels = []
for line in lines:
    instruction = line.strip().split()
    cycle_count = 1
    value = 0
    if instruction[0] == 'addx':
        cycle_count = 2
        value = int(instruction[1])

    for _ in range(cycle_count):
        total_cycle_count += 1
        if x_reg - 1 <= ((total_cycle_count - 1) % 40) <= x_reg + 1:
            pixels.append('#')
        else:
            pixels.append('.')

    x_reg += value

print(*pixels[0:40])
print(*pixels[40:80])
print(*pixels[80:120])
print(*pixels[120:160])
print(*pixels[160:200])
print(*pixels[200:240])
