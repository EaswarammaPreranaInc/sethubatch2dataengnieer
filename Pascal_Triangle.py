'''
The program prints Pascal’s Triangle up to n rows.
It defines a function pascal(n) which loops over each row i (0 to n-1).
For each element j in row i, it calculates the binomial coefficient using:
using math.factorial().
Spaces are added before each row for triangle formatting, and each row is printed line by line.
'''

import math
def pascal(n):
    for i in range(n):
        print(" "*(n-i),end="")
        for j in range(i+1):
            Value=math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
            print(Value,end=" ")
        print()
n=int(input("Enter Number of rows : "))
pascal(n)

'''
Output:

Enter Number of rows : 5
     1 
    1 1 
   1 2 1 
  1 3 3 1 
 1 4 6 4 1 

'''