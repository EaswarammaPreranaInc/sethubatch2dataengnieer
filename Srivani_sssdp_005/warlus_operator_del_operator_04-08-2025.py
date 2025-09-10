
# Find  outputs  (Home  work)
for  i   in   range(1 , 8): # range from 1 to 7
	print(i) # prints 
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

'''
Outputs:
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
	continue # Error because continue must be in for loop or while loop
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
print('Outside loop')

'''
Outputs:
1
Sec
Hello
2
Sec
hello
3
Outside loop
'''





# Identify Error  (Home  work)
if(10 , 20 , 30): 
	print('Hyd')
	break  # Error because break must be in either for loop or while loop
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
print('Outside loop')

'''
Outputs:
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
		exit() # stops execution of program
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

'''
Outputs:
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
print('Outside loop')

'''
Outputs:
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
print('Outside loop')

'''
Outputs:
1
Sec
Hello
2
Sec
Hello
3
Outside loop
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
Outputs:
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
1) What  is  the  output  if  15  is  seacrhed ?  --->  Found  at  index  2

2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

3) What  action  to  be  made  when  'x'  does  not  match  with  the  current  element  of  list ?  --->
																						Compare  'x'  with  next  element  of  list

4) What  action  to  be  made  when  'x'  matches   with  list  element ?  --->
																				Print  found   message  along  with  index  and
																				do  not  search  for  'x'  in  rest  of  the  list

5) What  action  to  be  made  when  'x'   does  not  match  with  all  the  elements  of  list ?  --->
																										Print  not  found   message

6) Hint: Use for loop
'''
list = eval(input("Enter any list:"))
n = eval(input("Enter the element to be searched:"))
for i in range(len(list)):
    if list[i] == n:
        print("Found at index : " , i)
        break
else:
    print("Not Found")
	






'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found 3 times
'''
list = eval(input("Enter any list:"))
n = eval(input("Enter the element to be searched:"))
count = 0
for i in range(len(list)):
    if list[i] == n:
        print(n, "is found at index", i)
        count += 1
if count > 0:
    print(n,"is found", count, "times")
else:
    print("Not Found")
	






#  Walrus   operator (:=)  demo  program
print(a := 25) # Value of 'a' is 25 and result of 'a' is also 25 so prints 25
print(a = 25) # Error because value of 'a' is 25 and result of 'a' is nothing
print(a) # prints 25 
print(a := 6 + 7) # print(a := 13), prints 13 , value of 'a' is 13 and result of 'a' is 13
print(a) # print 13
print((a := 6) + 7) # prints 13, value of 'a' is 6 and result of 'a' is 6 so print(6 + 7)
print(a) # prints 6
print((a = 6) + 7) # Error 







# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') # prints Hyd because 0 == 0 is True
else:
	print('Sec')
if  b := 0:
	print('Hyd') # Error because value of 'b' is 0 and result of 'b'is 0
else:
	print('Sec : ' , b) # prints Sec: 0
if  c = 0: # Error because value 'c' is 0 and result of 'c' is nothing
	print('Hyd') 
else: # Error
	print('Sec') # prints Sec
	







'''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True = 36.8
ctr = 0 + 1 + 1 + 1 = 3

1) What  is  ctrl + z ?  ---> End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  ---> Throws  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  ---> ctrl + d
'''
count=0
sum=0
try:
    while True:
        n = eval(input("Enter input  (ctrl + z  to  stop)  :"))
        count += 1
        sum += n
except EOFError:
    try:
        print("Average:", sum/count)
    except ZeroDivisionError:
        print("Enter atleast one input")
    except NameError:
        print("Input cannot be string")
    except TypeError:
        print("Input cannot be string")
		




#  del  operator  demo program  (Home  work)
a = 25 # object 25 assigned to ref 'a'
print(a) # prints 25
del  a # deletes ref 'a' and object automatically deleted by PVM
print(a) # Error because ref 'a' is already deleted





# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # prints 25<space>25<space>25
del   a # deletes ref 'a'
print(b , c) # prints 25<space>25
print(a) # Error because ref 'a' is already deleted
del   b # deletes ref 'b'
print(c) # prints 25
print(b) # Error because ref 'b' is already deleted
del   c # deletes ref 'c' and object is automatically deleted by PVM
print(c) # Error because ref 'c' is already deleted





#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd' # ref 'a' points to int object 25,ref 'b' points to float object 10.8 and ref 'c' points to string object 'Hyd'
print(a , b , c) # prints 25<space>10.8<space>Hyd
del   a , b , c # deletes ref a, ref b, ref c and objects are also automatically deleted by PVM
print(a) # Error because ref 'a' is already deleted
print(b) # Error because ref 'b' is already deleted
print(c) # Error because ref 'c' is already deleted






# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18] # Ref 'a' points to list of 4 elements
print(a) # prints the list a i.e. [10, 20, 15, 18]
del  a[2] # deletes element at index 2 in list 'a'
print(a) # prints modified list 'a' i.e., [10, 20, 18]
del  a # deletes ref 'a' and list is automatically deleted by PVM
print(a) # Error because ref 'a' is already deleted
print(a[0]) # Error because ref 'a' is already deleted






# Find outputs  (Home work)
a = (10 , 20 , 15 , 18) # ref 'a' points to tuple of 4 elements
print(a)  # prints 'a' i.e., (10, 20, 15, 18)
print(a[0]) # prints element of tuple at index 0 i.e., 10
del  a[2] # Error bacause tuple is immutable
del  a # deletes ref 'a' and tuple is automatically deletes by PVM
print(a) # Error because ref 'a' is already deleted
print(a[0]) # Error because ref 'a' is already deleted
