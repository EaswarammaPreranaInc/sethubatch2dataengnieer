#1st
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

#2nd
# Identify Error  (Home  work)
if ():
	print('Hyd')
	#continue
	print('Sec')
	
#3rd
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

#4th
# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	#break
	print('Sec')
	
#5th
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

#6th
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')

#7th
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

#8th
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

#9th
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

#10th
l=eval(input("Enter any List: "))
s=eval(input("Enter the element to be searched: "))
for i in range(len(l)):
    if l[i]==s:
        print("Found at index: " ,i )       
else:
    print("Not found")
	
#11th
lst = list(map(int, input().split()))
x = int(input())
c = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(x, "is found at index", i)
        c += 1
print(x, "is found", c, "times")

#12th
#  Walrus   operator (:=)  demo  program
print(a := 25)
#print(a = 25)
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)
#print((a = 6) + 7)

#13th
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
#if  c = 0:
	print('Hyd')
#else:
	print('Sec')
	
#14th
total = 0
count = 0
try:
    while True:
        val = input("Enter input  (ctrl + z  to  stop)  :  ")
        if val.lower() == "true":
            num = 1
        elif val.lower() == "false":
            num = 0
        else:
            num = float(val)
        total += num
        count += 1
except EOFError:
    if count > 0:
        print("Average :", total / count)
    else:
        print("No input given.")


#15th
#  del  operator  demo program  (Home  work)
a = 25
print(a)
del   a
#print(a)

#16th
a = b = c = 25
print(a , b , c)
del   a
print(b , c)
#print(a)
del   b
print(c)
#print(b)
del   c
#print(c)

#17th
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c
#print(a)
#print(b)
#print(c)

#18th
a = [10 , 20 , 15 , 18]
print(a)
del  a[2]
print(a)
del  a
#print(a)
#print(a[0])


#19th
# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)
print(a[0])
#del  a[2]
del  a
#print(a)
#print(a[0])

