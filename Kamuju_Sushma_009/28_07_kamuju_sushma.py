#Name: Kamuju Sushma
#Home Work-1
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

# Enter first complex number : 3+4j
# Enter second complex number: 5+6j
# Sum :  (8+10j)
# Difference :  (-2-2j)
# Product:  (-9+38j)
# Division :  (0.6393442622950819+0.03278688524590165j)
x=complex(input("Enter first complex number :"))
y=complex(input("Enter second complex number :"))
print(f'Sum : {x+y}')
print(f'Difference : {x-y}')
print(f'Product : {x*y}')
print(f'Division : {x/y}')

#Home Work-2
# Identify  error
# else:
# 		print('else  suite') #else suit cannot be written without if suite
print('Outside')

#Home Work-3
# Identify  error
# if  9 > 5 #':' is missing
	# print('Hello')
print('Bye')

#Home Work-4
# Identify  error
if  9 > 12:
	print('Hyd')
# else #':' is missing here
	# print('Sec')
	
#Home Work-5
# Identify  error
# if  (10,20,15): 
# print('Hyd') #':' appreared in before line so tab space or spaces is necessary
# else:
# print('Sec') #':' appreared in before line so tab space or spaces is necessary

#Home Work-6
# Identify  error
# if  ():
# 			print('Hyd')
# 	else: #else should be indended with 'if'
# 					print('Sec')
# print('Bye')

#Home Work-7
# Identify  error
# if  { }:
# {
# 	print('One')
# 	print('Two')
# 	print('Three')
# }
# else:
# {
# 	print('Four')
# 	print('Five')
# 	print('Six')
# }
# print('Bye')

#suites should not be written in '{ }'

#Home Work-8
# Identify  error
# if  ():
# 	print('One')
# 	print('Two')
# 	print('Three')
# else: # because of ':' it is necessary to give tab or space in the next line 
# if  []:
# 	print('Four')
# 	print('Five')
# 	print('Six')
# else: # because of ':' it is necessary to give tab or space in the next line 
# if  {}:
# 	print('Seven')
# 	print('Eight')
# 	print('Nine')
# else:
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# print('Bye')

#Home Work-9
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
n=int(input("Enter number: "))
if n%2==0:
	print("Even Number")
else:
	print("Odd Number")

#Home Work-10
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
#output, is One <new line> Two <new line> Three <new line> Bye 
#reason, empty tuple is False so else suite will be executed

#Home Work-11
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
#Output, Hyd <nl> Sec <nl> cyb
#Reason, non empty dictioanry is True so if suite will be executed

#Home Work-12
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
# Enter month number (1 - 12): 6
# June

try:
    m=int(input("Enter month number: "))
    if(m==1):
            print("January")
    elif(m==2):
            print("February")
    elif(m==3):
            print("March")
    elif(m==4):
            print("April")
    elif(m==5):
            print("May")
    elif(m==6):
            print("June")
    elif(m==7):
            print("July")
    elif(m==8):
            print("August")
    elif(m==9):
            print("September")
    elif(m==10):
            print("October")
    elif(m==11):
            print("November")
    elif(m==12):
            print("December")
    else:
            print("Input  should  be  between  1  and   12")
except ValueError:
        print("Input  should  be  an  integer")

#Home Work -13
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
n=int(input("Enter number : "))
if(n==0):
        print("Zero")
else:
        if(n==1):
                print("One")
        else:
                if(n==2):
                        print("Two")
                else:
                        if(n==3):
                                print("Three")
                        else:
                                if(n==4):
                                        print("Four")
                                else:
                                        if(n==5):
                                                print("Five")
                                        else:
                                                if(n==6):
                                                        print("Six")
                                                else:
                                                        if(n==7):
                                                                print("Seven")
                                                        else:
                                                                if(n==8):
                                                                        print("Eight")
                                                                else:
                                                                        if(n==9):
                                                                                print("Nine")
                                                                        else:
                                                                                print("Invalid")