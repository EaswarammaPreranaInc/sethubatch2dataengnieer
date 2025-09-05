#Tarun Banala (089)  03-09-2025

#Question 1
''' Problem Statement
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
Player 1, playing to maximize their score, anticipates both outcomes. They will choose Option B because it results in a higher score (11 vs 9).'''

#Answer 

from functools import lru_cache

def optimal_score(matrix):
    rows, cols = len(matrix), len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    def in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    @lru_cache(maxsize=None)
    def dfs(p1x, p1y, p2x, p2y, turn, visited_mask):
        def is_visited(x, y):
            return (visited_mask >> (x * cols + y)) & 1

        def set_visited(x, y):
            return visited_mask | (1 << (x * cols + y))

        if turn == 1:  # Player 1's turn
            best_score = float('-inf')
            moved = False
            for dx, dy in directions:
                nx, ny = p1x + dx, p1y + dy
                if in_bounds(nx, ny) and not is_visited(nx, ny):
                    moved = True
                    new_mask = set_visited(nx, ny)
                    next_score = dfs(nx, ny, p2x, p2y, 2, new_mask)
                    best_score = max(best_score, matrix[nx][ny] + next_score)
            if not moved:
                return 0
            return best_score
        else:  # Player 2's turn
            worst_score = float('inf')
            moved = False
            for dx, dy in directions:
                nx, ny = p2x + dx, p2y + dy
                if in_bounds(nx, ny) and not is_visited(nx, ny):
                    moved = True
                    new_mask = set_visited(nx, ny)
                    next_score = dfs(p1x, p1y, nx, ny, 1, new_mask)
                    worst_score = min(worst_score, next_score)
            if not moved:
                return dfs(p1x, p1y, p2x, p2y, 1, visited_mask)
            return worst_score

    # Initial positions
    p1_start = (0, 0)
    p2_start = (0, len(matrix[0]) - 1)

    # Initial visited mask
    start_mask = 0
    start_mask |= (1 << (p1_start[0] * cols + p1_start[1]))
    start_mask |= (1 << (p2_start[0] * cols + p2_start[1]))

    # Start with initial score from (0,0), Player 1's starting cell
    return matrix[0][0] + dfs(p1_start[0], p1_start[1], p2_start[0], p2_start[1], 2, start_mask)
