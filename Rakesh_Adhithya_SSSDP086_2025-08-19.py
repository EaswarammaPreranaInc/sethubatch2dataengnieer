'''
Modify  the  following  program  with  walrus  operator

Hint:  Call  index()  method  only  once
'''
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
try:
	i = -1
	while i := a . index(15 , i + 1):
		print(i)
except:
	print(F'15  is  found  {a . count(15)}times ')




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

5) Hint:  Use  index() method

Enter  the  first  list :  [10 , 20 , 30]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 , 16]
True

Enter  the  first  list : [10 , 20 , 20]
Enter  the  second  list : [15 , 18 , 10 ,  12 ,  19 , 20 , 14 , 12 , 30 , 25 , 16]
False
'''


list1 = eval(input('Enter the first list:  '))
list2 = eval(input('Enter the second list:  '))
i = -1
try:
    for x in list1:
        i = list2.index(x, i+1)
    print('True')
except ValueError:
    print('False')





# copy()  method  demo program  (Home  work)
a = [10 , 20 , 15 , 18]
b = a . copy()     #creates a copy of object a and ref b is assigned to it
print(b)           #[10, 20, 15, 18]
print(a  is  b)    #False
print(a  ==  b)    #True
c = a[:]           #slice returns a new object of same sequence
print(c)           #[10, 20, 15, 18]
print(a  is  c)    #False
print(a  ==  c)    #True
d = a              #shallow copy
print(d)           #[10, 20, 15, 18]
print(a  is  d)    #True
print(a  ==  d)    #True




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

Enter  List  :   [12 , 20 , 18 , 15 , 10 ,  15 , 10 ,  15 ,  20 , 18 , 15 , 10 , 20 , 15 , 10]
Mode : 15
'''
list = eval(input('Enter List:  '))
count = 0
mode = 0
for x in set(list):
    if list.count(x) > count:
        count = list.count(x)
        mode = x
print(f'Mode: {mode}')





#  Nested  List  demo  program  (Home  work)
a = [[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(a)         #[[10 , 20 , 30 ,  40]  ,  [50 , 60 ,  70 , 80]  ,  [90 , 100 , 110 , 120] ]
print(len(a))    #3
print(a[0])      #How  to  print  1st  inner  list
print(a[1])      #How  to  print  2nd  inner  list
print(a[2])      #How  to  print  3rd  inner  list
print(a[0][2])   #How  to  print  30
print(a[1][3])   #How  to  print  80
print(a[2][1])   #How  to  print  100




#  Find  outputs (Home  work)
a=[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
print(a[0])       #How  to  print  1st   inner  list
print(a[1])       #How  to  print  2nd   inner  list
print(a[2])       #How  to  print  3rd   inner  list
print(len(a[0]))  #How  to  print  number  of  elements  in  1st  inner  list
print(len(a[1]))  #How  to  print  number  of  elements  in  2nd  inner  list
print(len(a[2]))  #How  to  print  number  of  elements  in  3rd  inner  list








#  How  to  print  nested  list  in  differnent  ways
a = [[10 , 20] , [30 , 40 ,  50] , [60 , 70 , 80 , 90]]
print('Nested list  with  print function')
print(a)
print('Each  inner  list   of   outer  list  without  indexes')
for x in a:
    print(x, end=', ')
print()
print('Elements  in  the  form   of  matrix   without  using  indexes')
for row in a:
    for col in row:
        print(col, end=' ')
    print()
print('Elements  in  the  form   of  matrix  using  indexes')
for row in range(len(a)):
    for col in range(len(a[row])):
        print(a[row][col], end=' ')
    print()




#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40] , [50 , 60] , [70 , 80]]
for  x  in  a:
    print(x)                    #prints innerlist and moves to next line
print()                         #prints a new line
for  x , y  in  a:
	print(x , y , sep = '...')  #prints elements in innerlist with ... as separator



#  Find  outputs (Home  work)
a = [[10 , 20 , 30] , [40 , 50 , 60] , [70 , 80 , 90]]
for  x  in  a:
    print(x)                        #prints innerlist and moves to next line
print()                             #prints a new line
for  x , y ,  z  in   a:
	print(x , y , z , sep = '...')  #prints elements in innerlist with ... as separator




#  Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
for  x  in  a:
	print(x)        #prints each innerlist and moves next line                 
# for  x , y  in  a:  #throws error in 2nd iteration because in list 3 elements but only 2 variables
# 	print(x , y ,	sep = '...')



#  Find  outputs  (Home  work)
a = [[]]
print(a[0])   #How  to  print  inner  list)
print(*a)     #How  to  print  inner  list  in another way)



#  Find  outputs  (Home  work)
a = [[10 , 'Rama' , 1000.0] , [20 , 'Sita' , 2000.0] , [15 , 'Rajesh' , 3500.0] , [18 , 'Kiran' , 2800.0] , [5 , 'Amar'  ,5000.0] ]
print(sorted(a))                    #sorts based on 1st non matching char in each list                   
print(sorted(a , reverse = True))   #sorts in revese order based on 1st non matching char in each list
print(a)                            #remains unchanged