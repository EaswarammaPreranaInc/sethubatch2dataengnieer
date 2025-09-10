prgm-1

x=eval(input("Enter 1st complex value: " ))
y=eval(input("Enter 2nd complex value: " ))
print(F'{x}+{y}={x+y}')
print(F'{x}-{y}={x-y}')
print(F'{x}*{y}={x*y}')
print(F'{x}/{y}={x/y}')


questions with errors
Q1
else:
		print('else  suite')
print('Outside')	# there is else statement without if

Q2
if  9 > 5
	print('Hello')
print('Bye')	# there must be : after the if condition


if  9 > 12:
	print('Hyd')
else
	print('Sec') # for else condition : is mandatory

Q3
if  (10,20,15):
print('Hyd') # indentation like space or tab key is mandatory after :
else:
print('Sec') # indentation like space or tab key is mandatory after :

Q4
if  ():
			print('Hyd')
	else:						# else should be indented with if i.e if and else should be in same column
					print('Sec')
print('Bye') 

Q5
if  { }:
{
	print('One')
	print('Two')
	print('Three')		# the statements after if condition are suite suite should not be {}
}
else:
{
	print('Four')
	print('Five')
	print('Six')
}				# the statements after else condition are suite suite should not be {}

print('Bye')

Q6
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:			# here if should be indented with space or tab key
	print('Four')
	print('Five')
	print('Six')
else:			# this else should be with second if as 1st if already has else
if  {}:			# if condition should be indented
	print('Seven')
	print('Eight')
	print('Nine')
else:			# indentation
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement

n=float(input('Enter a number: '))
if (n%2==0):
    print('Given number is even number')
else:
    print('Given number is odd number')


# Find outputs  (Home  work)
if():				# empty tuple so false if suite is skipped 
        print('Hyd')
        print('Sec')
        print('Cyb')
else:				# as the condition is false else suite is executes=d
        print('One')		# one is printed and goes to next line
        print('Two')		# two is printed and next line
        print('Three') 		# three is printed and next line
print('Bye')			# bye is printed irrespective of condition


if{10 : 20 , 30 : 40}:		# non empty dictionary so true
        print('Hyd')		# hyd is printed and goes to next line
        print('Sec')		# sec is printed and goes to next line
        print('Cyb')		# cyb is printed and goes to next line
print('Bye')			# bye is printed irrespective of condition


if { }:				# empty dictionary so false
	print('Hyd')
	print('Sec')
	print('Cyb')		# but we don't have else suite to run so
print('Bye')			# bye is only printed


# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

try:
    n=int(input('Enter month number(1-12): '))
    if (n==1):
        print('january')
    elif (n==2):
        print('february')
    elif (n==3):
        print('march')
    elif (n==4):
        print('april')
    elif (n==5):
        print('may')
    elif (n==6):
        print('june')
    elif (n==7):
        print('july')
    elif (n==8):
        print('august')
    elif (n==9):
        print('september')
    elif (n==10):
        print('october')
    elif (n==11):
        print('november')
    elif (n==12):
        print('december')
    else:
        print('Input  should  be  between 1 and 12')
except:
    print('Input  should  be an integer')


#Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)


n=int(input('Enter  number: '))
if (n==0):
    print('Zero')
else:
    if (n==1):    
        print('one')
    else:
        if (n==2):
            print('two')
        else:
            if (n==3):
                print('three')
            else:
                if (n==4):
                    print('four')
                else:
                    if (n==5):
                        print('five')
                    else:
                        if (n==6):
                            print('six')
                        else:
                            if (n==7):
                                print('seven')
                            else:
                                if (n==8):
                                    print('eight')
                                else:
                                    if (n==9):
                                        print('nine')
                                    else:
                                        if (n==10):
                                            print('invalid')
                                        else:
                                            print('enter a valid digit')
    

