'''
Problem Statement
You are given an M
timesN matrix filled with characters 'X' and 'O'. Your task is to capture all regions of 'O's that are "surrounded".
 
A region is captured by flipping all 'O's in that region to 'X's. A region of 'O's is considered surrounded if it is not connected to any 'O' on the border of the grid. A connection can be to an adjacent cell (up, down, left, or right).
The operation should be performed in-place on the given matrix.
 
Input Format
An MtimesN matrix of characters ('X' and 'O').
Output Format
The same matrix, with the surrounded 'O' regions flipped to 'X'.
 
Sample Case
Input Matrix:
 
[['X', 'X', 'X', 'X', 'X'],
 ['X', 'O', 'O', 'X', 'O'],
 ['X', 'X', 'O', 'X', 'O'],
 ['X', 'O', 'X', 'O', 'X'],
 ['O', 'O', 'O', 'X', 'X']]
Expected Output (in-place modification):
 
[['X', 'X', 'X', 'X', 'X'],
 ['X', 'O', 'O', 'X', 'O'],
 ['X', 'X', 'O', 'X', 'O'],
 ['X', 'O', 'X', 'X', 'X'],
['O', 'O', 'O', 'X', 'X']]
   Explanation:
The 'O's on the border (e.g., at (4,0) and (1,4)) are "safe". Any region of 'O's connected to these safe 'O's is also safe.
The large cluster of 'O's in the bottom-left is connected to the 'O' at (4,0) and is therefore safe. 
The two 'O's on the right edge are on the border, so they are safe.
The only 'O' that is not connected to any border 'O's is the one at (3,3). 
It forms a surrounded region of size 1 and is flipped to 'X'.
'''


# Input number of rows and columns
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

# Input each row as space-separated values
matrix = []
for i in range(rows):
    row = input(f"Enter row {i+1} (space-separated 'X' or 'O'): ").split()
    matrix.append(row)

# Print input matrix
print("\nInput Matrix:")
for row in matrix:
    print(row)


queue = []
for i in range(rows):
    if matrix[i][0] == 'O':
        matrix[i][0] = 'S'
        queue.append((i, 0))
    if matrix[i][cols-1] == 'O':
        matrix[i][cols-1] = 'S'
        queue.append((i, cols-1))

for j in range(cols):
    if matrix[0][j] == 'O':
        matrix[0][j] = 'S'
        queue.append((0, j))
    if matrix[rows-1][j] == 'O':
        matrix[rows-1][j] = 'S'
        queue.append((rows-1, j))

while queue:
    i, j = queue.pop(0)
    if i > 0 and matrix[i-1][j] == 'O':
        matrix[i-1][j] = 'S'
        queue.append((i-1, j))
    if i < rows-1 and matrix[i+1][j] == 'O':
        matrix[i+1][j] = 'S'
        queue.append((i+1, j))
    if j > 0 and matrix[i][j-1] == 'O':
        matrix[i][j-1] = 'S'
        queue.append((i, j-1))
    if j < cols-1 and matrix[i][j+1] == 'O':
        matrix[i][j+1] = 'S'
        queue.append((i, j+1))

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 'O':
            matrix[i][j] = 'X'
        elif matrix[i][j] == 'S':
            matrix[i][j] = 'O'

# Print modified matrix
print("\nModified Matrix:")
for row in matrix:
    print(row)


'''
Output:

Enter number of rows: 5
Enter number of columns: 5
Enter row 1 (space-separated 'X' or 'O'): X X X X X
Enter row 2 (space-separated 'X' or 'O'): X O O X O
Enter row 3 (space-separated 'X' or 'O'): X X O X O
Enter row 4 (space-separated 'X' or 'O'): X O X O X
Enter row 5 (space-separated 'X' or 'O'): O O O X X

Input Matrix:
['X', 'X', 'X', 'X', 'X']
['X', 'O', 'O', 'X', 'O']
['X', 'X', 'O', 'X', 'O']
['X', 'O', 'X', 'O', 'X']
['O', 'O', 'O', 'X', 'X']

Modified Matrix:
['X', 'X', 'X', 'X', 'X']
['X', 'X', 'X', 'X', 'O']
['X', 'X', 'X', 'X', 'O']
['X', 'O', 'X', 'X', 'X']
['O', 'O', 'O', 'X', 'X']

'''