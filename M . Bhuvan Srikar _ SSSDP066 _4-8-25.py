# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

'''
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside loop
'''


# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue # error as continue can use only in loops
	print('Sec')

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

'''
1
Sec
Hello
2
Sec
Hello
3
Outside loop
'''

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break # error as break can be used in the loops only
	print('Sec')

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
print('Outside loop')

'''
1
Sec
Hello
2
Sec
Hello
3
Hyd
Hello
4
Sec
Hello
5
Sec
Hello
6
Hyd
Hello
7
Sec
Hello
Outside loop
'''


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

'''
1
Sec
Hello
2
Sec
Hello
3
'''

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
print('Outside  loop')
'
'''
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
else suite
Outside loop
'''



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
print('Outside  loop')

'''
1
Sec
Hello
2
Sec
Hello
3
Outside loop
'''# Find  outputs  (Home  work)
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
print('Outside loop')

'''
1
Sec
Hello
2
Sec
Hello
3
Sec
Hello
4
Sec
Hello
5
Sec
Hello
6
Sec
Hello
7
Sec
Hello
else suite
Outside loop
'''

'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]
1) What  is  the  output  if  15  is  searched ?  --->  Found  at  index  2

2) What  is  the  output  if  19  is  searched ?  --->  Not  found

3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
												Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  when  'x'  matches   with  list  element ?  ---> Print  found   message  along  with  index  and
									do  not  search  for  'x'  in  rest  of  the  list

5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->
												Print  not  found   message

6) Hint: Use  for  loop
'''
a = eval(input('Enter any list : '))
n = int(input('Enter a element to be searched : '))
for i in range(len(a)):
	if a[i] == n:
		print(f'Found at index {i}')
		break
else:
	print('Element not found')

'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found   3  times
'''
a = eval(input('Enter any list : '))
n = int(input('Enter a element to be searched : '))
ctr = 0
for i in range(len(a)):
	if a[i] == n:
		print(f'{n} is found at index {i}')
		ctr += 1
else:
	print(f'{n} is found {ctr} times')


#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) # Error
print(a) # 25
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 6
print((a = 6) + 7) # error

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
if  c = 0: # error as in if cannot compare with =
	print('Hyd')
else:
	print('Sec')

'''
Hyd
Sec : 0
'''
'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True = 36.8
ctr = 0 + 1 + 1 + 1 = 3

1) What  is  ctrl + z ?  ---> End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  ---> Throws  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  ---> ctrl + d
'''
try:
	sum = 0
	ctr = 0
	while 1:
		a = eval(input('Enter input  (ctrl + z  to  stop) : '))
		sum += a
		ctr += 1
except EOFError:
	print(sum/ctr)

#  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a # deletes reference a 
print(a) # error as reference is deleted and so object

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 <space> 25 <space> 25
del   a # deletes reference a
print(b , c) # 25 <space> 25
print(a) # error as reference a is deleted
del   b # deletes reference b
print(c) # 25
print(b)  # error as reference b is deleted
del   c # deletes reference c
print(c)  # error as reference c is deleted


#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 <space> 25 <space> 25
del   a , b , c
print(a) # error as reference a is deleted
print(b) # error as reference b is deleted
print(c) # error as reference c is deleted

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del  a[2] # deletes element at index 2
print(a) # [10 , 20 , 18]
del  a # deletes whole object a
print(a) # error as object a is deleted
print(a[0]) # error as object a is deleted

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) # (10 , 20 , 15 , 18)
print(a[0]) # (20 , 15 , 18)
del  a[2] # deletes element at index 2 
del  a # deletes whole object
print(a) # error as object is deleted
print(a[0]) # error as a object is deleted
