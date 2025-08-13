#1st
a=complex(input("Enter first complex number: "))
b=complex(input("Enter second complex number: "))
print(f'Sum :{a+b}')
print(f'Difference :{a-b}')
print(f'Product :{a*b}')
print(f'Division :{a/b}')

#2nd
# Identify  error
#else:
#		print('else  suite')
print('Outside')

#3rd
# Identify  error
#if  9 > 5
	#print('Hello')
print('Bye')

#4th
# Identify  error
if  9 > 12:
	print('Hyd')
#else
	print('Sec')
	
#5th
# Identify  error
if  (10,20,15):
#print('Hyd')
else:
#print('Sec')

#6th
# Identify  error
if  ():
			print('Hyd')
	#else:
				print('Sec')
print('Bye')

#7th
# Identify  error
if  { }:
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


#8th
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
#if  []:
	print('Four')
	print('Five')
	print('Six')
#else:
#if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
#else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')


#9th
a=int(input("Enter any number: "))
if a%2==0:
    print('Even Number')
else:
    print('Odd Number')
	

#10th
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')

#11th
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')

#12th
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')

#13th
try:
    a=int(input("Enter month number(1-12): "))
    if a==1:
        print("January")
    elif a==2:
        print("February")
    elif a==3:
        print("March")
    elif a==4:
        print("April")
    elif a==5:
        print("May")
    elif a==6:
        print("June")
    elif a==7:
        print("July")
    elif a==8:
        print("August")
    elif a==9:
        print("September")
    elif a==10:
        print("October")
    elif a==11:
        print("November")
    elif a==12:
        print("December")
    else:
        print("Input should be in between 1 and 12")
except ValueError:
    print("Input should be an integer")


#14th
try:
    a=int(input('Enter any digit(0-9): '))
    if a==0:
        print("Zero")
    else:
        if a==1:
            print("One")
        else:
            if a==2:
               print("Two")
            else:
                if a==3:
                    print("Three")
                else:
                    if a==4:
                        print("Four")
                    else:
                        if a==5:
                            print("Five")
                        else:
                            if a==6:
                                print("Six")
                            else:
                                if a==7:
                                    print("Seven")
                                else:
                                    if a==8:
                                        print("Eight")
                                    else:
                                        if a==9:
                                           print("Nine")
                                        else:
                                            if a==10:
                                               print("invalid")
except:
      print("input should be a integer number")




