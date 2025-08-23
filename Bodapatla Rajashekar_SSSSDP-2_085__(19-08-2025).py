'''
#1
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
	print(F'15  is  found  {a . count(15)}  times ')'''
	
a =eval(input("enter the list:"))

try:
    i = -1   
    while (i := a.index(15, i + 1)) >= 0:
        print(i)
except ValueError:
    print(f'15 is found {a.count(15)} times')

#2
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
    What  is  the  output ?  --->  True  becoz   elements  2 , 2 , 5  are  in  [2 , 2 , 3 , 4 , 5]

4) First  list :  [2 , 4 , 3]
    Second  list :  [2 , 2 , 3 , 4 , 5]
    What  is  the  output ?  --->  False  becoz   elements  2 , 4 , 3   are  not  in  [2 , 2 , 3 , 4 , 5]

5) Hint:  Use  index()  method
'''
a=eval(input("enter the 1 list:"))
b=eval(input("enter the  2nd list:"))




pos = -1   
result = True

try:
    for i in a:
        pos = b.index(i, pos + 1)   # search next occurrence after 'pos'
except ValueError:
    result = False

print(result)

#3
# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)             #[10 , 20 , 15 , 18]
print(a  is  b)      #False
print(a  ==  b)      #True
c = a[:]
print(c)             #[10 , 20 , 15 , 18]
print(a  is  c)       #False
print(a  ==  c)       #True
d = a
print(d)             #[10 , 20 , 15 , 18]
print(a  is  d)      #True
print(a  ==  d)      #False


'''

#4
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

a=eval(input("enter the  list:"))
b=set(a)
ctr=0
mode=0

for i in b:
    if a.count(i)>ctr:
        ctr=a.count(i)
        mode=i
print(f'mode:',mode)
print(f'counter:',ctr)



#5
#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)                                 #[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))                            #3
print(How  to  print  1st  inner  list)  #a[0]
print(How  to  print  2nd  inner  list)  #a[1]
print(How  to  print  3rd  inner  list)  #a[2]
print(How  to  print  30)          #a[0][2]
print(How  to  print  80)          #a[1][3] or a[1][-1]
print(How  to  print  100)         #a[2][1]


'''

#6
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)                            #a[0]
print(How  to  print  2nd   inner  list)                            #a[1]
print(How  to  print  3rd   inner  list)                            #a[2]
print(How  to  print  number  of  elements  in  1st  inner  list)   #len(a[0])
print(How  to  print  number  of  elements  in  2nd  inner  list)   #len(a[1])
print(How  to  print  number  of  elements  in  3rd  inner  list)   #len(a[2])


#7
#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')   
print(???)
print('Each  inner  list   of   outer  list  without  indexes')
How  to  print  each  inner  list  of  list  'a'  without  using  indexes  (use  for  loop)
print('Elements  in  the  form   of  matrix   without  using  indexes')
How  to   print  elements  of  each  inner  list  without  using  indexes  in  matrix style  (use  nested  loop)
print('Elements  in  the  form   of  matrix  using  indexes')
How  to   print  elements  of  each  inner  list  using  indexes  in  matrix style (use  nested  loop)



'''
matrix   style
----------------
10    20
30    40   50
60    70   80   90
'''


a = [[10, 20], [30, 40, 50], [60, 70, 80, 90]]

print(a)     #[[10, 20], [30, 40, 50], [60, 70, 80, 90]]
for i in a:     
    print(i)


for i in a:      
    for j in i:  
        print(j, end="   ")
    print()           


for i in range(len(a)):        
    for j in range(len(a[i])):  
        print(a[i][j], end="   ")
    print()   


#8
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
'''
[10, 20]
[30, 40]
[50, 60]
[70, 80] '''

for  x , y  in  a:
	print(x , y , sep = '...')
	
'''
10...20
30...40
50...60
70...80
'''
#9
#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

'''
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90
'''

#10
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')
'''
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
10...20
ERROR


#11  Find  outputs  (Home  work)
a = [[]]                
print(How  to  print  inner  list)    #print(a[0])
print(How  to  print  inner  list  in  another  way)  #print(a[0][0])

#12
#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))  #[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True))  #[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a) #[[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]

