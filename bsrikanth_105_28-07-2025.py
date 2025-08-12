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
Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)

Program:
c1 = complex(input("Enter first complex number: "))   # e.g., 3+4j
c2 = complex(input("Enter second complex number: "))  # e.g., 5+6j

# Perform operations
sum_result = c1 + c2
diff_result = c1 - c2
product_result = c1 * c2
division_result = c1 / c2

# Display results
print("Sum:", sum_result)
print("Difference:", diff_result)
print("Product:", product_result)
print("Division:", division_result)



# Identify  error
else:
		print('else  suite')
print('Outside')				#else cannot be used alone without if statement.
# Identify  error
if  9 > 5
	print('Hello')				
print('Bye')					#SyntaxError:semicolon is mandatory after if condition
# Identify  error
if  9 > 12:
	print('Hyd')
else						#SyntaxError:semicolon is mandatory after else condition
	print('Sec')
# Identify  error
if  (10,20,15):
print('Hyd')
else:						#Indentation Error
print('Sec')
# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')	#Indentation error
print('Bye')
# Identify  error
if  { }:
{
	print('One')
	print('Two')
	print('Three')
}
else:						#{} is used for dictonary 
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
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

Program:
a=int(input())
if a%2==0:
	print('Even Number')
else:
	print('Odd Number')



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

Output:
One
Two
Three
Bye


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
Output:
Hyd
Sec
Cyb
Bye


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

Output:
Bye


 # Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
Enter month number (1 - 12): 6
June
Enter month number (1 - 12): 13
Input  should  be  between  1  and   12
Enter month number (1 - 12): 10.8
Input  should  be  an  integer
'''
output:
month=int(input())
if n>0 and n<=12:
    if month == 1:
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("October")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")

else:
    print("Enter a valid number and month between 1-12")    

Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid

Program:
digit=int(input('Enter digit between 0-9:')
if digit>=0 and digit<=9:
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
else:
    print("Invalid")


