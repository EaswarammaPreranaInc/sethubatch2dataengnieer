#1.  Write a program to add, sub, mul, div two complex numbers
x = eval(input("Enter first complex number :"))
y = eval(input("Enter second complex number :"))
print('Sum :', x + y)
print('Difference :', x - y)
print('Product :', x * y)
print('Division :', x / y)


#2. Identify  error
else:
		print('else  suite')
print('Outside')
# There is if condition to use else and indentation error
[
	
#3. Identify  error
if  9 > 5 # There is no colon at end of the statement
	print('Hello')
print('Bye')



#4. Identify  error
if  9 > 12:
	print('Hyd')
else # Error due to colon at end
	print('Sec')



#5. Identify  error
if  (10,20,15):
print('Hyd') # Indentation error
else:
print('Sec') # Indentation error



#6. Identify  error
if  ():
			print('Hyd')
	else: # else should be in same vertical line
					print('Sec')
print('Bye')


#7. Identify  error
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
# Error due to curly braces


#8. Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []: # indentation error and error due to []
	print('Four')
	print('Five')
	print('Six')
else:
if  {}:  # indentation error and error due to {}
	print('Seven')
	print('Eight')
	print('Nine')
else:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')



#9.write a program to find even or odd number
a = int(input("Enter a number :"))
if(a%2==0):
    print("Even number "  )
else:
     print("Odd number "  )


#10. Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One') # One
        print('Two') # Two
        print('Three') # Three
print('Bye') # Bye



#11. Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd') # Hyd
        print('Sec') # Sec
        print('Cyb') # Cyd
print('Bye') # Bye



#12. write a program to print month name
a = int(input("Enter a number :"))
if(a==1):
    print("Jan")
elif(a==2):
    print("Feb")
elif(a==3):
    print("Mar")
elif(a==4):
    print("Apr")
elif(a==5):
    print("May")
elif(a==6):
    print("Jun")
elif(a==7):
    print("Jul")
elif(a==8):
    print("Aug")
elif(a==9):
    print("sep")
elif(a==10):
    print("Oct")
elif(a==11):
    print("Nov")
elif(a==12):
    print("Dec")
else:
    print("Input should be between  1  and  12 and an integer")



#13. write a program to print digit in words
a = int(input("Enter a number :"))
if(a==0):
    print("Zero")
if(a==1):
    print("One")
if(a==2):
    print("Two")
if(a==3):
    print("Three")
if(a==4):
    print("Four")
if(a==5):
    print("Five")
if(a==6):
    print("Six")
if(a==7):
    print("Seven")
if(a==8):
    print("Eight")
if(a==9):
    print("Nine")
if(a>9):
    print("input should be between 0 to 9")