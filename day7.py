file = open('day7-input.txt', 'r')
lines = file.readlines()


class Directory:
    def __init__(self, parent_dir):
        self.subdirs: dict = {}
        self.files: list[tuple] = []
        self.parent: Directory = self if parent_dir is None else parent_dir
        self.total_size = 0

    def calculate_total_size(self) -> int:
        total_file_size = sum(file[0] for file in self.files)
        total_dir_size = sum(subdir.calculate_total_size() for subdir in self.subdirs.values())
        self.total_size = total_file_size + total_dir_size
        return self.total_size

    def get_sizes(self, sizes):
        sizes.append(self.total_size)
        for subdir in self.subdirs.values():
            subdir.get_sizes(sizes)


root_dir = Directory(None)
current_dir = root_dir
for line in lines:
    line = line.strip().split(' ')
    if line[0] == '$':
        if line[1] == "cd":
            dir_name = line[2]
            if dir_name == '/':
                pass
            elif dir_name == "..":
                current_dir = current_dir.parent
            else:
                if dir_name not in current_dir.subdirs:
                    print(f"Error, directory {dir_name} does not exist")
                    exit(1)
                current_dir = current_dir.subdirs[dir_name]
    else:
        if line[0] == 'dir':
            if line[1] not in current_dir.subdirs:
                current_dir.subdirs[line[1]] = Directory(current_dir)
            else:
                print(f"Error, directory {line[1]} already exists")
                exit(1)
        else:
            file = (int(line[0]), line[1])
            current_dir.files.append(file)

root_dir.calculate_total_size()
sizes = []
root_dir.get_sizes(sizes)
print(sum(size for size in sizes if size <= 100000))


# Part 2
sizes.sort()
print(f"Occupied space is {sizes[-1]}")
free_space = 70000000 - sizes[-1]
print(f"Free space is {free_space}")
to_be_freed = 30000000 - free_space
print(f"To be freed space is {to_be_freed}")
to_free_sizes = list(size for size in sizes if size >= to_be_freed)
print(f"Dir size to free is {to_free_sizes[0]}")
