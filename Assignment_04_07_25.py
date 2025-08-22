
#Continue
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
'''output:
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
Outside loop'''

if ():
	print('Hyd')
	continue
	print('Sec')
'''output:
SyntaxError: 'continue' not properly in loop'''

#Break
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
print('Outside loop')
'''output:
1
Sec
Hello
2
Sec
Hello
3
Outside loop'''

if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
'''output:
SyntaxError: 'break' outside loop'''

#Pass
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
print('Outside loop')
'''output:
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
Outside loop'''

#Exit
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
print('Outside loop')
'''output:
1
Sec
Hello
2
Sec
Hello
3'''
#For else
for  i  in  range(1 , 8):
	print(i)
	if   i % 3 == 0:
		continue
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
print('Outside  loop')
'''output:
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
Outside  loop'''

for  i  in  range(1 , 8):
	print(i)
	if  i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
print('Outside  loop')
'''output:
1
Sec
Hello
2
Sec
Hello
3
Outside  loop'''

for  i  in  range(1 , 8):
	print(i)
	if  i == 8:
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
print('Outside loop')
'''output:
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
Outside loop'''
#Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
#print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

#Let  list  be   [10 , 20 , 15 , 12 , 18]
#1) What  is  the  output  if  15  is  seacrhed ?  --->  Found  at  index  2

#2) What  is  the  output  if  19  is  seacrhed ?  --->  Not  found

list1=[10 , 20 , 15 , 12 , 18]
n=int(input("Enter the number to be searched"))
for i in range(len(list1)):
  if list1[i]==n:
    print(f'{n} found at {i}')
    break
else:
     print("not found")
'''output:
Enter the number to be searched15
15 found at 2
Enter the number to be searched19
not found'''
#Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
#and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)


lst = eval(input("Enter elements of list:"))
x = eval(input("Enter the number to search: "))
i = 0
found = False
while i < len(lst):
    if lst[i] == x:
        print(f"Found at index {i}")
        found = True
        break  
    i += 1  
else:
    print("Not found")
output:
Enter elements of list:25,10.8,'Hyd',True
Enter the number to search: 10.8
Found at index 1

lst = eval(input("Enter elements of list:"))
x = eval(input("Enter the number to search: "))
i = 0
count=0
found = False
while i < len(lst):
    if lst[i] == x:
        print(f"Found at index {i}")
        found = True
        count+=1
    i += 1 
print(f'{x} is found {count} times')    
output:
Enter elements of list:10,10,20,19,13,15,13,10
Enter the number to search: 10
Found at index 0
Found at index 1
Found at index 7
10 is found 3 times

#Walrus Operator
print(a := 25)#25
print(a = 25)#TypeError: 'a' is an invalid keyword argument for print()
print(a)#25
print(a := 6 + 7)#13
print(a)#13
print((a := 6) + 7)#13
print(a)#6
print((a = 6) + 7)#SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

a = 0
if  a == 0:
	print('Hyd')#Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)#Sec:0
if  c = 0:#SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?

	print('Hyd')#Hyd
else:
	print('Sec')#SyntaxError: invalid syntax

a = b = c = 25
print(a , b , c)#25 25 25
del   a
print(b , c)#25 25
print(a)#ERROR!NameError: name 'a' is not defined
del   b
print(c)#25
print(b)#NameError: name 'b' is not defined
del   c
print(c)#NameError: name 'c' is not defined

a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)#25 10.8 Hyd
del   a , b , c
print(a)#NameError: name 'a' is not defined
print(b)#NameError: name 'b' is not defined
print(c)#NameError: name 'c' is not defined

a = [10 , 20 , 15 , 18]
print(a)#[10, 20, 15, 18]
del  a[2]
print(a)#[10, 20, 18]
del  a
print(a)#NameError: name 'a' is not defined
print(a[0])#NameError: name 'a' is not defined

a = (10 , 20 , 15 , 18)
print(a)#(10, 20, 15, 18)
print(a[0])#10
del  a[2]
del  a
print(a)#TypeError: 'tuple' object doesn't support item deletion
print(a[0])#TypeError: 'tuple' object doesn't support item deletion

