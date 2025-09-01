"""
0408

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
'''
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
Outside loop'''


# Identify Error  (Home  work)
if ():
 	print('Hyd')
 	continue
 	print('Sec')
# continue cannot be used in if , it is used in loops only

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
'''1
sec
Hello
2
sec
Hello
3
Outside loop'''

# Identify Error  (Home  work)
if(10 , 20 , 30):
 	print('Hyd')
 	break
 	print('Sec')
# Break is used in loops only

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


'''
1
sec
Hello
2
sec
Hello
3
Hyd
Hello
4
sec
Hello
5
sec
Hello
6
Hyd
Hello
7
sec
Hello
Outside loop
'''



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
'''1
sec
Hello
2
sec
Hello
3'''


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
'''
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
'''

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
'''
1
Sec
Hello
2
Sec
Hello
3
else suite
Outside loop

'''


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
'''
1
Sec
Hello
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
else suite
Outside loop

'''



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

Enter any list: [10,20,15,12,18]
Enter the element to be searched : 15
Found  at   index  :   2

Enter any list: [25,10.8,'Hyd',True]
Enter the element to be searched : 3+4j
Not  Found

'''
a = [10 , 20 , 15 , 12 , 18]
tar = 15

for i in range(len(a)):
    if a[i] == tar:
        print(f'{tar} is found in {a} at index {i}')
        break
else:
    print(f'{tar} is not found in {a}')
 
'''



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
'''
a =  [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
tar = 15
count = 0
for i in range(len(a)):
    if a[i] == tar:
        print(f'{tar} is found at index {i}')
        count += 1
print(f'{tar} is found {count} times')
 
'''

#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) # error
print(a)   # 25
print(a := 6 + 7) # 13
print(a)  # 13
print((a := 6) + 7)  #13
print(a)  # 6
print((a = 6) + 7) #  error




# Find  outputs  (Home  work)
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
#Hyd
#Sec : 0


#  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a # a is deleted
print(a) # a is not defined


# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25,25,25
del   a # a is  deleted
print(b , c) # 25,25
print(a) # a is not defined
del   b # b is deleted
print(c) # 25
print(b) # b is not defined
del   c # c is deleted
print(c) # c is not defined


#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)  # 25,10.8,Hyd
del   a , b , c  #  a,b,c are deleted
print(a) # a is not defined
print(b) # b is not defined
print(c) # c is not defined


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #  [10 , 20 , 15 , 18]
del  a[2] # 15 is deleted
print(a) #  [10 , 20 , 18]
del  a # a is deleted
print(a) # a is not defined
print(a[0]) # a is not defined


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) #  (10 , 20 , 15 , 18)
print(a[0])  # 10
del  a[2] # error
del  a  # deletes the a
print(a) #  a is not defined
print(a[0]) #  a is not defined







# '''
(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

sum = 0 + 25 + 10.8 + True = 36.8
ctr = 0 + 1 + 1 + 1 = 3

1) What  is  ctrl + z ?  ---> End  of  inputs  i.e.  No  more  inputs

2) What  does  input()  function  do  when  input  is  ctrl + z ?  ---> Throws  EOFError

3) How  is   end  of  inputs  denoted  in  unix ?  ---> ctrl + d

Enter input  (ctrl + z  to  stop)  :  25
Enter input  (ctrl + z  to  stop)  :  10.8
Enter input  (ctrl + z  to  stop)  :  True
Enter input  (ctrl + z  to  stop)  :  36.9
Enter input  (ctrl + z  to  stop)  :  45
Enter input  (ctrl + z  to  stop)  :  False
Enter input  (ctrl + z  to  stop)  :  92.8
Enter input  (ctrl + z  to  stop)  :  ^Z
Average :   30.214285714285715
'''

total = 0
count = 0

print("Enter input (ctrl + z to stop):")

while True:
    try:
        val = input("Enter input (ctrl + z to stop):")
        if val.lower() == "true":
            num = True
        elif val.lower() == "false":
            num = False
        else:
            num = float(val)  # handles both int and float
        total += num
        count += 1
    except EOFError:
        break
    except ValueError:
        print("Invalid input. Skipping...")

if count == 0:
    print("No valid inputs entered.")
else:
    avg = total / count
    print("Average :", avg)
"""