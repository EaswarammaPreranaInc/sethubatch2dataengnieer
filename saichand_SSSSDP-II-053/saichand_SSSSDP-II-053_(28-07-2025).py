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

sample output:
Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)
'''

# program
x=complex(input("Enter first complex number :" ))
y=complex(input("Enter second complex number :" ))
print('Sum :', x + y)
print('Difference :', x - y)
print('Product :', x * y)
print('Division :', x / y)





# Identify  error
else:					# without if we cannot use else
	print('else  suite')
print('Outside')




# Identify  error
if  9 > 5				# : is missing
	print('Hello')
print('Bye')




# Identify  error
if  9 > 12:
	print('Hyd')
else					# : is missing in else block
	print('Sec')




# Identify  error
if  (10,20,15):
print('Hyd')				# indentation error
else:
print('Sec')				# indentation error




# Identify  error
if  ():
			print('Hyd')
	else:							# indentation error
					print('Sec')
print('Bye')





# Identify  error
if  { }:			# error
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





# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:					# indentation error
if  []:
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:					# indentation error
	print('Seven')
	print('Eight')
	print('Nine')
else:					# indentation error
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')





# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

# program
a=int(input("Enter a number:"))
if a % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")




# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')		# One
        print('Two')		# Two
        print('Three')		# Three
print('Bye')			# Bye





# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')		# Hyd
        print('Sec')		# Sec
        print('Cyb')		# Cyb
print('Bye')			# Bye





# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')			# Bye





# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
sample outputs:
Enter month number (1 - 12): 6
June

Enter month number (1 - 12): 13
Input  should  be  between  1  and   12

Enter month number (1 - 12): 10.8
Input  should  be  an  integer

# program
try:
    m=int(input("Enter month number (1 - 12):"))
    if m==1:
        print("January")
    elif m==2:
        print("Feburvary")
    elif m==3:
        print("March")
    elif m==4:
        print("April")
    elif m==5:
        print("May")
    elif m==6:
        print("June")
    elif m==7:
        print("July")
    elif m==8:
        print("August")
    elif m==9:
        print("September")
    elif m==10:
        print("Octomber")
    elif m==11:
        print("November")
    elif m==12:
        print("December")
    else:
        print("Input  should  be  between  1  and   12")
except:
    print("Input  should  be  an  integer")




'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

# program
# program
n=int(input("Enter a number :"))
if n==0:
    print("Zero")
else:
    if n==1:
        print("One")
    else:
        if n==2:
            print("Two")
        else:
            if n==3:
                print("Three")
            else:
                if n==4:
                    print("Four")
                else:
                    if n==5:
                        print("Five")
                    else:
                        if n==6:
                            print("Six")
                        else:
                            if n==7:
                                print("Seven")
                            else:
                                if n==8:
                                    print("Eight")
                                else:
                                    if n==9:
                                        print("Nine")
                                    else:
                                        print("Invalid")