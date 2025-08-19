# program  with  walrus  operator
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	while (i:=a.index(15,i+1)):
		print(i)
except:
	print(F'15 is found {a.count(15)} times ')

# program to determine first list is a sublist of 2nd list or not. Print True if it is a sublist and False otherwise
x=eval(input("enter 1st list: "))
y=eval(input("enter 2nd list: "))
i=-1
z=True
for a in x:
    try:
        i=y.index(a,i+1)
    except ValueError:          
        z = False
        break
print(z)
'''
output:
enter 1st list: [10,20,30]
enter 2nd list: [10,20,40,30,50]
True
'''

# copy()  method  
a = [10 , 20 , 15 , 18]
b = a . copy() # returns a new list 'b' with same elements as 'a'
print(b) # [10,20,15,18]
print(a  is  b) # False
print(a  ==  b) # True
c = a[:] # copy list elements to another list
print(c) # [10,20,15,18]
print(a  is  c) # False
print(a  ==  c) # True
d = a
print(d) # [10,20,15,18]
print(a  is  d) # True
print(a  ==  d) # True

#program to determine mode
x=eval(input("enter any list: "))
ctr=0
for i in x:
    a=x.count(i)
    if a>ctr:
        ctr=a
print('Mode :',i)

#  Nested  List  
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a) # [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a)) # 3
print(a[0]) # [10, 20, 30, 40] : print  1st  inner  list
print(a[1])  #  [50, 60, 70, 80] : print  2nd  inner  list
print(a[2]) # [90, 100, 110, 120] : print  3rd  inner  list
print(a[0][2]) # 30
print(a[1][3])  # 80
print(a[2][1])  # 100


#  Find  outputs  
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0]) # [10,20] :print  1st   inner  list
print(a[1]) # [30,40,50]  print  2nd   inner  list
print(a[2]) # [60,70,80,90] print  3rd   inner  list
print(len(a[0])) # 2 : print  number  of  elements  in  1st  inner  list
print(len(a[1])) # 3 : print  number  of  elements  in  2nd  inner  list
print(len(a[2])) # 4 : print  number  of  elements  in  3rd  inner  list

# print nested list in different ways
a=[[10,20],[30,40,50],[60,70,80,90]]
print(a[0]) # [10, 20]
print(a[1]) # [30, 40, 50]
print(a[2]) # [60, 70, 80, 90]
print(*a) # [10, 20] [30, 40, 50] [60, 70, 80, 90] : each inner list of outer list without indexes
for x in a:
    print(x) # [10,20] <next line> [30,40,50] <next line> [60,70,80,90] : print each inner list of list 'a'

# print elements of each inner list without using indexes in matrix style
for x in a:
    for y in x:
        print(y,end=' ')
    print() # print elements of each inner list without using indexes in matrix style
'''
output:
10 20
30 40 50
60 70 80 90 
'''

# Elements in the form of matrix using indexes
for i in range(len(a)):              
    for j in range(len(a[i])):      
        print(a[i][j], end=' ')
    print()
'''
output:
10 20
30 40 50
60 70 80 90 '''

#print elements of each inner list using indexes in matrix style(using nested loop)
for i in a[0:len(a)+1]:              
    for j in i[0:len(i)+1]:      
        print(j, end=' ')
    print()
'''
output:
10 20
30 40 50
60 70 80 90'''

#  Find  outputs 
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)
print() 
for  x , y  in  a:
	print(x , y , sep = '...')
'''
output:
[10, 20]
[30, 40]
[50, 60]
[70, 80]

10...20
30...40
50...60
70...80
'''

#  Find  outputs 
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)
print()
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')
'''
output:
[10, 20, 30]
[40, 50, 60]
[70, 80, 90]

10...20...30
40...50...60
70...80...90'''

'''
#  Find  outputs 
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)
for  x , y  in  a:
	print(x , y ,	sep = '...')  # ValueError : too many values to unpack
'''

#  Find  outputs 
a = [[]]
print(a[0])  # [] :print  inner  list
for x in a:
    print(x) # []

#  Find  outputs  
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a)) # [[5, 'Amar', 5000.0], [10, 'Rama', 1000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [20, 'Sita', 2000.0]]   
print(sorted(a , reverse = True)) #  [[20, 'Sita', 2000.0], [18, 'Kiran', 2800.0], [15, 'Rajesh', 3500.0], [10, 'Rama', 1000.0], [5, 'Amar', 5000.0]]   
print(a) # [[10, 'Rama', 1000.0], [20, 'Sita', 2000.0], [15, 'Rajesh', 3500.0], [18, 'Kiran', 2800.0], [5, 'Amar', 5000.0]]   

