giri

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
    month_name = {
        1: "January",2: "February",3: "March",4: "April",
        5: "May",6: "June",7: "July",8: "August",9: "September",
        10: "October",11: "November",12: "December"
    }
    n=int(input("enter month between 1-12:"))
    if n in month_name:
        print(month_name[n])
    else:
        print('out of the month given 1 to 12 only')
except:
    print("please provide int number only")
	

digit_to_word = {
    0: "Zero",1: "One",2: "Two",3: "Three",
    4: "Four",5: "Five",6: "Six",
    7: "Seven",8: "Eight", 9: "Nine"
}
n=int(input("enter a number 0-9:"))
if n in digit_to_word:
    print(digit_to_word[n])
else:
    print("invalid")
