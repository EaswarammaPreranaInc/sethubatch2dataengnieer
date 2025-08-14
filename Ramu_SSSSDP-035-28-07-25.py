#Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
try:
    n=int(input("Enter Any Integer  between (0 - 9) :"))
    if(n==0):
        print(n,"- Zero")
    else:
      if n==1:
        print(n,"- One")
      if n==2:
        print(n,"- Two")
      if n==3:
        print(n,"- Three")
      if n==4:
        print(n,"- Four")
      if n==5:
        print(n,"- Five")
      if n==6:
        print(n,"- Six")
      if n==7:
        print(n,"- Seven")
      if n==8:
        print(n,"- Eight")
      if n==9:
        print(n,"- Nine")
      if n>9:
        print("Invalid")
except ValueError:
    print("Intput value must be Integer ")


Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j

What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                      =   (15 - 18j + 20j + 24) / (25 + 36)= 39 / 61 + 2j / 61											   

 Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)
n=complex(input("Enter first complex number: "))
m=complex(input("Enter second complex number: "))
print("Sum : ", n + m)
print("Difference : ", n - m)
print("Product: ", n * m)
print("Division : ", n / m)
# Identify  error
else:   #without if  we can't write else
		print('else  suite')
print('Outside')
# Identify  error
if  9 > 5   #IndentationError
	print('Hello') #Hello
print('Bye')  #Bye
 # Identify  error
if  9 > 12:
	print('Hyd')
else     #IndentationError
	print('Sec') 
 # Identify  error
if  (10,20,15): # IndentationError 
print('Hyd') 
else:
print('Sec')
 # Identify  error
if  ():
			print('Hyd')
	else: #indentation Error
					print('Sec') 
print('Bye')
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
print('Bye') #Bye
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:  # IndentationError
	print('Four')
	print('Five')
	print('Six')
else:  # IndentationError
if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
else:  # IndentationError
	print('Hyd') 
	print('Sec') 
	print('Cyb') 
print('Bye') 
# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
n=int(input("Enter the Integer Number")
if n%2==0:
    print("Even)
else:
    print("Odd")
    
 # Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One') #One
        print('Two') #Two
        print('Three') #Three
print('Bye') #Bye
 # Find  outputs  (Home  work)
 if{10 : 20 , 30 : 40}:
        print('Hyd') #Hyd
        print('Sec')#Sec
        print('Cyb')#Cyb
       print('Bye') #Bye
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye') #Bye
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
 Enter month number (1 - 12): 6
June
 Enter month number (1 - 12): 13
Input  should  be  between  1  and   12
 Enter month number (1 - 12): 10.8
Input  should  be  an  integer'''
try:
  n=int(input("Enter month number(1 - 12) : "))
  
  if n==1:
    print("January")
  elif n==2:
    print("Febuarary")
  elif n==3:
    print("March")
  elif n==4:
    print("April")
  elif n==5:
    print("May")
  elif n==6:
    print("June")
  elif n==7:
    print("July")
  elif n==8:
    print("August")
  elif n==9:
    print("September")
  elif n==10:
    print("October")
  elif n==11:
    print("November")
  elif n==12:
    print("December")
  else:
    print("Input  should  be  between  1  and   12")
except ValueError:
  print("Input should be Integer")
