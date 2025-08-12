for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')  
# End of loop
print('Outside loop')   
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello<nL> 3 <nl> 4 <nl> Sec <nl> Hello
<nl> 5  <nl> Sec <nl> Hello <nl> 6 <nl> Sec <nl> Hello <nl> 7 <nl> Sec <nl> Hello <nl> Outside loop

 # Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')   #  'continue' not in if its only in loop
 # Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')  # 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello<nL> 3 <nL> Outside loop

# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec') #oustside loop

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
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello<nL> 3 <nl> Hyd <nl> Hello <nl> 4 <nl> Sec <nl> Hello <nl> 5  <nl> Sec <nl> Hello <nl> 6 <nl> Sec <nl> Hello <nl> 7 <nl> Sec <nl> Hello <nl> Outside loop

 # Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		exit() # terminates the excution of program (interpreter terminates)
	else:
		print('Sec')
	print('Hello')
# End  of  the  loop
print('Outside loop')
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello<nL> 3 <nL> Outside loop

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
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello<nL> 3 <nl> 4 <nl> Sec <nl> Hello
<nl> 5  <nl> Sec <nl> Hello <nl> 6 <nl> Sec <nl> Hello <nl> 7 <nl> Sec <nl> Hello<nl> else  suite <nl> Outside loop

 # Find  outputs  (Home  work)
 #else cause is executed only if the loop completes normally
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
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello<nL> 3 <nL> Outside loop


[11:30 am, 4/8/2025] +91 99482 50500: # Find  outputs  (Home  work)
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
# 1 <nl> Sec <nl> Hello <nl> 2 <nl> Sec <nl> Hello<nL> 3 <nl> Sec<nl> Hello <nl> 4 <nl> Sec <nl> Hello<nl> 5  <nl> Sec <nl> Hello <nl> 6 <nl> Sec <nl> Hello <nl> 7 <nl> Sec <nl> Hello<nl> else  suite <nl> Outside loop

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

[11:41 am, 4/8/2025] +91 99482 50500: Enter any list: [10,20,15,12,18]
Enter the element to be searched : 15
Found  at   index  :   2
[11:42 am, 4/8/2025] +91 99482 50500: Enter any list: [25,10.8,'Hyd',True]
Enter the element to be searched : 3+4j
Not  Found
a=[10,20,15,12,18]
flag=False
b=0
search=eval(input("enter a searching value: "))
for i in range(len(a)):
    if a[i]==search:
        flag=True
        b=i
        break
if flag==True:
    print("index is :",b)
else:
    print("not found")
		
if search in a:
    print("index is :",a.index(search))
else:
    print("not found")
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
a=[10,20,15,12,18,15]
flag=False
count=0
search=eval(input("enter a searching value: "))
for i in range(len(a)):
    if a[i]==search:
        count+=1
        flag=True
        print("index is :",i)
if flag==True:
    print(f"{search} occur {count} times")
else:
    print("not found")
#  Walrus   operator (:=)  demo  program
print(a := 25) # 25
print(a = 25) # a invalid
print(a) # 25
print(a := 6 + 7) # 13
print(a) #13
print((a := 6) + 7) # 13
print(a) #6
print((a = 6) + 7) # a not define

 # Find  outputs  (Home  work)
a = 0
if  a == 0:
	print('Hyd') # Hyd
else:
	print('Sec')
if  b := 0:
	print('Hyd')
else:
	print('Sec : ' , b) # Sec: 0
if  c = 0:  # not define c
	print('Hyd') 
else:
	print('Sec')

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
[12:10 pm, 4/8/2025] +91 99482 50500: Enter input  (ctrl + z  to  stop)  :  25
Enter input  (ctrl + z  to  stop)  :  10.8
Enter input  (ctrl + z  to  stop)  :  True
Enter input  (ctrl + z  to  stop)  :  36.9
Enter input  (ctrl + z  to  stop)  :  45
Enter input  (ctrl + z  to  stop)  :  False
Enter input  (ctrl + z  to  stop)  :  92.8
Enter input  (ctrl + z  to  stop)  :  ^Z
Average :   30.214285714285715


a=0;cnt=0
while True:
    try:
        val=eval(input("enter a number:"))
        cnt+=1
        a+=val
    except:
        break
if cnt > 0:
    print("Average :",a, cnt,a/cnt)
else:
    print("No valid inputs were provided.")

    
    
 #  del  operator  demo program  (Home  work)
a = 25
print(a) # 25
del   a
print(a) # a not define
 # Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c) 25 25 25
del   a
print(b , c) 25 25 
print(a) #not define
del   b 
print(c) # 25
print(b) #not define
del   c
print(c) # not define
#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'
print(a , b , c) # 25 10.8 Hyd
del   a , b , c
print(a)  # not define
print(b)# not define
print(c) # not define
 # Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a) #[10 , 20 , 15 , 18]
del  a[2]
print(a) [10,20,18]
del  a
print(a) # not define
print(a[0]) # not define
[12:19 pm, 4/8/2025] +91 99482 50500: # Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a) #(10 , 20 , 15 , 18)
print(a[0]) # 10
del  a[2] # not possibe
del  a
print(a) # not define
print(a[0]) #not define
