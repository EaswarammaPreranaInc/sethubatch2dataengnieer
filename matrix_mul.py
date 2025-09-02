'''
The program takes the order and elements of two matrices as input from the user.
It checks the condition for multiplication: number of columns of the first matrix must equal the number of rows of the second.
If valid, it multiplies the matrices using nested loops and stores the result in a new matrix.
Finally, it displays both input matrices and the resultant matrix.
'''

row1=int(input("Enter number of rows of 1st matrix: "))
col1=int(input("Enter number of columns of 1st matrix: "))
row2=int(input("Enter number of rows of 2nd matrix: "))
col2=int(input("Enter number of columns of 2nd matrix: "))

if col1 == row2:
    # Enter elements into matrix 1
    matrix1=[[0]*col1 for _ in range(row1)]
    for i in range(row1):
        for j in range(col1):
            ele=int(input(f'Enter matrix1[{i}][{j}] element: '))
            matrix1[i][j] = ele
    
    print("\nMatrix 1:")
    for row in matrix1:
        print(row)

    # Enter elements into matrix 2
    matrix2=[[0]*col2 for _ in range(row2)]
    for i in range(row2):
        for j in range(col2):
            ele=int(input(f'Enter matrix2[{i}][{j}] element: '))
            matrix2[i][j] = ele

    # Initialize result matrix (row1 × col2)
    matrix_mul=[[0]*col2 for _ in range(row1)]

    # Matrix multiplication
    for i in range(row1):
        for j in range(col2):
            for k in range(col1):   
                matrix_mul[i][j] += matrix1[i][k] * matrix2[k][j]

    print("\nMatrix 2:")
    for row in matrix2:
        print(row)

    print("\nResultant Matrix:")
    for row in matrix_mul:
        print(row)

else:
    print("Matrix multiplication not possible (col1 != row2)")

'''
Output:

Enter number of rows of 1st matrix: 2
Enter number of columns of 1st matrix: 3
Enter number of rows of 2nd matrix: 3
Enter number of columns of 2nd matrix: 2

Enter matrix1[0][0] element: 1
Enter matrix1[0][1] element: 2
Enter matrix1[0][2] element: 3
Enter matrix1[1][0] element: 4
Enter matrix1[1][1] element: 5
Enter matrix1[1][2] element: 6

Matrix 1:
[1, 2, 3]
[4, 5, 6]

Enter matrix2[0][0] element: 7
Enter matrix2[0][1] element: 8
Enter matrix2[1][0] element: 9
Enter matrix2[1][1] element: 10
Enter matrix2[2][0] element: 11
Enter matrix2[2][1] element: 12

Matrix 2:
[7, 8]
[9, 10]
[11, 12]

Resultant Matrix:
[58, 64]
[139, 154]

'''

