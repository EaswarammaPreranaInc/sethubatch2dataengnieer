'''
Problem Statement
Two players, Player 1 (Maximizer) and Player 2 (Minimizer), play a game on an MtimesN matrix of integers. The board contains both positive and negative scores.
 
Game Rules:
Player 1 starts at cell (0, 0), and Player 2 starts at (0, N-1). The starting cells are considered visited, and their values are part of the players' initial state.
Player 1 moves first. The players take turns moving their token to an unvisited adjacent cell (up, down, left, or right).
The game ends when the current player cannot make a valid move (i.e., all adjacent cells are either visited or out-of-bounds).
Player 1's score is the sum of values of all cells they have visited. Player 2 does not have their own score; their sole purpose is to make moves that minimize Player 1's final score. Player 1's goal is to maximize their final score.
Assuming both players play optimally, what is Player 1's final score?
Input Format
A 2D integer matrix (or list of lists) representing the game board.
Output Format
A single integer representing Player 1's final score, assuming optimal play from both sides.
Sample Case
Input Matrix:
[[1, 10],
 [8,  2]]
Expected Output:
9
Explanation:
Player 1 starts at 1. Player 2 starts at 2. It's Player 1's turn.
Option A: Player 1 moves down to 8. Player 1's path is 1 -> 8, and their current score is 9. Now it's Player 2's turn. Player 2 at 2 moves to 10 to block Player 1. Now Player 1 at 8 is trapped. The game ends. Player 1's final score is 9.
Option B: Player 1 moves right to 10. Player 1's path is 1 -> 10, and their current score is 11. Now it's Player 2's turn. Player 2 at 2 moves to 8 to block Player 1. Now Player 1 at 10 is trapped. The game ends. Player 1's final score is 11.
Player 1, playing to maximize their score, anticipates both outcomes. They will choose Option B because it results in a higher score (11 vs 9).
'''

# Input rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input the matrix
matrix = []
for i in range(rows):
    row_vals = []
    for j in range(cols):
        val = int(input(f"Enter value for cell [{i}][{j}]: "))
        row_vals.append(val)
    matrix.append(row_vals)

# Print the matrix
print("\nMatrix:")
for i in range(rows):
    print(matrix[i])

visited = [[False]*cols for _ in range(rows)]

i1, j1 = 0, 0
i2, j2 = 0, cols-1

row1, col1, row2, col2 = i1, j1, i2, j2

visited[row1][col1] = True
visited[row2][col2] = True

score1 = matrix[row1][col1]


turn = 1  
while True:
    moved = False
    next_row, next_col = -1, -1

    if turn == 1:
        if row1 > 0 and not visited[row1-1][col1] and matrix[row1-1][col1] > next_row:
            next_row, next_col = row1-1, col1
            moved = True
        if row1 < rows-1 and not visited[row1+1][col1] and matrix[row1+1][col1] > next_row:
            next_row, next_col = row1+1, col1
            moved = True
        if col1 > 0 and not visited[row1][col1-1] and matrix[row1][col1-1] > next_row:
            next_row, next_col = row1, col1-1
            moved = True
        if col1 < cols-1 and not visited[row1][col1+1] and matrix[row1][col1+1] > next_row:
            next_row, next_col = row1, col1+1
            moved = True

        if moved:
            row1, col1 = next_row, next_col
            visited[row1][col1] = True
            score1 += matrix[row1][col1]
        turn = 2

    else:
        if row2 > 0 and not visited[row2-1][col2]:
            row2 -= 1
            moved = True
        elif row2 < rows-1 and not visited[row2+1][col2]:
            row2 += 1
            moved = True
        elif col2 > 0 and not visited[row2][col2-1]:
            col2 -= 1
            moved = True
        elif col2 < cols-1 and not visited[row2][col2+1]:
            col2 += 1
            moved = True

        if moved:
            visited[row2][col2] = True
        turn = 1

    if not moved:
        break

print("Player 1 final score:", score1)

'''
Output:

Enter number of rows: 2
Enter number of rows: 2
Enter number of columns: 2
Enter number of columns: 2
Enter value for cell [0][0]: 5
Enter value for cell [0][0]: 5
Enter value for cell [0][1]: 10
Enter value for cell [0][1]: 10
Enter value for cell [1][0]: 6
Enter value for cell [1][1]: 1

Matrix:
[5, 10]
[6, 1]
Player 1 final score: 11
'''
