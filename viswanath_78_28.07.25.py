#Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers
try:
    a = eval(input('Enter the first input : ')) #3+4j
    b = eval(input('Enter the second input : ')) #5+7J
    print(f'{a}+{b} = {a+b}') # (3+4j)+(5+7j) = (8+11j)
    print(f'{a}-{b} = {a-b}') # (3+4j)-(5+7j) = (-2-3j)
    print(f'{a}*{b} = {a*b}') # (3+4j)*(5+7j) = (-13+41j)
    print(f'{a}/{b} = {a/b:.2f}') # (3+4j)/(5+7j) = 0.58-0.01j
except TypeError:
    print('different sequences are not allowed')
except NameError:
    print('str must be in quotes')

else:                     # Error: 'else' cannot be used without a  'if' block before it
print('else  suite')
print('Outside')

if  9 > 5		  # Error: expected ':' after if statement
	print('Hello')         
print('Bye')

if  9 > 12:
	print('Hyd')
else			# Error: expected ':' after else
	print('Sec')           

if  (10,20,15):
print('Hyd')
else:
print('Sec') # Error: expected an indented block after 'if' and 'else'

if  (): 
			print('Hyd')
	else:
					print('Sec')
print('Bye') # Error: IndentationError: unexpected indent in ‘if” and else' block

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
print('Bye') # Error: SyntaxError: invalid syntax due to use of curly braces {} instead of colons and indentation

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
print('Bye') # Error: SyntaxError: expected ':' after else and if; also improper indentation and nesting without elif

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
try:
    a = float(input('Enter the input : ')) #10, 51.0
    if a%2 ==0:
        print( f'{a}', “is even number") # 10.0 is even number
    else:
        print((f'{a}',' is odd number') # 51.0  is odd number
except ValueError:
    print('str values,complex numbers and sequences are not allowed')

if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
Output: # One
# Two
# Three
# Bye

if {10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
 Output: # Hyd
# Sec
# Cyb
# Bye


if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
Output:  # Bye

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif
try:
    a = int(input('Enter the input : ')) #10
    if a == 1:
        print(f'{a} = January')
    elif a == 2:
        print(f'{a} = February')
    elif a == 3:
        print(f'{a} = March')
    elif a == 4:
        print(f'{a} = April')
    elif a == 5:
        print(f'{a} = May')
    elif a == 6:
        print(f'{a} = June')
    elif a == 7:
        print(f'{a} = July')
    elif a == 8:
        print(f'{a} = August')
    elif a == 9:
        print(f'{a} = September')
    elif a == 10:
        print(f'{a} = October') #10 = October
    elif a == 11:
        print(f'{a} = November')
    elif a == 12:
        print(f'{a} = December')
    else: 
        print('Invalid Input. Input must be between 1-12 of type int')
except ValueError:
    print('Invalid Input – Only numbers from 1 to 12 are allowed')
    
#Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
try:
    a = int(input('Enter the input : ')) #5
    if a==0 :
        print(f'{a} = Zero' )
    if a==1 :
        print(f'{a}  = One')
    if a==2 :
        print(f'{a} = Two')
    if a==3 :
        print(f'{a} = Three')
    if a==4 :
        print(f'{a} = Four')
    if a==5 :
        print(f'{a} = Five') # 5 = Five
    if a==6 :
        print(f'{a} = Six')
    if a==7 :
        print(f'{a} = Seven')
    if a==8 :
        print(f'{a} = Eight')
    if a==9 :
        print(f'{a} = Nine')
    if a not in range(10):
        print('Invalid Input. Input must be between 0-9 of type int ')
    except ValueError:
        print('Invalid Input – Only numbers from 0-9 are allowed')
(or)

a = int(input("Enter the number = ")) 
if a==0:
    print(f'{a}', '= Zero')
else:    
    if a==1:
         print(f'{a}', '= One')
    else :    
        if a==2:
             print(f'{a}', '= Two')
        else:
            if a==3:     
                print(f'{a}', '= Three')    
            else:
                if a==4:    
                     print(f'{a}', '= Four')
                else: 
                    if a==5:
                        print(f'{a}', '= Five')
                    else:
                        if a==6:
                            print(f'{a}', '= Six')   
                        else:
                            if a==7:
                                print(f'{a}', '= Seven')
                            else:
                                if a==8:
                                     print(f'{a}', '= Eight')
                                else:
                                    if a==9:
                                        print(f'{a}', '= Nine')
                                    else: 
                                        print(f'{a}', 'is Invalid input. Enter a value btwn 0-9')
     
     
