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
'''
##1
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
# if ():
# 	print('Hyd')
# 	continue
# 	print('Sec')

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
'''
##1
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
	# break
	# print('Sec')

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
'''
##1
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
print('Outside loop')
'''
##  1
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
print('Outside  loop')
'''
## 1
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
   else  suite
Outside  loop
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
print('Outside  loop')
'''
## 1
   Sec
   Hello
   2
   Sec
   Hello
   3
   Outside  loop
   '''

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
'''
## 1
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
else  suite
Outside loop
'''

try:
    lst = eval(input("Enter any list: "))
    x = eval(input("Enter the element to be searched: "))
    found = False 
    for i in range(len(lst)):
        if lst[i] == x:
            print("Found at index:", i)
            found = True
            break  # Stop searching once found
    if not found:
        print("Not Found")
except:
    print("Invalid input. Please enter proper list and element.")
'''
o/p:
Enter any list: [10,20,15,12,18]
Enter the element to be searched: 15
Found at index:2
'''

print(a := 25) # 25
print(a = 25)  # Error
print(a)       # 25
print(a := 6 + 7)# 13
print(a)         # 13
print((a := 6) + 7)# 13
print(a)           # 6
#print((a = 6) + 7) # invalid syntax

a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec') # Hyd 
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b) # Sec : 0
#if  c = 0:
# 	print('Hyd')
# else:
# 	print('Sec')

a = 25
print(a) # 25
del   a
print(a) # there is no element a 

a = b = c = 25
print(a , b , c) # 25 25 25
del   a      # removing a
print(b , c) # 25 25
print(a)     # their is no a
del   b      #  removing b
print(c)     # 25
print(b)     # there is no b
del   c      # removing c
print(c)     # there is no c

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 , 10.8 , 'Hyd'
del   a , b , c # removes all the a,b,c
print(a) # Error as their is not a we already deleted
print(b) # Error as their is not b we already deleted
print(c) # Error as their is not c we already deleted

a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del  a[2] # Removes a[2]=15
print(a) # [10 , 20 , 18]
del  a # error
print(a) # [10 , 20 , 18]
print(a[0]) # 10

a = (10 , 20 , 15 , 18)
print(a) # a = (10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2] # Tuple does not support 
del  a # Invalid
print(a) # a = (10 , 20 , 18)
print(a[0]) # 10