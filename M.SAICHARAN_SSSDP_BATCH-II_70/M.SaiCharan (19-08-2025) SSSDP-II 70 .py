                        NAME:M.SAICHARAN                    HOMEWORK
                        DATE:19-08-2025 


1.'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')
#program:
a = [10, 20, 15, 12, 14, 15, 18, 19, 15, 12, 25]
i = -1
count = 0
while True:
    try:
        print(i := a.index(15, i + 1))
        count += 1
    except ValueError:
        break
print(f'15 is found {count} times')



2.'''
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
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''
Enter  the  first  list :  [10 , 20 , 30]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
True

Enter  the  first  list : [10 , 20 , 20]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
False

#program:
first = eval(input("Enter first list : "))
second = eval(input("Enter second list : "))
try:
    for num in first:
        index = second.index(num)   
        second = second[index+1:]   
    print(True)
except ValueError:
    print(False)





3.# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)		#[10, 20, 15, 18]
print(a  is  b)		#False
print(a  ==  b)		#True
c = a[:]
print(c)		#[10, 20, 15, 18]
print(a  is  c)		#False
print(a  ==  c)		#True
print(d)		#[10, 20, 15, 18]
print(a  is  d)		#True
print(a  ==  d)		#True


'''
copy()  method
------------------
1) What  does  copy()  method  do ? --->  Returns  a  new  list  with  same  elements

2) b = a . copy()
    What  is  another  way  to  copy  list  elements  to  another list ?  --->  b = a[:]
'''
4.'''
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
Enter  List  :   [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode :  15

#program:
a  = eval(input("Enter a list :"))
mode = 1
max_count = 0
for num in set(a):  
    count = a.count(num) 
    if count > max_count:   
        max_count = count
        mode = num
print("Mode :", mode)
print("Count :", max_count)


5.#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)					#[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))					#3
print(How  to  print  1st  inner  list)		#print (a[0])
print(How  to  print  2nd  inner  list)		#print (a[1])
print(How  to  print  3rd  inner  list)		#print (a[2])
print(How  to  print  30)			#print (a[0][2])
print(How  to  print  80)			#print (a[1][3])
print(How  to  print  100)			#print (a[2][1])


'''
What  is  a  nested  list ?  --->  A  list  in  another  list
'''

6.#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)				#print(a[0])
print(How  to  print  2nd   inner  list)				#print(a[1])
print(How  to  print  3rd   inner  list)				#print(a[2])
print(How  to  print  number  of  elements  in  1st  inner  list)	#print(len(a[0]))
print(How  to  print  number  of  elements  in  2nd  inner  list)	#print(len(a[1]))
print(How  to  print  number  of  elements  in  3rd  inner  list)	#print(len(a[2]))



7.#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(???)#print(a)
print('Each  inner  list   of   outer  list  without  indexes')#for inner in a:
                                                                 print(inner)

How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
       #for inner in a:
    for val in inner:
        print(val, end="   ")
    print()

How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
      #for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j], end="   ")
    print()
How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)s
'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''


8.#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')
#output:
[10 , 20]
[30 , 40]
[50 , 60]
[70 , 80]

10...20
30...40
50...60
70...80


9.#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
#output:
[10 , 20 , 30]
[40 , 50 , 60]
[70 , 80 , 90]

10...20...30
40...50...60
70...80...90



10.#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:                     #Error
	print(x , y ,	sep = '...')
#output:
[10 , 20]
[30 , 40 , 50] 
[60 , 70 , 80 , 90]]


11.#  Find  outputs  (Home  work)
a = [[]]
print(How  to  print  inner  list)			#print(a[0])
print(How  to  print  inner  list  in  another  way)	#usingloops



12.#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))			#[ [5 , 'Amar'  ,5000.0] , [10 , 'Rama' , 1000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [20 , 'Sita' , 2000.0]]
print(sorted(a , reverse = True))	#[[20 , 'Sita' , 2000.0] ,[18 , 'Kiran' , 2800.0] , [15 , 'Rajesh' , 3500.0] ,[10 , 'Rama' , 1000.0] , [5 , 'Amar'  ,5000.0]]
print(a)				# [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0]]