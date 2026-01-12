import json


with open('records.json', 'r') as file:
    data = json.load(file)

teams = sorted(data.keys())
num_teams = len(teams)

matrix = [['' for _ in range(num_teams + 1)] for _ in range(num_teams + 1)]

# fill in the labels
for i in range(num_teams):
    matrix[0][i + 1] = teams[i]
    matrix[i + 1][0] = teams[i]

for i in range(num_teams):
    for j in range(num_teams):
        # Case 1: against itself -> N/A
        if teams[i] == teams[j]:
            matrix[i + 1][j + 1] = '-'
        # Case 2: fill in the number of wins first team has against second team
        else:
            matrix[i + 1][j + 1] = str(data[teams[i]][teams[j]]["W"])

matrix[0][0] = "  "

for i in range(num_teams + 1):
    for j in range(num_teams + 1):
        cell = matrix[i][j]
        # empty cell
        if i == 0 and j == 0:  
            print(f"{cell:3}", end="")
        # top row names
        elif i == 0: 
            print(f"{cell:4}", end="")
        # left side names
        elif j == 0:
            print(f"{cell:3}", end="")
        # filler spaces when team plays against itself
        elif cell == "-":  
            print(f"{cell:^4}", end="")
        else:  
            print(f"{cell:^4}", end="")
    print()
    


