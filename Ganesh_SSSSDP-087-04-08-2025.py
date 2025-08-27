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

  #output
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

   # output
	1
	Sec
	Hello
	2
	Sec
	Hello
	3
	Outsideloop


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break           # here we connot use break because break stmt only for while ,for loops only
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

  # outputs
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
	Outsideloop


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

  #outputs
	1
	Sec
	Hello
	2
	Sec
	Hello
	3
	Outside loop

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
    #  outputs
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
	sec
	Hello
	else suite
	outside loop

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

	#outputs
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

    # outputs
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

5) W…

 Enter any list: [10,20,15,12,18]
Enter the element to be searched : 15
Found  at   index  :   2

 Enter any list: [25,10.8,'Hyd',True]
Enter the element to be searched : 3+4j
Not  Found

 '''
Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

 # Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found   3  times

'''

	#outputs
	l= eval(input('enter a list nums: '))
	search_element= eval(input('search a element: '))
	count=0
	for i in range(len(l)):
		if search_element==l[i]:
			print(l[i],'found a element at index: ',i)
			count=count+1
		else:
			print('not found')
	print(l[i],'is found ',count,'times')


 #  Walrus   operator (:=)  demo  program
print(a := 25)		# here we are assigning reference a on object 25 print i.e 25 		
print(a = 25)		#error because here we assigning the reference on object 
print(a)		# 25
print(a := 6 + 7)	#here we are assigning reference a on object 6 +7 and its add and print i.e 13 
print(a)		#13
print((a := 6) + 7)	#13
print(a)		#6
print((a = 6) + 7)	#error because here we cannot are assigning the reference of object 


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

   # outputs
	Hyd
	Sec: 0
	

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
 Enter input  (ctrl + z  to  stop)  :  25
Enter input  (ctrl + z  to  stop)  :  10.8
Enter input  (ctrl + z  to  stop)  :  True
Enter input  (ctrl + z  to  stop)  :  36.9
Enter input  (ctrl + z  to  stop)  :  45
Enter input  (ctrl + z  to  stop)  :  False
Enter input  (ctrl + z  to  stop)  :  92.8
Enter input  (ctrl + z  to  stop)  :  ^Z
Average :   30.214285714285715

	#outputs
	num=eval(input('(ctrl + z to stop):  '))
	for i in range(len(num)):
		num[i]/len[num]
		


   #  del  operator  demo program  (Home  work)
a = 25
print(a)	# 25
del   a		# here we are deleting the object of a 
print(a)	# error because here we are already deleted the object a


 # Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)      # 25 25 25
del   a			# here we are deleting the object of a 
print(b , c)		# 25 25
print(a)		# error because here we are already deleted the object a
del   b			# here we are deleting the object of a
print(c)		# 25
print(b)		# error because here we are already deleted the object b
del   c			# here we are deleting the object of c
print(c)		# error because here we are already deleted the object c


  #  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)   	# 25 10.8 'Hyd'
del   a , b , c		# here we are deleting object of a , b, c
print(a)		# error because here we are deleted object a 
print(b)		# error because here we are deleted object b 
print(c)		# error because here we are deleted object c 


 # Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)      # [10, 20, 15, 18]
del  a[2]	# here delete index of 2 i.e [10, 20, 18]
print(a)	# [10, 20, 15, 18]
del  a		# here we are deleteing the object a
print(a)	# error here object is already deleted
print(a[0])	# error because we cannot found list of 0


 # Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)         # Here print all nums from tuple (10, 20, 15, 18)
print(a[0])      #  here print a(index-0) i.e= 10
del  a[2]	# error 
del  a           # here delete object of a
print(a)         # (10,20,15,18)
print(a[0])	# 10