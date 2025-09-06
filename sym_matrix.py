'''
The program checks whether a given square matrix is symmetric.
A matrix is symmetric if l[i][j]=l[j][i] for all i,j
The function sym(l) loops through the upper triangle of the matrix and compares each element with its transpose counterpart.
If any element does not match, it returns False.
Otherwise, it returns True.
The main code takes the matrix size and the elements row by row from the user.
'''

def sym(l):
    for i in range(len(l)):
        for j in range(i+1):
            if l[i][j] != l[j][i]:
                return False
    return True

n=int(input("Enter size of the Matrix: "))
l=[]
for i in range(n):
    row=[]
    a=input(f"Enter {n} elements of the {i+1} row : ")
    col=a.split(" ")
    for x in col:
        row.append(int(x))
    l.append(row)
    row=[]
print(sym(l))


'''

Output:

Enter size of the Matrix: 3
Enter 3 elements of the 1 row : 1 2 3
Enter 3 elements of the 2 row : 2 4 5
Enter 3 elements of the 3 row : 3 5 6
True

Enter size of the Matrix: 2
Enter 2 elements of the 1 row : 1 0
Enter 2 elements of the 2 row : 2 1
False

'''