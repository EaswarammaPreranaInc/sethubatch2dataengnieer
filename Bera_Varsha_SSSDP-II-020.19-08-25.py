'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once

a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	while i:= a . index(15,i+1):
		print(i)
except:
	print(F'15  is  found  {a . count(15)}  times ')
output:
15  is  found  3  times  
Write  a  program  to  determine  first  list  is  a  sublist  of  2nd  list  or  not.
Print  True  if  it  is  a  sublist  and  False  otherwise


f_list=eval(input("Enter the list elements"))
s_list=eval(input("Enter the sub list"))
pos=0
result= True
for i in f_list:
    try:
        pos=s_list.index(i,pos)+1
    except ValueError:
        result=False
        break
print(result)

output:
Enter the list elements [10 , 20 , 30]
Enter the sub list[15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
True
Enter the list elements[10 , 20 , 20]
Enter the sub list[15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 ,  16]
False

# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)#[10,20,15,18]
print(a  is  b)#False
print(a  ==  b)#True
c = a[:]
print(c)#[10,20,15,18]
print(a  is  c)#False
print(a  ==  c)#True
d = a
print(d)#[10,20,15,18]
print(a  is  d)#True
print(a  ==  d)#True

#Write  a  program  to  determine  mode

list1=  [12,20,18,15,10,15,10,15,20,18,15,10,20,15,10]
mode=None
cou=0
for i in set(list1):
    count=list1.count(i)
    print(f'{i}is repeated  {count} times')
    if count>cou:
        cou=count
        mode=i
print('mode=', mode)
print('count=' ,cou)
    
output:
10is repeated  4 times
12is repeated  1 times
15is repeated  5 times
18is repeated  2 times
20is repeated  3 times
mode= 15
count= 5

#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)#[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))#3
print(a[0])#[10,20,30,40]
print(a[1])#[50,60,70,80]
print(a[2])#[90,100,110,120]
print(a[0][2])#30
print(a[1][3])#80
print(a[2][1])#100



What  is  a  nested  list ?  --->  A  list  in  another  list




#  Find  outputs  (Home  work)
a=[[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])
print(a[1])
print(a[2])
print(*a[0])
print(*a[1])
print(*a[2])
print(len(a[0]))

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x in  a:
    print(x)
print()
for  x,y  in  a:
	print(x,y,sep='...')

output:
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80

#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x,y,z,sep = '...')

output:
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90

#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x,y,sep = '...')#error
	
output:
[10, 20]
[30, 40, 50]
[60, 70, 80, 90]
10...20 

#  Find  outputs  (Home  work)
a = [[]]
print(a[0])#[]
print(*a)#[]

#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))#[[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]
print(sorted(a , reverse = True))#[[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]
print(a)#[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]'''