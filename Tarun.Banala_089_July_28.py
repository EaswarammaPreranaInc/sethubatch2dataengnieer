#Name: *Tarun Banala*   28-07-2025

'''Write  a  program  to  add ,  subtract , multiply  
and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j


What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                         =   (15 - 18j + 20j + 24) / (25 + 36)
																		 = 39 / 61 + 2j / 61	'''									   

m=eval(input("Enter first complex number :"))
n=eval(input("Enter second complex number :"))
print("Sum :", m+n)
print("Difference :", m-n)
print("Product :", m*n)
print("Division :", m/n)

# Identify  error   
else:
		print('else  suite')
print('Outside')    # error is without if condition and indentation error

# Identify  error
if  9 > 5
	print('Hello')
print('Bye')     # colon  is missing

# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec') #  colon is missing at else condition
	
# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')  # indentation error

# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')  # indentation error at else 


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
print('Bye')   # {} error

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
print('Bye')  # if  []: error at 

m=int(input("enter number:"))
if (m%2==0):
    print("even number")
else:
    print("odd number")
	
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')    # One <nxt line> Two <nxt line> Three <nxt line> Bye

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye') # Hyd <nxt line> Sec <nxt line> Cyb <nxt line> Bye

if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') #Bye

try:
    n = int(input("Enter month number (1–12): "))
    if n == 1:
        print("January")
    elif n == 2:
        print("February")
    elif n == 3:
        print("March")
    elif n == 4:
        print("April")
    elif n == 5:
        print("May")
    elif n == 6:
        print("June")
    elif n == 7:
        print("July")
    elif n == 8:
        print("August")
    elif n == 9:
        print("September")
    elif n == 10:
        print("October")
    elif n == 11:
        print("November")
    elif n == 12:
        print("December")
    else:
        print("Out of range! Enter between 1 to 12 only.")
except:
    print("please provide int number only")
    
n = int(input("Enter a digit (0–9): "))
if n == 0:
    print("Zero")
elif n == 1:
    print("One")
elif n == 2:
    print("Two")
elif n == 3:
    print("Three")
elif n == 4:
    print("Four")
elif n == 5:
    print("Five")
elif n == 6:
    print("Six")
elif n == 7:
    print("Seven")
elif n == 8:
    print("Eight")
elif n == 9:
    print("Nine")
else:
    print("Invalid digit! Enter from 0 to 9.")
