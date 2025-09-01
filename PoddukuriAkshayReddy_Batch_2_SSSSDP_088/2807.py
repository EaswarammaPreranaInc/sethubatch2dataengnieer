


Poddukuri Akshay Reddy
2807

'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j


What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                         =   (15 - 18j + 20j + 24) / (25 + 36)
								      = 39 / 61 +2j / 61		   
'''
# Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)

num1 = complex(3, 4)  # 3 + 4j
num2 = complex(5, 6)  # 5 + 6j

sum_result = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)



# Identify  error
else:
		print('else  suite')
print('Outside')  
# if is not defined 



# Identify  error
if  9 > 5
	print('Hello')
print('Bye')
# if doesnot have ":" 



# Identify  error
if  9 > 12:
	print('Hyd')
else
	print('Sec')
# else doesnot have ":" 


# Identify  error
if  (10,20,15):
print('Hyd')
else:
print('Sec')
# indentation error first print should have space or tab at the begining 



# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')   
# else is not indented properly



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
# flower brackets are not used in python


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
#  indentation error else if are not indented



# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

x =int(input("Enter a number:"))
y = Even if x % 2 ==0 else Odd
print(y)

# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')

#One
#Two
#Three

# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
# Hyd
Sec
Cyb
Bye


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
# Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)


Enter month number (1 - 12): 6
June

Enter month number (1 - 12): 13
Input  should  be  between  1  and   12

Enter month number (1 - 12): 10.8
Input  should  be  an  integer



user_input = input("Enter month number (1 - 12): ")


if not user_input.isdigit():
    print("Input should be an integer")
else:
    month_num = int(user_input)
    
    if month_num == 1:
        print("January")
    elif month_num == 2:
        print("February")
    elif month_num == 3:
        print("March")
    elif month_num == 4:
        print("April")
    elif month_num == 5:
        print("May")
    elif month_num == 6:
        print("June")
    elif month_num == 7:
        print("July")
    elif month_num == 8:
        print("August")
    elif month_num == 9:
        print("September")
    elif month_num == 10:
        print("October")
    elif month_num == 11:
        print("November")
    elif month_num == 12:
        print("December")
    else:
        print("Input should be between 1 and 12")


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''
user_input = input("Enter a digit (0 - 9): ")

if user_input.isdigit() and len(user_input) == 1:
    digit = int(user_input)

    if digit == 0:
        print("Zero")
    else:
        if digit == 1:
            print("One")
        else:
            if digit == 2:
                print("Two")
            else:
                if digit == 3:
                    print("Three")
                else:
                    if digit == 4:
                        print("Four")
                    else:
                        if digit == 5:
                            print("Five")
                        else:
                            if digit == 6:
                                print("Six")
                            else:
                                if digit == 7:
                                    print("Seven")
                                else:
                                    if digit == 8:
                                        print("Eight")
                                    else:
                                        if digit == 9:
                                            print("Nine")
else:
    print("Invalid")

