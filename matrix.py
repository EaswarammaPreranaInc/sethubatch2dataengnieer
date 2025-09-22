'''
Question:
Write a program to check whether a given square matrix is a Unit (Identity) Matrix or not.
A Unit Matrix has 1s on its diagonal and 0s elsewhere.
'''

def matrix(nums):
    for i in range(len(nums)):
        for j in range(len(nums[0])):
            if i == j and nums[i][j] != 1:
                return "The given matrix is not a Unit Matrix"
            if i != j and nums[i][j] != 0:
                return "The given matrix is not a Unit Matrix"
    return "The given matrix is a Unit Matrix"

n = int(input("Enter size of the Matrix: "))
nums = []
for i in range(n):
    row = []
    a = input(f"Enter {n} elements of row {i+1}: ")
    col = a.split()
    for x in col:
        row.append(int(x))
    nums.append(row)

print(matrix(nums))

'''
Output 1:
Enter size of the Matrix: 3
Enter 3 elements of row 1: 1 0 0
Enter 3 elements of row 2: 0 1 0
Enter 3 elements of row 3: 0 0 1
The given matrix is a Unit Matrix

Output 2:
Enter size of the Matrix: 2
Enter 2 elements of row 1: 1 1
Enter 2 elements of row 2: 0 1
The given matrix is not a Unit Matrix
'''
