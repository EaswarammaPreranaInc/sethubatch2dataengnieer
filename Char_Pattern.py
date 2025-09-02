'''
Write a  program to print following pyramid
Input: 5

             A
            A B
           A B C
          A B C D
         A B C D E


	   i         ch
---------------------
       1         'A'

	   2         'A'  to  'B'

	   3         'A'  to  'C'

	   4         'A'  to  'D'

	   5         'A'  to  'E'
'''

n = int(input("Enter Number of lines : "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")  
    print()


'''
Output:

Enter Number of lines : 7
      A 
     A B
    A B C
   A B C D
  A B C D E
 A B C D E F
A B C D E F G

'''
