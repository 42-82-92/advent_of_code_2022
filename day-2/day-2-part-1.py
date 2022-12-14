# https://adventofcode.com/2022/day/2

# Problem Statement: Winner of the coveted camping spot has to win a rock, paper, scissors contest, but the strategy guide has too many entry's to tabulate by hand. 

# Goal: Determine the score as laid out by the strategy guide.

# Notes:
    # scoring:
        # Rock    = X = 1
        # Paper   = Y = 2
        # Scissors= Z = 3
        # Lost    = 0
        # Draw    = 3 
        # Win     = 6
    # brackets vs braces vs parentheses
        # Brackets are used to make lists
        # Braces are used to make dictionary
        # Parenthesis are used to make tuple
    # A dictionary will be needed so you can look up keys and return values

# Step 1:
# open the file and declare a list
f = open("input.txt", "r")
data = f.read()
lines = data.splitlines()

# Step 2:
# set variable values
# set a score counter
round = 0
final_score = 0

ROCK, PAPER, SCISSORS = "A", "B", "C"
my_hand = {"X": ROCK,"Y": PAPER, "Z": SCISSORS}
my_hand_values = {ROCK: 1, PAPER: 2, SCISSORS: 3}
round_scoring = {
    ROCK:     {ROCK: 3, PAPER: 6, SCISSORS: 0},
    PAPER:    {ROCK: 0, PAPER: 3, SCISSORS: 6},
    SCISSORS: {ROCK: 6, PAPER: 0, SCISSORS: 3},
}
for line in lines:
    plays = line.split(" ")
    other_player = plays[0]
    my_play = plays[1]
    # print(other_player, my_play)
    actual_play = my_hand[my_play]
    match_score = round_scoring[other_player][actual_play]
    round += match_score + my_hand_values[actual_play]
print(round)


# Step 3: 
# step through the list, adding each row, returning your round score.

# Step 3 part 2:
# step through the round scores, determine the final score of each round

# Step 4
# present the final score value. 
