4/08/2025 home work 
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

#####Answeres #####
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

-----_------------///////////////////
if ():
    print('Hyd')
    continue # SyntaxError: 'continue' not in a loop
    print('Sec')
-----_------------///////////////////
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

####### answere 
1
Sec
Hello
2
Sec
Hello
3
Outside loop
//////////////
# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
////////////////
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


########Answere 
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

############
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

@@@@@@
1
Sec
Hello
2
Sec
Hello
3
Outside  loop

##########
def search_element_no_duplicates(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            print(f"Found at index: {i}")
            return
    print("Not found")

# Example usage:
my_list = eval(input("Enter any list: "))
search_for = eval(input("Enter the element to be searched: "))
search_element_no_duplicates(my_list, search_for)
@@@@@@@@@@@
def search_element_with_duplicates(lst, element):
    count = 0
    for i in range(len(lst)):
        if lst[i] == element:
            print(f"{element} is found at index {i}")
            count += 1
    if count > 0:
        print(f"{element} is found {count} times")
    else:
        print(f"{element} not found")

# Example usage:
my_list = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]
search_for = 15
search_element_with_duplicates(my_list, search_for)
@@@@@@@@@@@@
#  Walrus   operator (:=)  demo  program
print(a := 25)           # 25
print(a = 25)            # SyntaxError: invalid syntax
print(a)                 # 25
print(a := 6 + 7)        # 13
print(a)                 # 13
print((a := 6) + 7)      # 13
print(a)                 # 6
print((a = 6) + 7)       # SyntaxError: invalid syntax

@@@@@@@@@@@@@@
a = 0
if  a == 0:
	print('Hyd')       # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)  # Sec : 0
if  c = 0:               # SyntaxError: invalid syntax
	print('Hyd')
else:
	print('Sec')
@@@@@@@@@@@@@@@
#  del  operator  demo program  (Home  work)
a = 25
print(a)      # 25
del   a
print(a)      # NameError: name 'a' is not defined

# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)   # 25 25 25
del   a
print(b , c)       # 25 25
print(a)           # NameError: name 'a' is not defined
del   b            # This line is not reached due to the error above
print(c)
print(b)
del   c
print(c)

#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)   # 25 10.8 Hyd
del   a , b , c
print(a)           # NameError: name 'a' is not defined
print(b)           # This line is not reached due to the error above
print(c)

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)           # [10, 20, 15, 18]
del  a[2]
print(a)           # [10, 20, 18]
del  a
print(a)           # NameError: name 'a' is not defined
print(a[0])        # This line is not reached due to the error above

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)           # (10, 20, 15, 18)
print(a[0])        # 10
del  a[2]          # TypeError: 'tuple' object doesn't support item deletion
del  a             # This line is not reached due to the error above
print(a)
print(a[0])
