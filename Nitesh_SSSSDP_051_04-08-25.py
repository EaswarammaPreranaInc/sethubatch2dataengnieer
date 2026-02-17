
#Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')

#Output
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
Outside loop
'''




# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue        #Continue is used only for & while loops not for if
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

#Output
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
	break		#Break cannot be used in 'if' it is only used for and while loop
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

#Output
1
Sec
Hello
2
Sec
Hello
3
Hello
4
Sec
Hello
5
Sec
Hello
6
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

#Output
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

#Output
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

#Output
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

#Output
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
n = eval(input("Enter any list:"))
s_element = eval(input("Enter the element to be searched: "))
for i in range(len(n)):
    if n[i]==s_element:
        print(f"Found  at   index  :{i}")
        break
else:
    print("Not  Found")

#Output
Enter any list:[10,20,15,12,18]            
Enter the element to be searched: 15
Found  at   index  :2

Enter any list:[25,10.8,'Hyd',True]
Enter the element to be searched: 3+4j
Not  Found




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

n = eval(input("Enter any list:"))
s_element = eval(input("Enter the element to be searched: "))
count = 0
for i in range(len(n)):
    if n[i]==s_element:
        print(f"Found  at   index  :{i}")
        count+=1
        continue
if count > 0:
    print(f"{s_element}  is  found   {count}  times")
else:
    print("Not found")

#Output
Enter any list:[10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]
Enter the element to be searched: 15
Found  at   index  :2
Found  at   index  :5
Found  at   index  :8
15  is  found   3  times



#  Walrus   operator (:=)  demo  program
print(a := 25) #Here reference a points to int-obj 25 and results the 25
print(a = 25) #Returns the error 
print(a)  #Returns the 25 as we are already initialized the value 25 to a
print(a := 6 + 7) #Returns the result of 13 which is a = 13
print(a) #Returns the 13 
print((a := 6) + 7) #Here reference a points to only 6 and then adds to 7 i.e 13
print(a) #Returns 6
print((a = 6) + 7) #Returns the error





# Find  outputs  (Home  work)
a = 0 #Reference a points to int-obj 0
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
	
#Outputs
'''
Hyd
sec : 0
#Error #Invalid syntax
'''


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
total = 0
count = 0

while True:
    print("Enter input  (ctrl + z  to  stop)")
    try:
        value = eval(input())
        total += value
        count += 1
    except EOFError:
        break
    except:
        print("Invalid input, please enter a number or boolean.")

if count > 0:
    average = total / count
    print(f"Average = {average}")
else:
    print("No valid inputs were entered.")

#Output
Enter input  (ctrl + z  to  stop)
25
Enter input  (ctrl + z  to  stop)
10.8
Enter input  (ctrl + z  to  stop)
True
Enter input  (ctrl + z  to  stop)
36.9
Enter input  (ctrl + z  to  stop)
45
Enter input  (ctrl + z  to  stop)
False
Enter input  (ctrl + z  to  stop)
92.8
Enter input  (ctrl + z  to  stop)
^Z
Average = 30.214285714285715



#  del  operator  demo program  (Home  work)
a = 25 #Reference a points to obj 25
print(a) #Returns the value of a
del   a #Deletes the reference a 
print(a) #THrows error as we have deleted the reference a



# Find  outputs  (Home  work)
a = b = c = 25 #Here reference a b c points to one object 25
print(a , b , c) #Returns the value of a b c is 25 25 25
del   a #Reference a is deleted 
print(b , c) #Returns the values of b c i.e 25 25
#print(a) #Throws error that a is not defined
del   b #Deletes the reference b
print(c) #Returns the value of c i.e 25
print(b) #Throws an error that b is not defined
del   c #deletes the reference c
print(c) #Throws an error that c is not defined



#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd' #Here reference a b c points to 3 different objects i.e 25 10.8 Hyd
print(a , b , c) #Returns the values of a b c i.e 25 10.8 Hyd
del   a , b , c #Here we are deleting the references a b c
print(a) #Throws the error that a is not defined
print(b) #Throws the error that b is not defined
print(c) #Throws the error that c is not defined




# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18] #Here the reference a points to list [10, 20, 15, 18]
print(a) #Returns the list which points to a
del  a[2] #Deletes the values of reference a where the index is 2 i.e 15
print(a) #Returns the list without 15
del  a #Here we are deleting the reference a 
print(a) #Error that a is not defines
print(a[0]) #Error that there is no a defined


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18) #Here a points to the tuple
print(a) #Returns the tuple 
print(a[0]) #returns the element at index 0 i.e 10
del  a[2] #Error that we cannot delete the elements from tuple since the tuple is immutable
del  a #Delete the reference a 
print(a) #Throws an error that a is not defined
print(a[0]) #Throws an error that a is not defined

 try:
    add=0
    count=0
    x=[]
    while True:
        x=eval(input('Enter input (ctrl + z to stop) : '))
        add += x
        count +=1
except:
    print(f'Average : {add/count:.2f} ')