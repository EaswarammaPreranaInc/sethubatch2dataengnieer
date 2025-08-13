# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

# OUTPUT:
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl> 3 <nl> 4 <nl> Sec <nl> Hello <nl> 
# 5 <nl> Sec <nl> Hello <nl> 6 <nl>  7 <nl> Sec <nl> Hello <nl> Outside loop


# Identify Error  (Home  work)
if ():
	print('Hyd')
	# continue
	print('Sec')   # continue can be used only inside for or while loop
	

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

#OUTPUT
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl> 3 <nl> 'Outside loop'


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	# break
	print('Sec')
	
# break can be used only inside for or while loop



# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

#OUTPUT
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl> 3 <nl> 'Hyd' <nl> Hello <nl> 
# 4 <nl> Sec <nl> Hello <nl> 5 <nl> Sec <nl> Hello <nl> 6 <nl> 'Hyd' <nl> Hello <nl> 
# 7 <nl> Sec <nl> Hello <nl> Outside loop


# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

# OUTPUTS:
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl> 3



# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')

# OUTPUT:
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl> 3 <nl> 4 <nl> Sec <nl> Hello <nl> 
# 5 <nl> Sec <nl> Hello <nl> 6 <nl>  7 <nl> Sec <nl> Hello <nl> else suite <nl> Outside loop


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
#End   of  the  loop
print('Outside loop')


#OUTPUT
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl> 3 <nl> 'Outside loop'


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')

# OUTPUT:
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl> 3 <nl> Sec <nl> Hello <nl> 4 <nl> Sec <nl> Hello <nl> 
# 5 <nl> Sec <nl> Hello <nl> 6 <nl> Sec <nl> Hello <nl> 7 <nl> Sec <nl> Hello <nl> else suite <nl> Outside loop



list = eval(input('Enter any list:  '))
element = eval(input('Enter the element to be searched:  '))
for i in list:
    if element == i:
        print('Found')
        break
else:
    print('Not Found')
	

list = eval(input('Enter any list:  '))
element = eval(input('Enter the element to be searched:  '))
count = 0
for i in range(len(list)):
    if element == list[i]:
        print(f'{list[i]} is found at index {i}')
        count += 1
else:
    print(f'Total count is {count}')
	

#  Walrus   operator (:=)  demo  program
print(a := 25)       #25 and a is assigned to 25
#print(a = 25)       #TypeError, a is not a keyword argument for print function
print(a)             #25
print(a := 6 + 7)    #13, a is assigned to 13
print(a)             #13
print((a := 6) + 7)  # a is assigned to 6 and prints 13
print(a)             # 6
#print((a = 6) + 7)  #SyntaxError


# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')         #Hyd
else:
	print('Sec')
if  b := 0:              #b is assigned to 0, and 0 is false
	print('Hyd')         
else:
	print('Sec : ' , b)  #'Sec: 0
# if  c = 0:               #c = 0 returns nothing, but one value should be there for if   
# 	print('Hyd')
# else:
# 	print('Sec')
	

try:
    sum = 0
    count = 0
    while(True):
        sum += eval(input('Enter input (ctrl + z to stop):  '))
        count += 1
except EOFError:
    print(f'Average: {sum/count}')   




#  del  operator  demo program  (Home  work)
a = 25
print(a)
del a
#print(a) #NameError

# Find  outputs  (Home  work)
a = b = c = 25    #3 ref's are assigned to 25
print(a , b , c)  # 25 <sp> 25 <sp> 25 <nl>
del   a 
print(b , c)      # 25 <sp> 25 <nl>
#print(a)          #NameError
del   b
print(c)          # 25
#print(b)          #NameError
del c
#print(c)          #NameError


#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)   # 25 <sp> 10.8 <sp> Hyd
del   a , b , c    
#print(a)            #NameError
#print(b)            #NameError
#print(c)            #NameError


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)        #[10 , 20 , 15 , 18]
del  a[2]       #20 is deleted
print(a)        #[10, 15, 18]
del  a          #entire list is deleted
#print(a)        #NameError
#print(a[0])     #NameError


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)
print(a[0])
del  a[2]
del  a
print(a)
print(a[0])

