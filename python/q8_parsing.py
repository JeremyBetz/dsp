# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

input_file = csv.DictReader(open("football.csv"))

min_goalDifference = None
team = None
for row in input_file:
    goalDifference = abs(int(row["Goals"])-int(row["Goals Allowed"]))
    if min_goalDifference == None or min_goalDifference > goalDifference:
        min_goalDifference = goalDifference
        team = row["Team"]

print(team)
