# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')#outside loop
print()
# Identify Error  (Home  work)
if ():
	print('Hyd')
	#continue#error because this statement is permitted for only for and while loops.
    
	print('sec')
print()
# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')#outside loop
print()
# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	#break# error because this statement is permitted for only for and while loops.
	print('Sec')
print()
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
print('Outside loop')#outside loop
print()
# Find  outputs  (Home  work)
for  i   in   range(1 , 8):

	print(i)

	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

print()
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')#else suite
# End  of  the  loop
print('Outside  loop')#outside loop

print()
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
print('Outside  loop')#outside loop

print()
# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')#else suite
# End  of  the  loop
print('Outside loop')#outside loop
print()

#  Walrus   operator (:=)  demo  program
print(a:=25)
#print(a = 25)#invalid
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)
#print((a = 6) + 7)#error
print()
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
#if  c = 0:# error invalid
	print('Hyd')
#else: #error 
	print('Sec')
print()

#  del  operator  demo program  (Home  work)
a = 25
print(a)#25
del  a

#print(a)# error
print()
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)#25 25 25
del   a
print(b , c)#25 25
#print(a)#error
del   b
print(c)#25
#print(b)# error
del   c
#print(c)#error
print()
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)# 25 10.8 hyd
del   a , b , c
#print(a)# error
#print(b)#error
#print(c)#error
print()
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
del  a[2]
print(a)#[10, 20, 18]
del  a
#print(a)#error
#errorprint(a[0])#error
print()
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)#(10, 20, 15, 18)
print(a[0])#10
#del  a[2]#error
del  a
#print(a)#error
#print(a[0])#error
print()
a=eval(input('enter any list:'))
x=eval(input('enter the element to be searched:'))
for i in range(len(a)):
	if a[i]==x:
		print('found at index:',i)
		break
else:
		print('not found')
print()
		
a=eval(input('enter any list:'))
x=eval(input('enter the element to be searched:'))
ctr=0
for i in range(len(a)):
	if a[i]==x:
		print('found at index:',i)
		ctr+=1
	print(F'{x}is found {ctr}times')
print()
try:
	sum=ctr=0
	while True:
		x=eval(input('enter input(ctrl+z to stop):'))
		sum+=x
		ctr+=1
except EOFError:
	try:
		print(F'Average:{sum/ctr:.2f}')
	except ZeroDivisionError:
		print('enter atleast one input')
except NameError:
	print('input can not be string')		

	

	

	 

    
