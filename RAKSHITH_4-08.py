# Find  outputs  (Home  work)

for  i   in   range(1 , 8):
	print(i)        #1<nextline>sec<nextline>Hello<nextline>2<nextline>sec<nextline>Hello<nextline>3<nextline>4<nextline>sec
	if  i % 3  == 0: #Hello<nextline>5<nextline>sec<nextline>Hello<nextline>6<nextline>7<nextline>sec<nextline>Hello<nextline>
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')       #Outside loop

# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue        #Error 'continue'  can be used only with while and for loops.
	print('Sec')
    

# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)        #1<nextline>sec<nextline>Hello<nextline>2<nextline>sec<nextline>Hello
	if   i % 3 == 0: #<nextline>3<nextline>Outside loop
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')    #break only used with while and for loops
	break
	print('Sec')
    

# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)            #1<nextline>sec<nextline>Hello<nextline>2<nextline>
	if   i % 3 == 0:    #sec<nextline>Hello<nextline>3<nextline>Hyd<nextline>sec<nextline>
		pass            #Hello<nextline>4<nextline>sec<nextline>Hello<nextline>5<nextline>sec<nextline>
		print('Hyd')    #Hello<nextline>6<nextline>Hyd<nextline>sec<nextline>Hello<nextline>
	else:               #7<nextline>sec<nextline>Hello<nextline>outside loop
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')


# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)            #1<sec<nextline>Hello<nextline>2<nextline>Sec<nextline>Hello<nextline>3
	if   i % 3 == 0:
		exit()
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)        #1<nextline>sec<nextline>Hello<nextline>2<nextline>sec<nextline>Hello<nextline>
	if   i % 3 == 0: #3<nextline>4<Nextline>sec<nextline>Hello<nextline>5<nextline>sec<nextline>Hello<nextline>
		continue     #6<nextline>7<nextline>sec<nextline>Hello<nextline>else suite<nextline>
	else:            #outside loop
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside  loop')


 # Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)            #1<nextline>sec<nextline>Hello<nextline>2<nextline>sec<nextline>Hello
	if  i % 3 == 0:     #3<nextline>Outside loop
		break
	else:
		print('Sec')
	print('Hello')
else:
	print('else  suite')
#End   of  the  loop
print('Outside  loop')


 # Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)      #1<nextline>sec<nextline>Hello<nextline>2<nextline>sec<nextline>Hello<nextline>
	if  i == 8:   #3<nextline>sec<nextline>Hello<nextline>4<nextline>sec<nextline>Hello<nextline>
		break     #5<nextline>sec<nextline>Hello<nextline>6<nextline>sec<nextline>Hello<nextline>
	else:         #7<nextline>sec<nextline>Hello<nextline>else suite<nextline>Outside loop
		print('Sec')
	print('Hello')
else:
	print('else  suite')
# End  of  the  loop
print('Outside loop')


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


Enter any list: [10,20,15,12,18]
Enter the element to be searched : 15
Found  at   index  :   2
Enter any list: [25,10.8,'Hyd',True]
Enter the element to be searched : 3+4j
Not  Found


a=eval(input('Enter any list: '))
x=int(input('Enter the element to be searched : '))
for i in range(len(a)):
    if x==a[i]:
        print(f"Found at index : {i}")
        break
else:
    print("Not Found")




Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  element
and  also  number  of  times  it  is  found (Assume  that  list  may  contain  duplicate  elements)

List :   [10 , 20 , 15 , 12 , 18 , 15 , 19 , 14 , 15 , 14]

Search  for  15

Outputs :  15  is  found  at  index  2
                 15  is  found  at  index  5
                 15  is  found  at  index  8
                 15  is  found   3  times


a=eval(input('Enter a list: '))
x=int(input('Enter the element to be searched : '))
count =0
for i in range(len(a)):
    if x ==a[i]:
        print(f"{a[i]} is found at index {i}")
        count +=1
        
print(f"{x} is found {count } times")


#  Walrus   operator (:=)  demo  program
print(a := 25)  #25 -->25 is assigned to reference a 
#print(a = 25)   #nothing error  unexpected argument 'a'
print(a)        #25
print(a := 6 + 7)   #13
print(a)            #13
print((a := 6) + 7) # 13
print(a)            #6
#print((a = 6) + 7)  #error


# Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd')    #Hyd
else:
	print('Sec')
if  b := 0:         
	print('Hyd')    
else:
	print('Sec : ' , b) #sec : 0
if  c = 0:
	print('Hyd')    #c is not defined error
else:
	print('Sec')    #sec
    
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

Enter input  (ctrl + z  to  stop)  :  25
Enter input  (ctrl + z  to  stop)  :  10.8
Enter input  (ctrl + z  to  stop)  :  True
Enter input  (ctrl + z  to  stop)  :  36.9
Enter input  (ctrl + z  to  stop)  :  45
Enter input  (ctrl + z  to  stop)  :  False
Enter input  (ctrl + z  to  stop)  :  92.8
Enter input  (ctrl + z  to  stop)  :  ^Z
Average :   30.214285714285715

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





#  del  operator  demo program  (Home  work)
a = 25
print(a)    #25
del   a     #delete reference a
print(a)    #error a is not defined


# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)    #25<nextline>25<nextline>25
del   a
print(b , c)        #25<nextline>25
print(a)            #error reference a is not defined
del   b
print(c)            #25
print(b)            #error reference b is not defined
del   c
print(c)            #error reference c is not defined


#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c)    #25<nextline>10.8<nextline>Hyd
del   a , b , c
print(a)            #Error reference a is not defined
print(b)            #Error reference b is not defined
print(c)            #Error reference c is not defined


# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)        # [10 , 20 , 15 , 18]
del  a[2]       # delete the element at index 2
print(a)        #[10 , 20 , 18]
del  a
print(a)        #error a is not defined 
print(a[0])     #error a is not defined


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)        #(10 , 20 , 15 , 18)
print(a[0])     #10
del  a[2]       #error tuple is immutable 
del  a          #error tuple is immutable
print(a)        # error a is not defined
print(a[0])     # error a is not defined