a=complex(input('Enter 1st complex number:'))
b=complex(input('Enter 2nd complex number:'))
print(f'sum:',a+b)
print(f'difference:',a-b)
print(f'division',a/b)
print(f'product',a*b)

# Identify  error
else:
		print('else  suite')
print('Outside')# error due there is no if condition

print()

# Identify  error
if  9 > 5# error if condition always ends with colon
	print('Hello')
print('Bye')

# Identify  error
if  9 > 12:
	print('Hyd')
else# syntax error becoz else ends with colon
	print('Sec')


# Identify  error
if  (10,20,15):
print('Hyd')#after if must be indented like space or tab
else:
print('Sec')#after else must be indented like space or tab


print()

try:
    import calendar
    monthnum=int(input('enter month number:'))
    if monthnum==1:
        print('jan')
    elif monthnum==2:
        print('feb')
    elif monthnum==3:
        print('march')
    elif monthnum==4:
        print('april')
    elif monthnum==5:
        print('may')
    elif monthnum==6:
        print('june')
    elif monthnum==7:
        print('july')
    elif monthnum==8:
        print('august')
    elif monthnum==9:
        print('sept')
    elif monthnum==10:
        print('oct')
    elif monthnum==11:
        print('nov')
    elif monthnum==12:
        print('dec')
    else:
        print('input should in 1 and 12')
except:
    print('input should be in int')


a=int(input('enter num:'))
if a==0:
    print('zero')
else:
    if a==1:
        print('one')
    else:
        if a==2:
            print('two')
        else:
            if a==3:
                print('three')
            else:
                if a==4:
                    print('four')
                else:
                    if a==5:
                        print('five')
                    else:
                        if a==6:
                            print('six')
                        else:
                            if a==7:
                                print('seven')
                            else:
                                if a==8:
                                    print('eight')
                                else:
                                    if a==9:
                                        print('nine')
                                    else:
                                        print('inavalid')
