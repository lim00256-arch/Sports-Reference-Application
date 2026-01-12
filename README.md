# Sports-Reference-Application
## Opening the file
The file is first opened in read mode, and teams and num_teams variables are created to store the names of the teams and the number of teams.
The variable matrix, which stores a 2D array representing the final product, is also created.

## Filling in labels
Using a for loop, both sides of the labels on the 2D array are filled in, drawing from the team names stored in list teams.

## Filling in data
Using double for loop, loop through every cell in the matrix. We fill each cell in with the data given in the file, looking up how many wins the current row team has against the current column team.

## Printing the data
We first set the matrix[0][0] cell to be an empty string.
Then, we print every cell in the matrix with a double for loop, accounting for any space imbalance.
