# Find  outputs  (Home  work)
for  i   in   range(1 , 8): 
	print(i) # 1 2 3 4 5 6 7
	if  i % 3  == 0: # condition to check i is divisible by 3 or not
			continue # does nothing go to next line and continue loop
	else:
			print('Sec') 
	print('Hello')# Sec Hello Sec Hello Hello Sec Hello Sec Hello Hello Sec Hello
# End of loop
print('Outside loop') # Outside loop

# Identify Error  (Home  work)
if ():'''
Modify  following   program  with  walrus  operator
Hint:  Combine  lines  7   and   8  to a  single  line  with   walrus  operator
'''
try:
	sum =  ctr = 0
	while  True:
		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))
		sum += x
		ctr +=1	
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')
	print('Hyd')  
	continue # used only in 'for' or 'while' loops
	print('Sec')  

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i) # 1 2 3 
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello') 
# End  of  the  loop
print('Outside loop') # Sec Hello Sec Hello Outside loop

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break # # used only in 'for' or 'while' loops , to break loop
	print('Sec')

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) # 1 2 3 4 5 6 7 
	if   i % 3 == 0:
		pass # wont execute any stat pass to another stat
		print('Hyd')
	else:
		print('Sec')
	print('Hello') # Sec Hello Sec Hello Hello Sec Hello Sec Hello Hello Sec Hello
# End  of  the  loop
print('Outside loop') # Outside loop

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i) # 1 2 3
	if   i % 3 == 0:
		exit() # exits the programs 
	else:
		print('Sec')
	print('Hello') # Sec Hello Sec Hello 
# End  of  the  loop
print('Outside loop') # wont prints 

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i) # 1 2 3 4 5 6 7
	if   i % 3 == 0: 
		continue
	else:
		print('Sec')
	print('Hello') # Sec Hello Sec Hello Hello Sec Hello Sec Hello Hello Sec Hello 
else:
	print('else  suite') # else suite
# End  of  the  loop
print('Outside  loop') # Outside loop

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i) # 1 2 3
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello') # Sec Hello Sec Hello else suite
else:
	print('else  suite')
#End   of  the  loop
print('Outside  loop') # Outside loop

# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i) # 1 2 3 4 5 6 7
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello') # Sec Hello Sec Hello Hello Sec Hello Sec Hello Hello Sec Hello 
else:
	print('else  suite') # else suite
# End  of  the  loop
print('Outside loop') # Outside loop

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

6) Hint: Use  for  loop
'''
########### program ############
a = eval(input("Enter any list :")
x = int(input("Enter the element to be searched:"))
for i in range(len(a)):
     if a[i] == x:
	 print(F"Fount at index : {i}")
	 break
     else:
	 print("Not found")
####### out put #######
Enter any list: [10,20,15,12,18]
Enter the element to be searched : 15
Found  at   index  :   2
Enter any list: [25,10.8,'Hyd',True]
Enter the element to be searched : 3+4j
Not  Found

'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

'''
########### program ############
a = eval(input("Enter any list :")
x = int(input("Enter the element to be searched:"))
c = 0
for i in range(len(a)):
     if a[i] == x:
	 print(F"{x}  is  found  at  index  {i}")
	 c +=1 
     else:
	 print("Not found")
print(F"{x} is found {c} times")

############### output ###########
Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found   3  times
'''

#  Walrus   operator (:=)  demo  program
print(a := 25) # a is assigned to obj 25
print(a = 25) # ref a is assigned to obj 25
print(a) # 25
print(a := 6 + 7) # prints result a = 13
print(a) # 13
print((a := 6) + 7) # error
print(a) # 13
print((a = 6) + 7) # error

# Find  outputs  (Home  work)
a = 0 # ref a is assined to obj
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd') # Hyd
else:
	print('Sec : ' , b)
if  c = 0: # error
	print('Hyd')
else:
	print('Sec')

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
########### program ############
i=0
b=0
while True:
    print("Enter input  (ctrl + z  to  stop)  :", end = "")
    a = eval(input())
    if a == '^Z':
        break
    else:
        b +=a
        i+=1
print(F"Average: {b/i}")

#########output############
Enter input  (ctrl + z  to  stop)  :  25
Enter input  (ctrl + z  to  stop)  :  10.8
Enter input  (ctrl + z  to  stop)  :  True
Enter input  (ctrl + z  to  stop)  :  36.9
Enter input  (ctrl + z  to  stop)  :  45
Enter input  (ctrl + z  to  stop)  :  False
Enter input  (ctrl + z  to  stop)  :  92.8
Enter input  (ctrl + z  to  stop)  :  ^Z
Average :   30.214285714285715

#  del  operator  demo program  (Home  work)
a = 25 # ref a assigned to obj 
print(a) # prints obj 'a'
del   a # deletes reference 'a'
print(a) # error

# Find  outputs  (Home  work)
a = b = c = 25 # multiple assignments
print(a , b , c) # 25 25 25 
del   a # deletes ref 'a'
print(b , c) # 25 25 
print(a) # error
del   b # deletes ref 'b'
print(c) # 25
print(b) # error
del   c # deletes ref 'c'
print(c) # error

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c # deletes all the reference
print(a) # error
print(b) # error
print(c) # error

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18] # list obj
print(a) # [10 , 20 , 15 , 18]
del  a[2] # deletes element a[2]
print(a) # [10 , 20 , 18]
del  a # deletes ref a 
print(a) # error
print(a[0]) # error

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18) # tuple obj
print(a) # (10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2] # deletes a[2]
del  a # deletes ref 'a'
print(a) # error
print(a[0])  #error