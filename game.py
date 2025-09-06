'''
There  are  21  matchsticks.
User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins

Logic:  Total  should  be  5

Hint: Use while  loop

						n = 21
   Iteration     user         computer                 n
-------------------------------------------------------------
         1         2              3               n = 21 - 5 = 16

		 2         3              2               n = 16 - 5 = 11

		 3         1              4               n = 11 - 5 = 6

		 4         4              1               n =6 - 5 = 1
---------------------------------------------------------------
'''

def pick():
    while True:
        try:
            u = int(input())
            if 1 <= u <= 4:
                return u
            else:
                print("Input can not be > 4 nor < 1, Reenter : ", end="")
        except ValueError:
            print("Invalid input, Reenter : ", end="")
n = int(input("Enter total number of matchsticks: "))
while n > 1:
    print("How many matchsticks would you like to pick (1 , 2 , 3 or 4) ? : ", end="")
    user = pick()
    n -= user
    comp = min(5 - user, n - 1)
    print(f"Computer picks {comp} matchsticks")
    n -= comp

print("You have lost the game and Computer wins")

'''
Output:

How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  3
Computer  picks  2 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  0
Input  can  not  be >  4  nor  <  1,  Reenter  :  1
Computer  picks  4 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  2
Computer  picks  3 matchsticks
How  many  matchsticks  would  you  like  to  pick (1 , 2 ,  3 or  4) ?  :  5
Input  can  not  be >  4  nor  <  1,  Reenter  :  6
Input  can  not  be >  4  nor  <  1,  Reenter  :  7
Input  can  not  be >  4  nor  <  1,  Reenter  :  8
Input  can  not  be >  4  nor  <  1,  Reenter  :  4
Computer  picks  1 matchsticks
You  have  lost  the  game  and Computer wins
'''
