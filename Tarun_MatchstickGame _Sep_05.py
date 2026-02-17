#Question:
'''
There  are  21  matchsticks.
User  can  pick  1 , 2 , 3  or  4  matchsticks.
Computer  picks  after  user  and  whoever  picks  the  last  matchstick, they  lose  the  game.
Write  a  program  such  that  computer  wins

Logic:  Total  should  be  5

Hint: Use while  loop

						n = 21
   Iteration     user         computer             n
-------------------------------------------------------------
         1               2                 3               n = 21 - 5 = 16

		 2              3                 2               n = 16 - 5 = 11

		 3              1                 4               n = 11 - 5 = 6

		 4              4                 1               n =6 - 5 = 1
---------------------------------------------------------------
'''
#Answer:
n = 21
print("Total matchsticks:", n)
print("Rules: You can pick 1, 2, 3, or 4 matchsticks. Whoever picks the last one loses.")

while n > 0:
    # User's turn
    while True:
        try:
            user_pick = int(input("\nYour turn! Pick 1, 2, 3, or 4 matchsticks: "))
            if user_pick in [1, 2, 3, 4] and user_pick <= n:
                break
            else:
                print("Invalid input! Please pick between 1 and 4 and don't exceed remaining matchsticks.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    
    n -= user_pick
    print(f"You picked {user_pick}. Remaining matchsticks: {n}")
    
    if n == 0:
        print("\nYou picked the last matchstick. You lose! Computer wins.")
        break
    
    # Computer's turn
    # Computer's strategy: Always pick (5 - user_pick) to maintain the 5-matchstick cycle
    comp_pick = 5 - user_pick
    # If remaining matchsticks are less than comp_pick, adjust
    if comp_pick > n:
        comp_pick = n  # Computer picks all remaining, but this should not happen in optimal play
    
    n -= comp_pick
    print(f"Computer picks {comp_pick}. Remaining matchsticks: {n}")
    
    if n == 0:
        print("\nComputer picked the last matchstick. You win!")
        break
