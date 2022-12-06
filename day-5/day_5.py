def rearrange(stacks: dict, rearrangements: list, part: int):
    for rearrangement in rearrangements:
        crates_to_move = stacks[rearrangement["from"]][-rearrangement["quantity"]:]
        if part == 1:
            crates_to_move = crates_to_move[::-1]
        stacks[rearrangement["to"]] = stacks[rearrangement["to"]] + crates_to_move
        stacks[rearrangement["from"]] = stacks[rearrangement["from"]][:-rearrangement["quantity"]]
    return stacks


def get_top_crates(stacks: dict):
    top_crates = ""
    for idx, stack in stacks.items():
        top_crates = top_crates + stack[-1]
    return top_crates


procedures = []
with open("input.txt") as file:
    for line in file:
        if "move" in line:
            procedures.append(line.rstrip().split(" "))

stacks = {
    1: "ZJNWPS",
    2: "GST",
    3: "VQRLH",
    4: "VSTD",
    5: "QZTDBMJ",
    6: "MWTJDCZL",
    7: "LPMWGTJ",
    8: "NGMTBFQH",
    9: "RDGCPBQW"
}
rearrangements = [{"quantity": int(procedure[1]), "from": int(procedure[3]), "to": int(procedure[5])} for procedure in procedures]

# Part 1
rearranged_stacks = rearrange(stacks.copy(), rearrangements, part=1)
top_crates = get_top_crates(rearranged_stacks)
print(f"Part 1: {top_crates=}")

# Part 2
rearranged_stacks = rearrange(stacks.copy(), rearrangements, part=2)
top_crates = get_top_crates(rearranged_stacks)
print(f"Part 2: {top_crates=}")
