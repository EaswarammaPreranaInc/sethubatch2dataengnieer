'''
Sample Input:
1
1
1
2

sample output:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

Explanation:
Each variable x,y and z will have values of 0 or 1.
All permutations of lists in the form [i,j,k] = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]].
Remove all arrays that sum to n=2 to leave only the valid permutations.
'''



x = int(input())
y = int(input())
z = int(input())
n = int(input())
a = [[i,j,k] for i in range(x+1)for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(a)
