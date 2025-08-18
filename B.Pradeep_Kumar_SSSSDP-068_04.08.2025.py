# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)  #   1,2,3,4,5,6,7
	if  i % 3  == 0:
			continue  # in 3,6 elements will be executed continue
	else:
			print('Sec')  #  if condition false then else condition executes
	print('Hello')  #  Hello
# End of loop
print('Outside loop') #  Outside loop prints always because of outside loop


# Identify Error  (Home  work)
if (): #  Error due to if needed atleast one condtion
	print('Hyd')
	continue  #  Continue only for loops
	print('Sec')


# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)  #  
	if   i % 3 == 0:   #  if condtion is true then break will executes 
		break
	else:
		print('Sec') # sec
	print('Hello')  # hello prints  when loop execute
# End  of  the  loop
print('Outside loop')  #  always prints 


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break  #  Error due to break must in loop
	print('Sec')



# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass  #  if condition is true then pass executes it means do nothiing
		print('Hyd')  #  hyd
	else:
		print('Sec') #  if condition is false then sec will prints
	print('Hello') # prints hello when in loop
# End  of  the  loop
print('Outside loop')  # always prints



# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()  #  if condition is true then whole remaining program stops execution
	else:
		print('Sec') # else sec
	print('Hello')# Helo
# End  of  the  loop
print('Outside loop')  #  Always prints


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)   #  1,2,3,4,5,6,7
	if   i % 3 == 0:
		continue  # if cond is true then it will continue next
	else:
		print('Sec')  # if cond is false then Sec will prints
	print('Hello')# when in loop it will prints
else:
	print('else  suite')  #  If For loop outof range then else will executes
# End  of  the  loop
print('Outside  loop')  # always prints


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)  #  1,2,3,4,5,6,7

	if  i % 3 == 0:
		break  #  If cond true then next pogram will stops inside loop
	else:
		print('Sec')  # if false then SEC will prints
	print('Hello')# always when in for loop
else:
	print('else  suite')  #  prints when for loop outof range
#End   of  the  loop
print('Outside  loop')  # always prints


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)  #  
	if  i == 8: # Error due to range is 1-7
		break
	else:
		print('Sec')  # sec
	print('Hello')# hello
else:
	print('else  suite')  # else prints when for out of range
# End  of  the  loop
print('Outside loop')  #  Always prints




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

6) Hint: Use  for  loop
'''


x= list(input("enter list "))

y=int(input("Enter a number is list :"))

for i in range(len(x)):
    if x[i]==y:
        print(f"found at index :{i}")
        break
else:
    print("Not found")



#  Walrus   operator (:=)  demo  program
print(a := 25)  # 25
print(a = 25)  #  Error
print(a)  # 25
print(a := 6 + 7)  #  a=13
print(a)  # 13
print((a := 6) + 7)  #  Error
print(a)  #  13
print((a = 6) + 7)  #  Error


# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')  # Hyd
else:
	print('Sec')
if  b := 0:  # Error
	print('Hyd')
else:
	print('Sec : ' , b)  # Sec,0
if  c = 0:
	print('Hyd')  
else:
	print('Sec')  #  Sec


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

print("Enter numbers (Ctrl + Z to stop):")

sum = 0
times = 0

try:
    while True:
        x = input()
        sum = sum + float(x)
        times = times + 1
except EOFError:
    pass

if times > 0:
    print("Average =", sum / times)
else:
    print("No input given.")


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)  #  tuple of a
print(a[0])  #  10
del  a[2]  #  15
del  a #  Whole tuple will deleted
print(a)  # empty
print(a[0])  #  empty
