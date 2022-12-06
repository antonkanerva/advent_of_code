def part_one_points(opener, response):
    """Calculates the points of a Rocker, Paper, Scissors game based on chosen response and the outcome of the game."""
    points = 0

    # Points for chosen response
    if response == "X":  # Rock
        points += 1
    elif response == "Y":  # Paper
        points += 2
    elif response == "Z":  # Scissors
        points += 3

    # Points for game outcome
    if opener == "A":  # Rock
        if response == "X":  # Rock
            points += 3  # Draw
        elif response == "Y":  # Paper
            points += 6  # Win
        elif response == "Z":  # Scissors
            points += 0  # Lose
    elif opener == "B":  # Paper
        if response == "X":  # Rock
            points += 0  # Lose
        elif response == "Y":  # Paper
            points += 3  # Draw
        elif response == "Z":  # Scissors
            points += 6  # Win
    elif opener == "C":  # Scissors
        if response == "X":  # Rock
            points += 6  # Win
        elif response == "Y":  # Paper
            points += 0  # Lose
        elif response == "Z":  # Scissors
            points += 3  # Draw

    return points


with open("input.txt") as file:
    games = [line.rstrip().split(" ") for line in file]

# Part 1
game_points = [part_one_points(game[0], game[1]) for game in games]
sum_of_points = sum(game_points)
print(f"Part 1: {sum_of_points=}")

# Part 2
score = {
    "X": {"outcome": 0, "A": 3, "B": 1, "C": 2},
    "Y": {"outcome": 3, "A": 1, "B": 2, "C": 3},
    "Z": {"outcome": 6, "A": 2, "B": 3, "C": 1}
}
game_points = [score[game[1]]["outcome"] + score[game[1]][game[0]] for game in games]
print(f"Part 2: {sum(game_points)=}")

