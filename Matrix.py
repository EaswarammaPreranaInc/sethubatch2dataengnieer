'''
The program finds the largest element in a user-defined matrix and prints its row and column positions.
The function Matrix(x):
    Flattens the matrix into a single list using extend().
    Finds and returns the maximum value using max().
The main code takes matrix dimensions (row and col) and matrix elements from the user.
After finding the largest element, it loops through the matrix to print the row and column numbers (1-indexed) where the element occurs.
'''

def Matrix(x):
    b=[]
    for i in x:
        b.extend(i)
    m=max(b)
    return m
row=int(input("Enter Number of Rows: "))
col=int(input("Enter Number of Columns: "))
x=[[0]*col for _ in range(row)]
for i in range(row):
    for j in range(col):
        a=int(input(f"Enter element of matrix[{i}][{j}] : "))
        x[i][j] = a
b=Matrix(x)
print("Largest element : ",x)
for i in range(row):
    for j in range(col):
        if b == x[i][j]:    
            print("Row Number: ", i+1)
            print("Column Number: ", j+1)


'''

Output:

Enter Number of Rows: 3
Enter Number of Columns: 2
Enter element of matrix[0][0] : 1
Enter element of matrix[0][1] : 2
Enter element of matrix[1][0] : 3
Enter element of matrix[1][1] : 4
Enter element of matrix[2][0] : 5
Enter element of matrix[2][1] : 0
Matrix :  [[1, 2], [3, 4], [5, 0]]
Largest element :  5
Row Number:  3
Column Number:  1


'''