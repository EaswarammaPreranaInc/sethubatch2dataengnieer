try:
    a = complex(input('Enter first complex number:  '))
    b = complex(input('Enter second complex number:  '))
    print(f'Sum: {a+b}')
    print(f'Difference: {a-b}')
    print(f'Product: {a*b}')
    print(f'Division: {a/b:.2f}')
except ValueError:
    print('Please enter only complex number')
except:
    print('Please try again with valid input')


#IF

# Identify  error
# else:
# 		print('else  suite')
# print('Outside')               
#SyntaxError: else cannot be without for and also else statements must be indented


# Identify  error
# if  9 > 5
# 	print('Hello')
# print('Bye')

#there should be a semicolon for the if condition


# Identify  error
if  9 > 12:
	print('Hyd')
# else
# 	print('Sec')
	
#There should be a semicolon for else


# Identify  error
# if  (10,20,15):
# print('Hyd')
# else:
# print('Sec')

#The statements of if and else must be indented with either space or tab key


# Identify  error
# if  ():
# 			print('Hyd')
# 	else:
# 					print('Sec')
# print('Bye')

#else must be indented with the if statement



# Identify  error
# if  { }:
# {
# 	print('One')
# 	print('Two')
# 	print('Three')
# }
# else:
# {
# 	print('Four')
# 	print('Five')
# 	print('Six')
# }
# print('Bye')

#statements of the suite cannot be in {}, in python {} are meant for set, dict


# Identify  error
# if  ():
# 	print('One')
# 	print('Two')
# 	print('Three')
# else:
# if  []:
# 	print('Four')
# 	print('Five')
# 	print('Six')
# else:
# if  {}:
# 	print('Seven')
# 	print('Eight')
# 	print('Nine')
# else:
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# print('Bye')

#all the if statements from line 7 must be indented with space or tab key because of colon on previous line

try:
    a = int(input('Enter a integer number:  '))
    if(a%2==0):
        print('Even Number')
    else:
        print('Odd Number')
except ValueError:
    print('Please enter only integer number')
except:
    print('Please enter a valid input')



# Find outputs  (Home  work)
if():                    #() is empty tuple, means false
        print('Hyd')
        print('Sec')
        print('Cyb')
else:                    #else suite is executed as condition is false
        print('One')     #One
        print('Two')     #Two
        print('Three')   #Three
print('Bye')             #Bye, this is executed irrespective of the condition


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}: #dict is non-empty, so if condition is true
        print('Hyd')   #Hyd
        print('Sec')   #Sec
        print('Cyb')   #Cyb
print('Bye')           #Bye


# Find outputs  (Home  work)
if { }:            #condition is false becoz of empty dict
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')      #Bye



try:
    number = int(input('Enter a number between 1 to 12:  '))
    if number<1 or number >12:
        print('Input should be between 1 and 12')
    elif number==1:
        print('Januaury')
    elif number==2:
        print('Febuaury')
    elif number==3:
        print('March')
    elif number==4:
        print('April')
    elif number==5:
        print('May')
    elif number==7:
        print('June')
    elif number==8:
        print('August')
    elif number==9:
        print('September')
    elif number==10:
        print('October')
    elif number==11:
        print('November')
    else:
        print('Decemeber')
except ValueError:
    print('Please enter only integer value')




try:
    a = int(input('Enter a digit between 0 and 9'))
    if a<0 or a>9:
        print('Please enter a digit between 0 and 9')
    else:
        if a==0: 
            print('Zero')
        else:
            if a==1:
                print('One')
            else:
                if a==2:
                    print('Two')
                else:
                    if a==3:
                        print('Three')
                    else:
                        if a==4:
                            print('Four')
                        else:
                            if a==5:
                                print('Five')
                            else:
                                if a==6:
                                    print('Six')
                                else:
                                    if a==7:
                                        print('Seven')
                                    else:
                                        if a==8:
                                            print('Eight')
                                        else:
                                            if a==9:
                                                print('Nine')
except ValueError:
    print('Please enter only integer number')   


    