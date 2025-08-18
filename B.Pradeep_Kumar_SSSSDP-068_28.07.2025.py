# Identify  error
else:
		print('else  suite') # Indentation Error
print('Outside')  #  Indentation Error


# Identify  error
if  9 > 5    #  ':'  missed in this line
	print('Hello')
print('Bye')


# Identify  error
if  9 > 12:
	print('Hyd')
else  #  In else statement ':' has missed
	print('Sec')


# Identify  error
if  (10,20,15):
print('Hyd')  #   Indentation Error
else:
print('Sec')  #   Indentation Error



# Identify  error
if  ():
			print('Hyd')
	else:  #  Error due to if,else statements should in same indent
					print('Sec')
print('Bye')


# Identify  error
if  { }:
{    #  indentation Error
	print('One')
	print('Two')
	print('Three')
}
else:
{   #   Indentation Error
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
else:
if  []:   #   Indentation Error
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:    #   Indentation Error
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

try:
    num = int(input(" Enter a Number : "))
    if num%2==0:
              print(f" {num} is even")
    else:
        print(f" {num} is odd")
except:
    print(" Enter integers only")


# Find outputs  (Home  work)
if():
        print('Hyd')  
        print('Sec')
        print('Cyb')
else:
        print('One')  #  one
        print('Two')  #  Two
        print('Three') #  Three
print('Bye')  # Bye


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')  #  Hyd
        print('Sec')  #  Sec
        print('Cyb')  #  Cyb
print('Bye')  #  Bye

# Find outputs  (Home  work)
if { }:
	print('Hyd')  #  Hyd
	print('Sec')  #  Sec
	print('Cyb')  #  Cyb
print('Bye')  #  Bye



# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)


try:
    num = int(input(" Enter month Number(1-12): "))
    if num==1:
        print("January")
    elif num==2:
        print("Febraury") 
    elif num==3:
        print("March")
    elif num==4:
        print("April")
    elif num==5:
        print("May")
    elif num==6:
        print("June")
    elif num==7:
        print("July")
    elif num==8:
        print("August")
    elif num==9:
        print("September")
    elif num==10:
        print("October")
    elif num==11:
        print("November")
    elif num==12:
        print("December")
    else:
        print("input should be between 1 and 12")
except:
    print("Input Should be an integer")



'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
num = int(input(" Enter a Number(0-9): "))

if num==0:
    print("Zero")
if num==1:
    print("One")
if num==2:
    print("Two")
if num==3:
    print("Three")
if num==4:
    print("Four")
if num==5:
    print("Five")
if num==6:
    print("Six")
if num==7:
    print("Seven")
if num==8:
    print("Eight")
if num==9:
    print("Nine")
else:
    print("Invalid")
 
