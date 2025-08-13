


: # Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

##################### output:

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



: # Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')

#####################

Empty condition in if ():

if () is invalid.

Python requires a valid expression inside the if condition.

 Error: SyntaxError: expected expression

continue outside loop:

continue can only be used inside a loop (for or while).

Here, it’s placed inside an if block, but not inside any loop, so it raises an error.

 Error: SyntaxError: 'continue' not properly in loop



: # Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
##################
1
Sec
Hello
2
Sec
Hello
3
Outside loop



: # Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')
####################
1. Invalid if condition — if(10, 20, 30)
In Python, the condition in an if must be a single expression that evaluates to True or False.

(10, 20, 30) is a tuple, and non-empty tuples are always considered True, so Python won’t raise an error just for the condition itself.

BUT this form is confusing and incorrect for standard if usage. Python allows it, but it doesn't make logical sense unless you're intentionally checking a tuple.

So:  Syntactically valid but  Semantically wrong.

2. break used outside a loop
break is only allowed inside for or while loops.

Here, it's inside an if block but not inside any loop.

 Error:



: # Find  outputs  (Home  work)
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

#####################
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



: # Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
####################
1
Sec
Hello
2
Sec
Hello
3

: # Find  outputs  (Home  work)
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
###############
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


: # Find  outputs  (Home  work)
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
##################
1
Sec
Hello
2
Sec
Hello
3
Outside  loop


: # Find  outputs  (Home  work)
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
#############
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


: '''
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
: Enter any list: [10,20,15,12,18]
Enter the element to be searched : 15
Found  at   index  :   2
: Enter any list: [25,10.8,'Hyd',True]
Enter the element to be searched : 3+4j
Not  Found

###############
# Input the list
lst = eval(input("Enter any list: "))

# Input the element to search
x = eval(input("Enter the element to be searched: "))

# Flag to track if element is found
found = False

# Loop through the list
for index in range(len(lst)):
    if lst[index] == x:
        print("Found at index:", index)
        found = True
        break  # stop searching once found

# If element was not found after loop
if not found:
    print("Not Found")



: '''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found   3  times
##################
# Given list
lst = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]

# Element to search
x = int(input("Enter the element to be searched: "))

# Counter for number of times x is found
count = 0

# Loop through the list with index
for i in range(len(lst)):
    if lst[i] == x:
        print(x, "is found at index", i)
        count += 1

# Final count result
if count > 0:
    print(x, "is found", count, "times")
else:
    print(x, "is not found)



: #  Walrus   operator (:=)  demo  program
print(a := 25)
print(a = 25)
print(a)
print(a := 6 + 7)
print(a)
print((a := 6) + 7)
print(a)
print((a = 6) + 7)

##################

print(a := 25)

 Valid: assigns 25 to a and prints 25

print(a = 25)

 SyntaxError: cannot use normal assignment = inside print()

 Fix: a = 25; print(a)

print(a)

 Would work if previous line didn't cause error

print(a := 6 + 7)

 Valid: assigns 13 to a and prints 13

print(a)

Prints current value of a, which is 13

print((a := 6) + 7)

Assigns 6 to a, evaluates 6 + 7 = 13, prints 13

print(a)

 a is still 6, so prints 6

print((a = 6) + 7)

SyntaxError: = is not allowed in an expression like this




: # Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b)
if  c = 0:
	print('Hyd')
else:
	print('Sec')
##########
Hyd
Sec :  0
Hyd
Sec

last if condition is not executed error due to' ='




: '''
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
[04-08-2025 12:10] +91 99482 50500: Enter input  (ctrl + z  to  stop)  :  25
Enter input  (ctrl + z  to  stop)  :  10.8
Enter input  (ctrl + z  to  stop)  :  True
Enter input  (ctrl + z  to  stop)  :  36.9
Enter input  (ctrl + z  to  stop)  :  45
Enter input  (ctrl + z  to  stop)  :  False
Enter input  (ctrl + z  to  stop)  :  92.8
Enter input  (ctrl + z  to  stop)  :  ^Z
Average :   30.214285714285715
################
sum_ = 0
count = 0

print("Enter input (Ctrl + Z to stop):")

while True:
    try:
        data = input()
        value = eval(data)  # evaluates numbers, True/False etc.
        sum_ += value
        count += 1
    except EOFError:
        break
    except:
        print("Invalid input, skipped.")

if count > 0:
    average = sum_ / count
    print("Average:", average)
else:
    print("No valid inputs entered.")



: #  del  operator  demo program  (Home  work)
a = 25
print(a)####output:25
del   a
print(a)#####output:error due to name 'a' is not defined




: # Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)
del   a
print(b , c)
print(a)
del   b
print(c)
print(b)
del   c
print(c)

#############
25 25 25
25 25
NameError: name 'a' is not defined
25
NameError: name 'b' is not defined
NameError: name 'c' is not defined



: #  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)
del   a , b , c
print(a)
print(b)
print(c)
###############
25 10.8 Hyd
NameError: name 'a' is not defined
NameError: name 'b' is not defined
NameError: name 'c' is not defined



: # Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)
del  a[2]
print(a)
del  a
print(a)
print(a[0])

#################
a = [10, 20, 15, 18]
print(a)           # → [10, 20, 15, 18]
del a[2]
print(a)           # → [10, 20, 18]
del a
print(a)           # NameError
print(a[0])        # NameError (already error above)



: # Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)
print(a[0])
del  a[2]
del  a
print(a)
print(a[0])

##########
a = (10, 20, 15, 18)
print(a)           # → (10, 20, 15, 18)
print(a[0])        # → 10
del a[2]           #  TypeError: 'tuple' object doesn't support item deletion
del a
print(a)           #  NameError (if previous line not stopped execution)
print(a[0])        #  NameError
