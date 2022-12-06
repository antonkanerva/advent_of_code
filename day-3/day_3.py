def get_common_items(rucksacks: list, part: int):
    if part == 1:
        rs_compartments = [(rs[:int(len(rs) / 2)], rs[int(len(rs) / 2):]) for rs in rucksacks]
        common_items = [list(set(compartments[0]).intersection(set(compartments[1])))[0] for compartments in rs_compartments]
    else:  # Part 2
        rucksack_groups = []
        for i in range(int(len(rucksacks)/3)):
            rs_group = [rucksacks[i * 3], rucksacks[i * 3 + 1], rucksacks[i * 3 + 2]]
            rucksack_groups.append(rs_group)
        common_items = [list(set(rs_group[0]).intersection(set(rs_group[1])).intersection(rs_group[2]))[0] for rs_group in rucksack_groups]
    return common_items


with open("input.txt") as file:
    rucksacks = [line.rstrip() for line in file]

# Part 1
priorities = [ord(item) - 96 if item.islower() else ord(item) - 38 for item in get_common_items(rucksacks=rucksacks, part=1)]
print(f"Part 1: {sum(priorities)=}")

# Part 2
priorities = [ord(item) - 96 if item.islower() else ord(item) - 38 for item in get_common_items(rucksacks=rucksacks, part=2)]
print(f"Part 2: {sum(priorities)=}")
