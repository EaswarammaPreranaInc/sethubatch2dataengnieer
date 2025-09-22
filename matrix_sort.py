'''
Question:
Write a program to sort each row of a matrix individually.
The program should take the number of rows and columns as input, then take the matrix elements row-wise.
'''

def matrix(nums):
    for i in range(len(nums)):
        nums[i].sort()
    return nums

rows = int(input("Enter number of rows of the Matrix: "))
cols = int(input("Enter number of columns of the Matrix: "))
nums = []
for i in range(rows):
    a = input(f"Enter {cols} elements of row {i+1}: ")
    col = a.split()
    row = [int(x) for x in col[:cols]]
    nums.append(row)

sorted_matrix = matrix(nums)
print("Sorted Matrix:")
for row in sorted_matrix:
    print(*row)

'''
Output 1:
Enter number of rows of the Matrix: 2
Enter number of columns of the Matrix: 3
Enter 3 elements of row 1: 3 1 2
Enter 3 elements of row 2: 6 5 4
Sorted Matrix:
1 2 3
4 5 6

Output 2:
Enter number of rows of the Matrix: 3
Enter number of columns of the Matrix: 3
Enter 3 elements of row 1: 9 7 8
Enter 3 elements of row 2: 3 1 2
Enter 3 elements of row 3: 6 5 4
Sorted Matrix:
7 8 9
1 2 3
4 5 6
'''
