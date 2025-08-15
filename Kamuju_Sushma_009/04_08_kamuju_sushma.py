#Home Work-1
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
#output:
# Sec <newline> Hello  <nl> Sec <nl> Hello <nl> Sec <nl> Hello <nl> Sec <nl> Hello <nl> Sec <nl> Hello <nl>

#Home Work-2
# Identify Error  (Home  work)
# if ():
# 	print('Hyd')
# 	continue
# 	print('Sec')
# Reason for error: continue can be used only in loops

#Home Work-3
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
#output: 1 <nl> sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl> Outside loop

#Home Work-4
# Identify Error  (Home  work)
# if(10 , 20 , 30):
# 	print('Hyd')
# 	break
# 	print('Sec')
#Reason for error: break can be used only in loops

#Home Work-5
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

#output: 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl>
# 3 <nl> Hyd <nl> Hello <nl> 4 <nl> Sec <nl> Hello <nl> 5 <nl> Sec <nl> Hello <nl>
# 6 <nl> Hyd <nl> Hello <nl> 7 <nl> Sec <nl> Hello <nl> Outside loop

#Home Work-6
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

#output: 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello 

#Home Work-7
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
#output: 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello
#3 <nl> Hello <nl> 4 <nl> Sec <nl> Hello <nl> 5 <nl> Sec <nl> Hello
# 6 <nl> Hello <nl> else suite <nl> Outside loop

#else block will be executed because, break did not occur

#Home Work-8
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

#output: 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello <nl>
# 3 <nl> Outside loop

#Home Work-9
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

#output: 1 <nl> Sec <nl> Helo <nl> 2 <nl> Sec <nl> Helo <nl> 3 <nl> Sec <nl> Helo <nl> 4 <nl> Sec <nl> Helo <nl> 5 <nl> Sec <nl> Helo <nl>
# 6 <nl> Sec <nl> Helo <nl> 7 <nl> Sec <nl> Helo <nl>  else suite <nl> outside loop
 
#Home Work-10
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
# l=[10,20,15,12,18]
l=eval(input("Enter any list: "))
x=eval(input("Enter the element to be searched "))
found=False
for i in range(len(l)):
    if x == l[i]:
        print(f'Found at index {i}')
        found = True
        break
if not found:
	print(f'Not found')

#Home Work-11
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
l=eval(input("Enter any list: "))
x=eval(input("Enter the element to be searched "))
c=0
for i in range(len(l)):
    if x == l[i]:
        print(f'{x} is Found at index {i}')
        c+=1
print(f'{x} is found {c} times')

#Home Work-12
#  Walrus   operator (:=)  demo  program
print(a := 25) #25
print(a = 25) #nothing is printed
print(a) #24
print(a := 6 + 7) #13
print(a) #13
print((a := 6) + 7) #13
print(a) #6
# print((a = 6) + 7) #7

#Home Work-13
# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
#Hyd
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
#Hyd
# if  c = 0:
# 	print('Hyd') #Hyd 
# else:
# 	print('Sec')

#Home Work-14
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

# Enter input  (ctrl + z  to  stop)  :  25
# Enter input  (ctrl + z  to  stop)  :  10.8
# Enter input  (ctrl + z  to  stop)  :  True
# Enter input  (ctrl + z  to  stop)  :  36.9
# Enter input  (ctrl + z  to  stop)  :  45
# Enter input  (ctrl + z  to  stop)  :  False
# Enter input  (ctrl + z  to  stop)  :  92.8
# Enter input  (ctrl + z  to  stop)  :  ^Z
# Average :   30.214285714285715
sum=0
ctr=0
try:
    while True:
        x = eval(input("Enter input (Ctrl + Z to stop): "))
        sum += x
        ctr += 1
except EOFError:
	print(f'Average : {sum/ctr}')

#Home Work-15
#  del  operator  demo program  (Home  work)
a = 25
print(a) #25
del   a
print(a) #error

#Home Work-16
# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) #25 25 24
del   a 
print(b , c) #25 25
print(a) #error
del   b 
print(c)#25
print(b) #error
del   c 
print(c) #error

#Home Work-17
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
print(a)#error
print(b)#error
print(c)#error

#Home Work-18
# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) # [10 , 20 , 15 , 18]
del  a[2]
print(a) #[10 , 20 , 18]
del  a
print(a)#error
print(a[0])#error

#Home Work-19
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) #(10 , 20 , 15 , 18)
print(a[0]) #10
del  a[2] #error
del  a #error
print(a) #(10 , 20 , 15 , 18)
print(a[0]) #10

#reason for error: tuples are immutable