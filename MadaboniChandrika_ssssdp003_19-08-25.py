#1st program

'''
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

#Modified
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = 2
	while  True:
		print(i)
		(i := a . index(15 , i + 1))
except:
	print(F'15  is  found  {a . count(15)}  times ')


#2nd program
# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()
print(b)#[10 , 20 , 15 , 18]
print(a  is  b)#False 
print(a  ==  b)#True 
c = a[:]
print(c)#[10 , 20 , 15 , 18]
print(a  is  c)#True 
print(a  ==  c)#True 
d = a
print(d)#[10 , 20 , 15 , 18]
print(a  is  d)#True 
print(a  ==  d)#True 


# 3rd program
#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)#[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))#3
print(How  to  print  1st  inner  list)#print(a[0])
print(How  to  print  2nd  inner  list)#print(a[1])
print(How  to  print  3rd  inner  list)#print(a[2])
print(How  to  print  30)#print(a[0][2])
print(How  to  print  80)#print(a[1][3])
print(How  to  print  100)#print(a[2][1])


#4th program
#  Find  outputs  (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(How  to  print  1st   inner  list)#print(a[0])
print(How  to  print  2nd   inner  list)#print(a[1])
print(How  to  print  3rd   inner  list)#print(a[2])
print(How  to  print  number  of  elements  in  1st  inner  list)#print(len(a[0])
print(How  to  print  number  of  elements  in  2nd  inner  list)#print(len(a[1])
print(How  to  print  number  of  elements  in  3rd  inner  list)#print(len(a[2])


# 5th program
#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)
print('Each  inner  list   of   outer  list  without  indexes')
for x in a:
	print(x)
print('Elements  in  the  form   of  matrix   without  using  indexes')
for x in a:
    for y in x:
        print(y , end = ' ')
    print()
print('Elements  in  the  form   of  matrix  using  indexes')
for i in range(len(a)):
    for j in range(len(a[i])):
        print(a[i][j] , end = ' ')
    print()


# 6th program
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print()
for  x , y  in  a:
	print(x , y , sep = '...')

Output:
[10,20]
[30,40]
[50,60]
[70,80]

[10...20]
[30...40]
[50...60]
[70...80]



#7th program
#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')

Output:
[10 , 20 , 30]
[40 , 50 , 60]
[70 , 80 , 90]

[10...20...30]
[40...50...60]
[70...80...90]


#8th program
#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')

# Output:

[10 , 20]
[30 , 40 , 50]
[60 , 70 , 80 , 90]

[10...20]
[30...40...50]
[60...70...80...90]



# 9th program
#  Find  outputs  (Home  work)
a = [[]]
print(How  to  print  inner  list)#print(a[0])
print(How  to  print  inner  list  in  another  way) # print(*a)


# 10th program
#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))#[[5 , 'Amar'  ,5000.0],[10 , 'Rama' , 1000.0],[15 , 'Rajesh' , 3500.0],[18 , 'Kiran' , 2800.0],[20 , 'Sita' , 2000.0]]
print(sorted(a , reverse = True))#[[20 , 'Sita' , 2000.0],[18 , 'Kiran' , 2800.0],[15 , 'Rajesh' , 3500.0],[10 , 'Rama' , 1000.0],[5 , 'Amar'  ,5000.0]]
print(a)#[[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]



# 11th program
# Program to determine mode
a =eval(input('Enter a list: '))

mode = None
max_count = 0

for x in set(a):
    count = a.count(x)
    if count > max_count:
        max_count = count
        mode = x

print(f"mode = {mode}")


