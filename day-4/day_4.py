with open("input.txt") as file:
    pairs = [line.rstrip().split(",") for line in file]

elf_pairs = [{"elf_1": pair[0].split("-"), "elf_2": pair[1].split("-")} for pair in pairs]
elf_pairs = [{
    "elf_1": {"lower": int(pair["elf_1"][0]), "upper": int(pair["elf_1"][1])},
    "elf_2": {"lower": int(pair["elf_2"][0]), "upper": int(pair["elf_2"][1])}
} for pair in elf_pairs]

# Part 1
fully_contained = [
    (pair["elf_1"]["lower"] <= pair["elf_2"]["lower"] and pair["elf_1"]["upper"] >= pair["elf_2"]["upper"]) or  # Elf 1 contains elf 2
    (pair["elf_1"]["lower"] >= pair["elf_2"]["lower"] and pair["elf_1"]["upper"] <= pair["elf_2"]["upper"])  # Elf 2 contains elf 1
    for pair in elf_pairs
]
print(f"Part 1: {fully_contained.count(True)=}")

# Part 2
overlaps = [
    (pair["elf_1"]["lower"] <= pair["elf_2"]["lower"] and pair["elf_1"]["upper"] >= pair["elf_2"]["upper"]) or  # Elf 1 contains elf 2
    (pair["elf_1"]["lower"] >= pair["elf_2"]["lower"] and pair["elf_1"]["upper"] <= pair["elf_2"]["upper"]) or  # Elf 2 contains elf 1
    (pair["elf_1"]["lower"] <= pair["elf_2"]["lower"] <= pair["elf_1"]["upper"]) or  # Elf 1 "left overlaps" elf 2
    (pair["elf_1"]["lower"] <= pair["elf_2"]["upper"] <= pair["elf_1"]["upper"])  # Elf 1 "right overlaps" elf 2
    for pair in elf_pairs
]
print(f"Part 2: {overlaps.count(True)=}")
