file = open('day6-input.txt', 'r')
message = file.read()

answer = 0
marker_size = 4
for index in range(len(message) - (marker_size - 1)):
    marker = set()
    for subindex in range(marker_size):
        marker.add(message[index + subindex])

    if len(marker) == marker_size:
        answer = index + marker_size
        break

print(answer)

# Part 2
answer = 0
marker_size = 14
for index in range(len(message) - (marker_size - 1)):
    marker = set()
    for subindex in range(marker_size):
        marker.add(message[index + subindex])

    if len(marker) == marker_size:
        answer = index + marker_size
        break

print(answer)
