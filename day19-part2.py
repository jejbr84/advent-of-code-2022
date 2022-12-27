import copy

file = open('day19-input.txt', 'r')
lines = file.readlines()


class Resources:
    def __init__(self, ore, clay, obsidian):
        self.ore = ore
        self.clay = clay
        self.obsidian = obsidian


class Status:
    def __init__(self):
        self.resources = Resources(0, 0, 0)
        self.ore_robot_count = 0
        self.clay_robot_count = 0
        self.obsidian_robot_count = 0
        self.geode_robot_count = 0
        self._geode_count = 0
        self._minute_count = 0
        self._ore_robot_pending = False
        self._clay_robot_pending = False
        self._obsidian_robot_pending = False
        self._geode_robot_pending = False

    def run_minute(self):
        self._minute_count += 1
        self.resources.ore += self.ore_robot_count
        self.resources.clay += self.clay_robot_count
        self.resources.obsidian += self.obsidian_robot_count
        self._geode_count += self.geode_robot_count
        if self._ore_robot_pending:
            self.ore_robot_count += 1
            self._ore_robot_pending = False
        if self._clay_robot_pending:
            self.clay_robot_count += 1
            self._clay_robot_pending = False
        if self._obsidian_robot_pending:
            self.obsidian_robot_count += 1
            self._obsidian_robot_pending = False
        if self._geode_robot_pending:
            self.geode_robot_count += 1
            self._geode_robot_pending = False

    def get_minute_count(self) -> int:
        return self._minute_count

    def get_geode_count(self) -> int:
        return self._geode_count

    def add_ore_robot(self):
        self._ore_robot_pending = True

    def add_clay_robot(self):
        self._clay_robot_pending = True

    def add_obsidian_robot(self):
        self._obsidian_robot_pending = True

    def add_geode_robot(self):
        self._geode_robot_pending = True


class BluePrint:
    def __init__(self, text: str):
        words = text.split()
        self.ore_robot_costs = Resources(int(words[6]), 0, 0)
        self.clay_robot_costs = Resources(int(words[12]), 0, 0)
        self.obsidian_robot_costs = Resources(int(words[18]), int(words[21]), 0)
        self.geode_robot_costs = Resources(int(words[27]), 0, int(words[30]))

    def can_build_ore_robot(self, resources: Resources, do_build=False) -> bool:
        return self.__can_build_robot(self.ore_robot_costs, resources, do_build)

    def can_build_clay_robot(self, resources: Resources, do_build=False) -> bool:
        return self.__can_build_robot(self.clay_robot_costs, resources, do_build)

    def can_build_obsidian_robot(self, resources: Resources, do_build=False) -> bool:
        return self.__can_build_robot(self.obsidian_robot_costs, resources, do_build)

    def can_build_geode_robot(self, resources: Resources, do_build=False) -> bool:
        return self.__can_build_robot(self.geode_robot_costs, resources, do_build)

    def __can_build_robot(self, robot_costs: Resources, resources: Resources, do_build: bool) -> bool:
        can_build = False
        if resources.ore >= robot_costs.ore and resources.clay >= robot_costs.clay and resources.obsidian >= robot_costs.obsidian:
            can_build = True
            if do_build:
                resources.ore -= robot_costs.ore
                resources.clay -= robot_costs.clay
                resources.obsidian -= robot_costs.obsidian
        return can_build


blueprints = [BluePrint(line) for line in lines]
geode_counts = list()
for blueprint_index in range(3):
    blueprint = blueprints[blueprint_index]
    begin_status = Status()
    begin_status.ore_robot_count = 1
    status_queue = [begin_status]
    max_geode_count = 0
    best_geode_count = dict()

    max_ore_costs = max(blueprint.ore_robot_costs.ore, blueprint.clay_robot_costs.ore,
                        blueprint.obsidian_robot_costs.ore, blueprint.geode_robot_costs.ore)
    max_clay_costs = max(blueprint.ore_robot_costs.clay, blueprint.clay_robot_costs.clay,
                         blueprint.obsidian_robot_costs.clay, blueprint.geode_robot_costs.clay)
    max_obsidian_costs = max(blueprint.ore_robot_costs.obsidian, blueprint.clay_robot_costs.obsidian,
                             blueprint.obsidian_robot_costs.obsidian, blueprint.geode_robot_costs.obsidian)

    while status_queue:
        status = status_queue.pop(0)
        status.run_minute()
        if (status.get_minute_count() in best_geode_count.keys() and
                status.get_geode_count() < best_geode_count[status.get_minute_count()]):
            # There is a better path. Skip this one.
            continue
        else:
            best_geode_count[status.get_minute_count()] = status.get_geode_count()

        if status.get_minute_count() < 32:
            minutes_left = 32 - status.get_minute_count()
            if blueprint.can_build_geode_robot(status.resources):
                # Geode robot is always the best thing to build.
                new_status = copy.deepcopy(status)
                blueprint.can_build_geode_robot(new_status.resources, True)
                new_status.add_geode_robot()
                status_queue.append(new_status)
            else:
                if status.obsidian_robot_count < max_obsidian_costs:
                    if blueprint.can_build_obsidian_robot(status.resources):
                        new_status = copy.deepcopy(status)
                        blueprint.can_build_obsidian_robot(new_status.resources, True)
                        new_status.add_obsidian_robot()
                        status_queue.append(new_status)

                if status.ore_robot_count < max_ore_costs:
                    if blueprint.can_build_ore_robot(status.resources):
                        new_status = copy.deepcopy(status)
                        blueprint.can_build_ore_robot(new_status.resources, True)
                        new_status.add_ore_robot()
                        status_queue.append(new_status)

                if status.clay_robot_count < max_clay_costs:
                    if blueprint.can_build_clay_robot(status.resources):
                        new_status = copy.deepcopy(status)
                        blueprint.can_build_clay_robot(new_status.resources, True)
                        new_status.add_clay_robot()
                        status_queue.append(new_status)

                if status.resources.ore < max_ore_costs:
                    status_queue.append(copy.deepcopy(status))
        else:
            max_geode_count = max(max_geode_count, status.get_geode_count())

        if len(status_queue) % 10000 == 0:
            print(f"Queue length: {len(status_queue)}, minute: {status.get_minute_count()}")

    print(f"Blueprint {blueprint_index + 1} geode count: {max_geode_count}")
    geode_counts.append(max_geode_count)

multiplied_counts = 1
for count in geode_counts:
    multiplied_counts *= count
print(f"Multiplied counts: {multiplied_counts}")
