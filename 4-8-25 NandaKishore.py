#NANDA KISHORE VEMULA

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

# Outputs
	'''1
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
	continue   #continue  should be with in loops  only  for (or) while
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
 
 #outputs
'''1
   Sec
   Hello
   2
   Sec
   Hello
   3
   Outside loop'''




 # Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break  #Error  break should be with  loops  only  for (or) while
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

'''1
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
'''
1
Sec
Hello
2
Sec
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


# Outputs
	'''1
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
	   else suite
	   Outside loop
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

 #outputs
'''1
   Sec
   Hello
   2
   Sec
   Hello
   3
   Outside loop'''


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

#outputs
'''
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
Outside loop '''

 '''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]

6) Hint: Use  for  loop
'''

Enter any list: [10,20,15,12,18]
Enter the element to be searched : 15
Found  at   index  :   2

Enter any list: [25,10.8,'Hyd',True]
Enter the element to be searched : 3+4j
Not  Found

#Program
list=list(eval(input("Enter the elements into list:")))
n=eval(input("Enter the element to be searched:"))
for i in range(len(list)):
    if(list[i]==n):
        print("Found at index:",i)
        break
else:
    print("Not Found")



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

list=list(eval(input("Enter the elements into list:")))
n=eval(input("Enter the element to be searched:"))
print(type(list))
c=0
for i in range(len(list)):
    if(list[i]==n):
        print("Found at index:",i)
        c+=1
print(f'{n} is found {c} times')


#  Walrus   operator (:=)  demo  program
print(a := 25) -->25
print(a = 25) --> Error
print(a) -->25
print(a := 6 + 7) -->13
print(a) #13
print((a := 6) + 7) #13
print(a) #6
print((a = 6) + 7) #Error


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
if  c = 0:--------------------->Error
	print('Hyd')
else:
	print('Sec')


(Home  work)
Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z
(without  walrus  operator)

Let  inputs  be  25 , 10.8 , True ,  ctrl + z

#Program

sum=0
c=0
try:
    while True:
        n=eval(input("Enter input (ctrl+z to stop):"))
        sum+=n
        c+=1
except:
    print(f'Average of the inputs is :{sum/c}')


#  del  operator  demo program  (Home  work)
a = 25
print(a) #25
del   a
print(a) #Error


 # Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) # 25 25 25
del   a
print(b , c) #25 25
print(a) #Error
del   b
print(c) #25
print(b) #Error
del   c 
print(c) #Error

 #  Can  multiple  objects  be  deleted  with  same  del  operator ? #Yes
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c 
print(a) #Error
print(b) #Error
print(c) #Error

# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10,20,15,18]
del  a[2]
print(a) [10,20,18]
del  a
print(a)#Error
print(a[0]) #Error

# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) #(10,20,15,18)
print(a[0])#10
del  a[2] 
del  a
print(a)#Error
print(a[0])#Error