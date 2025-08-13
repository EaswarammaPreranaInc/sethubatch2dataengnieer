x=complex(input('enter 1st complex number :'))
y=complex(input('enter 2nd complex number :'))
print('sum: ',x+y)
print('Difference :',x-y)
print('Product :',x*y)
print('Division :',x/y)
print()
# Identify  error
#else:
#print('else  suite')# no if 
print('Outside')
print()
#identify error
#if 9>5 # :  missing after if 
	#print('hello') 
print('Bye')
print()
# Identify  error
if  9 > 12:
	print('Hyd')
#else # : is missing after else
	print('Sec')
	print()
# Identify  error
#if  (10,20,15): # indentation error
#print('Hyd')
#else:
#print('Sec')	
print()
# Identify  error
if  (): # indentation error
			print('Hyd')
	#else: 
					#print('Sec')
print('Bye')
print()
# Identify  error
if  { }: # suite should not be braces
#{
	print('One')
	print('Two')
	print('Three')
#}
else:
#{
	print('Four')
	print('Five')
	print('Six')
#}
print('Bye')
print()
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
#if  []: # indentation issue 
	print('Four')
	print('Five')
	print('Six')
#else:
#if  {}: # indentation error 
	print('Seven')
	print('Eight')
	print('Nine')
#else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
print()
x=int(input('enter a number :'))
if (x%2==0):
    print('x is even number')
else:
    print('x is odd number')
print(0)
print()
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
#one
#two
#three
#Bye	
print()
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
#Hyd
#Sec
#Cyb
#Bye
print()
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
# Bye : empty set
print()

#Program to print month name for input month number using if and elif 
try:
    x=int(input('enter a number(1-12) :'))
    if (x==1):
        print('January')
    elif(x==2):
        print('february')        
    elif(x==3):
        print('march')
    elif(x==4):
        print('april')
    elif(x==5):
        print('may')
    elif(x==6):
        print('june')
    elif(x==7):
        print('july')
    elif(x==8):
        print('august')
    elif(x==9):
        print('september')
    elif(x==10):
        print('october')
    elif(x==11):
        print('november')
    elif(x==12):
        print('december')
    else:
        print('Input should be between 1 and 12')
except:
     print('Input should be integer')	
print()
#program to print digit in words with else and if(do not use elif)
x=int(input('enter a number(0-9): '))
if(x==0):
    print('zero')
else:
    if(x==2):
        print('one')
    else:
        if(x==2):
            print('two')
        else:
            if(x==3):
                print('three')
            else:
                if(x==4):
                    print('four')
                else:
                    if(x==5):
                        print('Five')                        
                    else:
                        if(x==6):
                            print('Six') 
                        else:
                            if(x==7):
                                print('Seven')
                            else:
                                if(x==8):
                                    print('eight') 
                                else:
                                    if(x==9):
                                        print('Nine')
                                    else:
                                        print('invalid')     