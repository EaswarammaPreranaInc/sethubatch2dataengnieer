a)for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')
#1
#Sec
#Hello
#2
#Sec
#Hello
#3
#4
#
Sec
#Hello
#5
#Sec
#Hello
#6
#7
#Sec
#Hello
#Outside loop

b)if ():
	print('Hyd')
	continue
	print('Sec') # 'continue' can be used in for and while loop only

c)for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
‘’’1
Sec
Hello
2
Sec
Hello
3
Outside loop’’’

d)if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec') # 'continue' can be used in for and while loop only

e)for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		pass
		print('Hyd')
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
‘’’1
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
Outside loop’’’

f)for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
‘’’ 1
Sec
Hello
2
Sec
Hello
3’’’

g)for  i  in  range(1 , 8):
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
‘’’ 1
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
Outside  loop’’’

h)for  i  in  range(1 , 8):
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
‘’’ 1
Sec
Hello
2
Sec
Hello
3
Outside  loop’’’

i)for  i  in  range(1 , 8):
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
‘’’ 1
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
Outside loop’’’
 
j) Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates) 
list = eval(input("Enter any list: "))
x = eval(input("Enter the element to be searched : "))
for i in range(len(list)):
    if list[i] == x:
        print("Found  at   index  :  ", i)
        break
else:
    print("Not  Found")

k) Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)
 lst = eval(input("Enter the list: "))  
ele = eval(input("Enter the element to be searched: ")) 
found_times = 0
for i in range(len(lst)):
    if lst[i] == ele:
        print(ele, "is found at index", i)
        found_times = found_times + 1  # manual counter
if found_times > 0:
    print(ele, "is found", found_times, "times")
else:
    print(ele, "Not Found")

l)print(a := 25) #25
print(a = 25) # 'a' is an invalid keyword argument for print()
print(a) # name 'a' is not defined
print(a := 6 + 7) # 13
print(a) # 13
print((a := 6) + 7) # 13
print(a) # 13
print((a = 6) + 7) # SyntaxError

m)a = 0
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b) # Sec :  0 since 0 is zero element
if  c = 0:
	print('Hyd') # error c is referring to 0 but not pointing 0
else:
	print('Sec')

n) s = 0
ctr = 0
try:
    while True:
        x = eval(input("Enter input (Ctrl+Z to stop): "))
        s += x
        ctr += 1
except EOFError:
    pass

if ctr > 0:
    avg = s / ctr
    print("Average =", avg)  # Average = 12.266666666666667
else:
    print("No input provided.")

o)a = 25
print(a) # 25
del   a
print(a) # name 'a' is not defined

p)a = b = c = 25
print(a , b , c) # 25 25 25
del   a

q)print(b , c) # 25 25 
print(a) # name 'a' is not defined
del   b
print(c) # 25
print(b) # name 'b' is not defined
del   c
print(c) # name 'c' is not defined

r)a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
print(a) # name 'a' is not defined
print(b) # name 'b' is not defined
print(c) # name 'c' is not defined


s)a = [10 , 20 , 15 , 18]
print(a) # [10, 20, 15, 18]
del  a[2]
print(a) # [10, 20, 18]
del  a
print(a) # name 'a' is not defined
print(a[0]) # name 'a' is not defined

t)a = (10 , 20 , 15 , 18)
print(a) # (10, 20, 15, 18)
print(a[0]) # 10
del  a[2]
del  a
print(a) # name 'a' is not defined
print(a[0]) # name 'a' is not defined

