#Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

#First  complex  number   --->  3 + 4j
#2nd   complex  number   --->  5 + 6j
#What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
#What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
#What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j
#What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = 0.64+0.03j

try:
    x=eval(input('Enter 1st input: '))	#3+4j
    y=eval(input('Enter 2nd input: '))	#5+6j
    print(f"{x} + {y} = {x+y}")		#8+10j
    print(f"{x} - {y} = {x-y}")		#-2-2j
    print(f"{x} * {y} = {x*y}")		#-9+38j
    print(f"{x} / {y} = {x/y:.2f}")		#0.64+0.03j
except ZeroDivisionError:
    print('Input should be Non-Zero')


							   
# Identify  error
else:
		print('else  suite')
print('Outside') # SyntaxError else cannot be alone in python 


# Identify  error
if  9 > 5       #SyntaxError condition must be end with a colon
	print('Hello')
print('Bye')  


# Identify  error
if  9 > 12:
	print('Hyd')
else                #SyntaxError expected ':' colon 
	print('Sec')


# Identify  error

if  (10,20,15):    
print('Hyd')     # IndentationError Statement must be indeneted after if statement
else:
print('Sec')  

# Identify  error
if  ():
			print('Hyd')
	else:           #else and if must be in same indentation
					print('Sec')
print('Bye')


# Identify  error
if  { }:
{               #SyntaxError python do not use braces to define code blocks
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
else:
if  []:     #IndentationError if block must be indented after the else block
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

try:
    num=int(input('Enter the input: ')) #26
    if num%2==0:
        print(f"{num} is a EvenNumber") #26 is a EvenNumber
    else:
        print(f"{num} is a OddNumber")
except ValueError:
    print('Value must be an integer')
print()


# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:                #Output:- One<nextline>Two<nextline>Three<nextline>Bye
        print('One')
        print('Two')
        print('Three')
print('Bye')


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')        #Hyd<nextline>Sec<nextline>Cyb<nextline>Bye


# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')       #Bye if condition false because of empty dictionary


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)


try:
    month=int(input('Enter month number: ')) #5
    if month==1:
        print('January')
    elif month==2:
        print('February')
    elif month==3:
        print('March')
    elif month==4:
        print('April')
    elif month==5:
        print('May') # May
    elif month==6:
        print('June')
    elif month==7:
        print('July')
    elif month==8:
        print('August')
    elif month==9:
        print('september')
    elif month==10:
        print('Octobar')
    elif month==11:
        print('November')
    elif month==12:
        print('December')
    else:
        print('Input should be between 1 and 12')
except:
    print('Input must be an integer')


#Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
#0 - Zero
#1 - One
#2 - Two
#....
#9 - Nine
#10 - Invalid
try:
    digit=int(input('Enter the input: ')) # 5
    if digit==0:
        print('Zero')
    else:
        if digit==1:
            print('One')
        else:
            if digit==2:
                print('Two')
            else:
                if digit==3:
                    print('Three')
                else:
                    if digit==4:
                        print('Four')
                    else:
                        if digit==5:
                            print('Five') # Five
                        else:
                            if digit==6:
                                print('Six')
                            else:
                                if digit==7:
                                    print('Seven')
                                else:
                                    if digit==8:
                                        print('Eight')
                                    else:
                                        if digit==9:
                                            print('Nine')
                                        else:
                                            print('Value must be in between 1 and 9')
except:
    print('Value must be an integer')

                                OR

try:
    n=int(input('Enter number1: '))
    if n==0 or n==1 or n==2 or n==3 or n==4 or n==5 or n==6 or n==7 or n==8 or n==9:
        if n==0:
            print('zero')
        if n==1:
            print('One')
        if n==2:
            print('Two')
        if n==3:
            print('Three')
        if n==4:
           print('Four')
        if n==5:
            print('Five')
        if n==6:
            print('Six')
        if n==7:
            print('Seven')
        if n==8:
            print('Eight')
        if n==9:
            print('Nine')
    else:
        print('Input must be in between 1 to 9')
except ValueError:
    print('Input must be an integer')
    