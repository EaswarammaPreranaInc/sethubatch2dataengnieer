
'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	while (i := a . index(15, i + 1)) == True:
		print(i)
except:
	print(F'15  is  found  {a . count(15)}  times ')

'''output:
   15  is  found  3  times
'''

'''
Most   tricky  program
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise

1) First  list :  [10 , 20 , 30]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  --->  True  becoz  elements  10 , 20 , 30  are  in  2nd  list  in  same  order

2) First  list :  [10 , 20 , 20]
    Second  list :  [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
    What  is  the  output ?  ---> False  becoz   elements  10 , 20 , 30  are  not  in  2nd  list

3) First  list :  [2 , 2 , 5]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in   [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''
a=eval(input('Enter  the  first  list :'))
b=eval(input('Enter  the  second  list :'))
try:
	i=-1
	for x in a:
		i = b.index(x,i + 1)
	print('True')
except:
	print('False')	
	
'''
# Output:

Enter  the  first  list :  [10 , 20 , 30]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
True

Enter  the  first  list : [10 , 20 , 20]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
False
'''



# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18] 
b = a . copy() #Here copy method is used to copy the list of original list #Deep copy
print(b) #Returns the copied list i.e [10 , 20 , 15 , 18] 
print(a  is  b) #Returns False 
print(a  ==  b) #Returns True where elements are compared  
c = a[:] #Make a shallow copy of a into c
print(c) #Returns the list [10 , 20 , 15 , 18] 
print(a  is  c) #Returns False 
print(a  ==  c) #Returns True
d = a #Reference d points to a 
print(d) #Returns the list a i.e [10 , 20 , 15 , 18]
print(a  is  d) #Returns True
print(a  ==  d) #Returns True


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Returns  a  new  list  with  same  elements

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  b = a[:]
'''



'''
Tricky  program
Write  a  program  to  determine  mode

1) What  is  mode ?  ---> The  element  which  is  repeated  maximum  number  of  times  in  the  list

2) Let  input  be  [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
    What  is  set(list) ?  ---> {12 , 20 , 18 , 15 , 10}
    How  many  times  is  first  element  12  repeated  in  the  list  ?  --->  1
    How  many  times  is  2nd  element  20  repeated  in  the  list  ?  --->  3
    How  many  times  is  3rd  element  18  repeated  in  the  list  ?  --->  2
    How  many  times  is  4th  element  15  repeated  in  the  list  ?  --->  5
    How  many  times  is  last  element  10  repeated  in  the  list  ?  --->  4
    What  is  the  mode  ?  --->	15  becoz  it  is  repeated  max  number  of  times  i.e.  5

3) mode = 15
    ctr = 5
'''
'''Enter  List  :   [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode :  15
'''

n = eval(input("Enter the list: "))
max = 0
for i in n:
    c = n.count(i)
    if c > max:
        max = c
        mode = i
print(f"mode = {mode} and ctr = {max}")

'''output:
Enter the list: [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
mode = 15 and ctr = 5
'''



#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) #Returns the list a i.e [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) #Returns the length of list i.e 3
print(a[0]) #print(How  to  print  1st  inner  list)
print(a[1]) #print(How  to  print  2nd  inner  list)
print(a[2]) #print(How  to  print  3rd  inner  list)
print(a[0][2])#print(How  to  print  30)
print(a[1][3])#print(How  to  print  80)
print(a[2][1])#print(How  to  print  100)


'''
What  is  a  nested  list ?  --->  A  list  in  another  list
'''


#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])  #print(How  to  print  1st   inner  list) 
print(a[1])  #print(How  to  print  2nd   inner  list)
print(a[2])  #print(How  to  print  3rd   inner  list)
print(len(a[1]))  #print(How  to  print  number  of  elements  in  2nd  inner  list)
print(len(a[2]))   #print(How  to  print  number  of  elements  in  3rd  inner  list)



#  How  to  print  nested  list  in  differnent  ways

a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function') 
print(a) # Output:[[10, 20], [30, 40, 50], [60, 70, 80, 90]]

print('Each  inner  list   of   outer  list  without  indexes') 
for x in a:#How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
	print(x)
'''
# Output:
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
'''
print('Elements  in  the  form   of  matrix   without  using  indexes') 
for i in a:#How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
	for j in i:
		print(j,end='   ')
	print()
'''
# Output:
10   20
30   40   50
60   70   80   90
'''
print('Elements  in  the  form   of  matrix  using  indexes') 
for i in range(len(a)):#How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)
	for j in range(len(a[i])):
		print(a[i][j],end='   ')
	print()
'''
# Output:
10   20
30   40   50
60   70   80   90
'''





#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')

'''output
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80'''


#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

'''output:
[10 , 20 , 30]
[40 , 50 , 60]
[70 , 80 , 90]
next line
10...20...30
40...50...60
70...80...90
'''


#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')
	
'''output:
1st loop will executes sucessfully
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
10...20
#when it comes to second loop it executes 1st iteration where 1st list have 2 elements and when it comes to 2nd iteration it raises error because there more than 2 elements as we are using only 2 variables i.e x,y
'''



#  Find  outputs  (Home  work)
a = [[]]
print(a[0])  #print(How  to  print  inner  list)
print(*a)    #print(How  to  print  inner  list  in  another  way)



#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) #It compares the 0 index of inner list with all other inner lists and returns in ascending order i.e [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True)) #Here list is sorted and returns in reverse order i.e [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a) #Returns the original list i.e [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]