1.# Find  outputs  (Home  work)
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



2.# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec') # Error




3.# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

#output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop



4.# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')#Error




5.# Find  outputs  (Home  work)
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

#output:
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




6.# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

#output:
1
Sec
Hello
2
Sec
Hello
3






7.# Find  outputs  (Home  work)
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

#output:
1
sec
Hello
2
sec
Hello
3
4
sec
Hello
5
sec
Hello
6
7
sec
Hello
Outsideloop





8.# Find  outputs  (Home  work)
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

#output:
1
sec
Hello
2
sec
Hello
3
else  suite
Outside  loop



9.# Find  outputs  (Home  work)
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

#output:
1
sec
Hello
2
sec
Hello
3
sec
Hello
4
sec
Hello
5
sec
Hello
6
sec
Hello
7
sec
Hello
else  suite
Outside  loop


10.'''
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
sample outputs:
Enter any list: [10,20,15,12,18]
Enter the element to be searched : 15
Found  at   index  :   2


Enter any list: [25,10.8,'Hyd',True]
Enter the element to be searched : 3+4j
Not  Found

#program:

list = eval(input("Enter any list:"))
a = int(input("Enter any element;"))
search = False
for index in range(len(list)):
    if list[index] == a:
        print("Found at index :" , index)
        search = True
        break
if not search:
    print("Not Found:")







11.'''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found   3  times
'''
#program:
lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
x = int(input("Enter the element to be searched: "))

count = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(f"{x} is found at index {i}")
        count += 1
if count > 0:
    print(f"{x} is found {count} times")
else:
    print(f"{x} is not found in the list")






12.#  Walrus   operator (:=)  demo  program
print(a := 25)		#25
print(a = 25)		#Error
print(a)		#Error
print(a := 6 + 7)	#13
print(a)		#Error
print((a := 6) + 7)	#13
print(a)		#Error
print((a = 6) + 7)	#Error




13.# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')		#Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)	#sec
if  c = 0:#Error
	print('Hyd')
else:
	print('Sec')




'''
14.(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True = 36.8
ctr = 0 + 1 + 1 + 1 = 3

1) What  is  ctrl + z ?  ---> End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  ---> Throws  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  ---> ctrl + d
'''
sample output:
Enter input  (ctrl + z  to  stop)  :  25
Enter input  (ctrl + z  to  stop)  :  10.8
Enter input  (ctrl + z  to  stop)  :  True
Enter input  (ctrl + z  to  stop)  :  36.9
Enter input  (ctrl + z  to  stop)  :  45
Enter input  (ctrl + z  to  stop)  :  False
Enter input  (ctrl + z  to  stop)  :  92.8
Enter input  (ctrl + z  to  stop)  :  ^Z
Average :   30.214285714285715

#program:
total = 0
count = 0

print("Enter input (Ctrl + Z to stop):")

while True:
    try:
        user_input = input()
        value = eval(user_input)
        total += value
        count += 1
    except EOFError:
        break
    except:
        print("Invalid input. Skipping...")

if count > 0:
    avg = total / count
    print("Average:", avg)
else:
    print("No valid inputs to calculate average.")








15.#  del  operator  demo program  (Home  work)
a = 25
print(a)		#25
del   a
print(a)		#Error




16.# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)	#25 25 25
del   a
print(b , c)		#25 25
print(a)		#Error
del   b
print(c)		#25
print(b)		#Error
del   c
print(c)		#Error




17.#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)	#25 10.8 Hyd
del   a , b , c
print(a)		#Error
print(b)		#Error
print(c)		#Error




18.# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)		#[10 , 20 , 15 , 18]
del  a[2]
print(a)		#[10 , 20 , 18]
del  a			#Error
print(a)		#Error
print(a[0])		#Error




19.# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)	#(10 , 20 , 15 , 18)
print(a[0])	#10
del  a[2]
del  a
print(a)	#Error
print(a[0])	#Error