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
"""o/p: 
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
Outside loop"""
# Identify Error  (Home  work)
if ():
	print('Hyd')
	#continue  # Error continue is not use in if()
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
"""o/p:
1
Sec
Hello
2
Sec
Hello
3
Outside loop
"""


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	#break  # Error the break con’t use the if()
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
"""o/p:
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
"""

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
"""o/p:
1
Sec
Hello
2
Sec
Hello
3
"""
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
"""o/p:
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
else  suite
Outside  loop
"""

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
"""o/p:
1
Sec
Hello
2
Sec
Hello
3
Outside  loop"""


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
"""o/p:
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
else  suite
Outside loop

"""
"""
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

6) Hint: Use  for  loop
"""
a = eval(input("Enter a list : "))
b = eval(input("Enter element to search: "))
for i in range(len(a)):
    if a[i] == b:
        print("Found at index :",i)
        break  
else:
    print("Not found")


"""Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found   3  times
"""
a = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
b= int(input("Enter element to search: "))
count = 0
for i in range(len(a)):
    if a[i] == b:
        print(f"{b} is found at index {i}")
        count += 1
if count > 0:
    print(f"{b} is found {count} times")
else:
    print(f"{b} is not found in the list")


#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) # Error
print(a)  #25
print(a := 6 + 7)  # 13
print(a)  # 13
print((a := 6) + 7)   #13
print(a)   #6
#print((a = 6) + 7) # Error


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
#if  c = 0:                                     # Error
	print('Hyd')
#else:
	print('Sec')


"""(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True = 36.8
ctr = 0 + 1 + 1 + 1 = 3

1) What  is  ctrl + z ?  ---> End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  ---> Throws  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  ---> ctrl + d
"""
sum = 0
c = 0
try:
    while True:
        a= eval(input("enter input (ctrl + z to stop) :"))
        sum += a
        c += 1
except:
    print("Average :",sum/c)




#  del  operator  demo program  (Home  work)
a = 25
print(a)  # 25
del   a
print(a)  # Error


# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)  # 25 25 25
del   a
print(b , c)  # 25 25
print(a) # Error
del   b
print(c)  # 25
print(b)  # Error
del   c
print(c)  # Error




#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 hyd
del   a , b , c
print(a) # Error
print(b) # Error
print(c) # Error


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)  # [ 10,20,15,18 ]
del  a[2]  # [10,20,18]
print(a)  # [10,20,18]
del  a
print(a) #error
print(a[0])  #Error


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  # (10,20,15,18)
print(a[0])  # 10
del  a[2]
del  a
print(a)  #Error
print(a[0])  #Error

