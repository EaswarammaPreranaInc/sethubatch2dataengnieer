


'''
Write  a  program  to   add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j
What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                         =   (15 - 18j + 20j + 24) / (25 + 36)																		 = 39 / 61 + 2j / 61											   
'''
a=complex(input("Enter the 1st complex number : "))
b=complex(input("Enter the 2nd complex number : "))
s=a+b
diff=a-b
p=a*b
d=a/b
print(f'sum : {s}')
print(f'difference : {diff}')
print(f'product : {p}')
print(f'division : {d}')




# Identify  error
else:
		print('else  suite')
print('Outside') 

#there is no if suite in the indentation with else suite




# Identify  error
if  9 > 5
	print('Hello')
print('Bye')

# there is no colon after condition syntax error




# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')
	
# thereisno colon after else SyntaxError




# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
# Indentation error there should be indentation to the statements inside the suite




# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')

# indentation error the else needs to be at same indentation as the if






# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')

# flower braces are not allowed for the suite in python {} are for dict and set objects





# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

# after else if needs to be indented





# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
n=int(input("Enter the number : "))
res='odd number' if n%2 else 'even number'
print(res)





# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One') # One
        print('Two') # Two
        print('Three') # Three
print('Bye') # Bye




# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') # Hyd
        print('Sec') # sec
        print('Cyb') # Cyb
print('Bye') # Bye




# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif 
import calendar
try:
    n=int(input("Enter Month number: "))
    if(n>12 or n<1):
        print("Please! enter valid number 1-12")
    else:
        print(calendar.month_name[n])
except ValueError:
    print("Input should be an integer")





# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif 

try:
    n=int(input("Enter the number: "))
    if(n>12 or n<1):
        print("Please! enter valid number 1-12")
    elif(n==1):
        print("January")
    elif(n==2):
        print("February")
    elif(n==3):
        print("March")
    elif(n==4):
        print("April")
    elif(n==5):
        print("May")
    elif(n==6):
        print("June")
    elif(n==7):
        print("July")
    elif(n==8):
        print("August")
    elif(n==9):
        print("September")
    elif(n==10):
        print("October")
    elif(n==11):
        print("November")
    else:
        print("December")
except ValueError:
    print("Input should be an Integer")





'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
try:
    n=int(input("Enter digit number : "))
    if(n<0 or n>9):
        print(f'{n} - Invalid')
    else:
        if(n==0):
            print(f'{n} - Zero')
        else:
            if(n==1):
                print(f'{n} - One')
            else:
                if(n==2):
                    print(f'{n} -Two')
                else:
                    if(n==3):
                        print(f'{n} - Three')
                    else:
                        if(n==4):
                            print(f'{n} - Four')
                        else:
                            if(n==5):
                                print(f'{n} - Five')
                            else:
                                if(n==6):
                                    print(f'{n} - Six')
                                else:
                                    if(n==7):
                                        print(f'{n} - Seven')
                                    else:
                                        if(n==8):
                                            print(f'{n} - Eight')
                                        else:
                                            if(n==9):
                                                print(f'{n} - Nine')
except ValueError:
    print("Input should be an integer")