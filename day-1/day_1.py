with open("input.txt") as file:
    lines = [int(line.rstrip()) if line.rstrip() != "" else -1 for line in file]

nr_of_lines = len(lines)
empty_line_indices = [idx + 1 for idx, val in enumerate(lines) if val == -1]
line_chunks = [lines[i:j-1] for i, j in zip(
    [0] + empty_line_indices,
    empty_line_indices + ([nr_of_lines] if empty_line_indices[-1] != nr_of_lines else [])
)]
calory_sums = [sum(calories) for calories in line_chunks]

# Part 1
maximum_calory_count = max(calory_sums)
print(f"Part 1: {maximum_calory_count=}")

# Part 2
top_3_sorted_calory_sums = sorted(calory_sums, reverse=True)[:3]
top_3_calory_count = sum(top_3_sorted_calory_sums)
print(f"Part 2: {top_3_calory_count=}")
