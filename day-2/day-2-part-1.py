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

# Step 1:
# open the file and declare a list
f = open("input.txt", "r")
lines = f.readlines()

# Step 2:
# set variable values
# set a score counter
round = 0
final_score = 0

# Step 3: 
# step through the list, adding each row, returning your round score.

# Step 3 part 2:
# step through the round scores, determine the final score of each round

# Step 4
# present the final score value. 
