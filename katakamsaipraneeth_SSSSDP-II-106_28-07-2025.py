'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j


What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                         =   (15 - 18j + 20j + 24) / (25 + 36)
																		 = 39 / 61 + 2j / 61											   
'''
############ program###############
a = eval(input("Enter first complex number :"))
b = eval(input("Enter second complex number:"))
print(F'Sum : {a+b}')
print(F'Difference : {a-b}')
print(F'Product : {a*b}')
print(F'Division : {a/b}')

########### output ############
Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)

# Identify  error
else: # There is no if condition so, else wont execute .Hence --error
		print('else  suite')
print('Outside') # always executes 

# Identify  error
if  9 > 5 # No colen ':' at end of if condition -- syntax error
	print('Hello')
print('Bye') # always executes

# Identify  error
if  9 > 12:
	print('Hyd')
else # no colen -- error
	print('Sec')

# Identify  error
if  (10,20,15):
print('Hyd') # there is no indendation at print stat
else:
print('Sec') # no indendation after else statement

# Identify  error
if  ():
			print('Hyd')
	else:  # if and else should be in same column otherwise error
					print('Sec')
print('Bye')

# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
} # if condition suit cannot be in set and even in else block 
else: 
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye') # always executes

# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []: # if condition should be under else block
	print('Four')
	print('Five')
	print('Six')
else:
if  {}: # if has no indendation 
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # always exectes

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
######## program ###########
a = int(input("Enter a integer number :"))
if a % 2 == 0:
	print("Even")
else:
	print("Odd")

# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye') # One  Two  Three  Bye

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye') # Hyd  Sec  Cyd  Bye


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') # Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
######## program #############
try:
    a = int(input("Enter month number (1 - 12):"))
    if a==1:
        print("January")
    elif a==2:
        print("February")
    elif a==3:
        print("March")
    elif a==4:
        print("April")
    elif a==5:
        print("May")
    elif a==6:
        print("June")
    elif a==7:
        print("July")
    elif a==8:
        print("August")
    elif a==9:
        print("September")
    elif a==10:
        print("October")
    elif a==11:
        print("November")
    elif a==12:
        print("December")
    else:
        print("Input should be between 1 and 12")
except ValueError:
    print("Input  should  be  an  integer")

######### output ##########
Enter month number (1 - 12): 6
June
Enter month number (1 - 12): 13
Input  should  be  between  1  and   12
Enter month number (1 - 12): 10.8
Input  should  be  an  integer

'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
####### program ##########
a = int(input("enter a single digit 0-9 :"))
if a == 0:
    print('0 - Zero')
else:
    if a == 1:
        print('1 - One')
    else:
        if a == 2:
            print('2 - Two')
        else:
            if a == 3:
                print('3 - Three')
            else:
                if a == 4:
                    print('4 - Four')
                else:
                    if a == 5:
                        print('5 - Five')
                    else:
                        if a == 6:
                            print('6 - Six')
                        else:
                            if a == 7:
                                print('7 - Seven')
                            else:
                                if a == 8:
                                    print('8 - Eight')
                                else:
                                    if a == 9:
                                        print('9 - Nine')
                                    else:
                                        print('Invalid')