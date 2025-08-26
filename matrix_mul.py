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

