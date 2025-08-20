#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)#[10,20,30,40,50,60,70,80]
print()#empty list
for  x , y  in  a:
	print(x , y , sep = '...')#[10,20]...[30,40]...[50,60]...[70,80]...

 #  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)#[10 , 20 , 30,40 , 50 , 60,70 , 80 , 90]
print()#[]
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')#[10 , 20 , 30] ...[40 , 50 , 60] ...[70 , 80 , 90]...


 #  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)#[10 , 20 ,30 , 40 , 50,60 , 70 , 80 , 90]
for  x , y  in  a:
	print(x , y ,	sep = '...')#[[10 , 20] ...[30 , 40 , 50] ... [60 , 70 , 80 , 90]]

#  Find  outputs  (Home  work)
a = [[]]
print(How  to  print  inner  list)#using for loop
print(How  to  print  inner  list  in  another  way)#using * operator,it will unpack the elements 


#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))#[[5 , 'Amar'  ,5000.0,[10 , 'Rama' , 1000.0],[15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , [20 , 'Sita' , 2000.0]]'
print(sorted(a , reverse = True))#[20 , 'Sita' , 2000.0],[18 , 'Kiran'],,[15 , 'Rajesh' , 3500.0],))[5 , 'Amar'  ,5000.0]]
print(a)#[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)#[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))#3
print(How  to  print  1st  inner  list)#a[0]
print(How  to  print  2nd  inner  list)#a[1]
print(How  to  print  3rd  inner  list)#a[2]
print(How  to  print  30)#a[0][2]
print(How  to  print  80)#a[1][3]
print(How  to  print  100)#a[2][1]




 #  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)#a[0]
print(How  to  print  2nd   inner  list)#a[1]
print(How  to  print  3rd   inner  list)#a[2]
print(How  to  print  number  of  elements  in  1st  inner  list)#print(len(a))

print(How  to  print  number  of  elements  in  2nd  inner  list)#print(len(a[1]))
print(How  to  print  number  of  elements  in  3rd  inner  list)#print(len(a[2]))

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)# [10 , 20 , 15 , 18]
print(a  is  b)#false
print(a  ==  b)#true
c = a[:]
print(c)#[10 , 20 , 15 , 18]
print(a  is  c)#false
print(a  ==  c)#true
d = a
print(d)#[10 , 20 , 15 , 18]
print(a  is  d)#false
print(a  ==  d)#true

'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
i=-1
try:
	while i := a . index(15 , i + 1):
		print(i)
		
except:
	print(F'15  is  found  {a . count(15)}  times ')



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

a = input("Enter 1st list: ").split()
b = input("Enter 2nd list: ").split()

try:
    i = b.index(a[0])   
    if b[i:i+len(a)] == a:
        print("true")
    else:
        print("not identical")
except ValueError:
    print("not identical")

a = [10, 20, 15, 10, 14, 10, 18, 20, 19]
mode = None
max_count = 0

for i in a:
    if a.count(i) > max_count:   
        max_count = a.count(i)
        mode = i                
print("Mode:", mode)
print("Count:", max_count)

#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')#
print(???)#print(a[: :,1]
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

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]

for row in a:
    print(row)
    #print(row[0],end=",")