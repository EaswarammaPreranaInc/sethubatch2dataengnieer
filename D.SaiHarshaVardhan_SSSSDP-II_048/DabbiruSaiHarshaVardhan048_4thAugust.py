                                                                                                                                   # Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')                                                                                                                                                                           output: 
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
# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue # no statement in if condition
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
output: 
 1
Sec
Hello
2
Sec
Hello
3
Outside loop
# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break#does not execute condition not properly assigned
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
output:1
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
output:
1
Sec
Hello
2
Sec
Hello
3
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
output:
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
output: 
1
Sec
Hello
2
Sec
Hello
3
Outside  loop
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
output:
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
numbers = [10, 20, 15, 12, 18]
x = int(input("Enter the number to search: "))
index = 0
found = False
while index < len(numbers):
    if numbers[index] == x:
        print(f"Found at index {index}")
        found = True
        break  
    index += 1  
if not found:
    print("Not found")

'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found   3  times
'''
numbers = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
x = int(input("Enter the number to search: "))
count = 0
for index in range(len(numbers)):
    if numbers[index] == x:
        print(f"{x} is found at index {index}")
        count += 1
if count == 0:
    print(f"{x} is not found")
else:
    print(f"{x} is found {count} times")
#  Walrus   operator (:=)  demo  program
print(a := 25)#print 25
print(a = 25)#error
print(a)#25
print(a := 6 + 7)#print 13
print(a)#print 13
print((a := 6) + 7)#print 13
print(a)#6
print((a = 6) + 7)#error
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')#print Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)# Sec  0
if  c = 0:
	print('Hyd')#error
else:
	print('Sec')#error
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
sum = 0
count = 0

print("Enter numbers one by one (use Ctrl+Z to stop):")

try:
    while True:
        user_input = input()
        value = eval(user_input)  
        sum_values += value
        count += 1
except :
    if count == 0:
        print("No inputs given.")
    else:
        average = sum_values / count
        print(f"Sum = {sum_values}")
        print(f"Count = {count}")
        print(f"Average = {average}")
#  del  operator  demo program  (Home  work)
a = 25
print(a)#print 25
del   a
print(a)#error a is undefined
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)# 25 25 25
del   a
print(b , c)# 25 25
print(a)#error
del   b
print(c)# 25
print(b)#error
del   c
print(c)#error
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)# 25 10.8 Hyd
del   a , b , c
print(a)#error
print(b)#error
print(c)#error
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)# [10, 20, 15, 18]
del  a[2]
print(a)# [10, 20, 18]
del  a
print(a)#error
print(a[0])#error
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)#print  (10 , 20 , 15 , 18)
print(a[0])# 10
del  a[2]#error del is not supported in tupple
del  a
print(a)#error
print(a[0])#error
