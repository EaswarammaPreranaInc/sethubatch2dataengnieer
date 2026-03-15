
# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)

a=[x**3 for x in range(1,11) if x%2==0]
print('Cubes  of  1  to  10  which  are  divisible  by   2 :',a)

'''
# Output:
Cubes  of  1  to  10  which  are  divisible  by   2 : [8, 64, 216, 512, 1000]
'''



'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''
a=eval(input('Enter  list  of  lower  case  strings :'))
b=[]
for i in a:
	b.append(i[0].upper())
print(b)
'''
# Output:
Enter  list  of  lower  case  strings : ['hyd' , 'pune' , 'chennai' , 'vijayawada']
['H', 'P', 'C', 'V']
'''


'''
(Home  work)
Repeat   previous  program  with  comprehension
'''
a=eval(input('Enter  list  of  lower  case  strings :'))
b=[i[0].upper() for i in a]
print(b)

'''
Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']

Output :  ['H' , 'P' , 'C' , 'V']
'''




'''
Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''

'''Enter  any  sentence :  Students are getting bored
[['STUDENTS', 8], ['ARE', 3], ['GETTING', 7], ['BORED', 5]]
'''
a=input('Enter  any  sentence : ')
b=a.split(' ')
c=[]
for i in b:
	c.append([i.upper(),len(i)])
print(c)
	


'''
(Home  work)
Repeat   previous  program  with  comprehension
'''
a=input('Enter  any  sentence : ')
b=a.split(' ')
c=[[i.upper(),len(i)] for i in b]
print(c)

'''
Input :  hyd  is  green  city
Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''



'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension

Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

a=eval(input('Enter 1st list :'))
b=eval(input('Enter 2nd list :'))
c=[]
for i in range(min(len(a),len(b))):
	c.append(a[i]+b[i])
print(c)

'''
# Output:
Enter 1st list : [10,20,30,40,50,60,70]
Enter 2nd list : [100,200,300,400]
[110, 220, 330, 440]
'''



'''
(Home  work)
Repeat   previous  program  with  comprehension
'''
a=eval(input('Enter 1st list :'))
b=eval(input('Enter 2nd list :'))
c=[a[i]+b[i] for i in range(min(len(a),len(b)))]
print(c)

'''
# Output:
Enter 1st list : [10,20,30,40,50,60,70]
Enter 2nd list : [100,200,300,400]
[110, 220, 330, 440]
'''


'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension

Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]

Hint:  Use  repetition  operator  *
'''

a=eval(input('How many lists? :'))
b=eval(input('How many elements in each list? :'))
c=[]
for i in range(a):
	c.append([0]*b)
print(c)

'''
# Output:
How many lists? : 3
How many elements in each list? : 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''




'''
(Home  work)
Repeat   previous  program  with  comprehension
'''
a=eval(input('How many lists? :'))
b=eval(input('How many elements in each list? :'))
c=[[0]*b for i in range(a)]
print(c)

'''
# Output:
How many lists? : 3
How many elements in each list? : 4
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
'''



'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension

Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

a=eval(input('Enter 1st list :'))
b=eval(input('Enter 2nd list :'))
c=[]
for i in a:
	if i not in b:
		c.append(i)
print('Elements of 1st list which are not in 2nd list :',c)

'''
# output:
Enter 1st list : [10,20,15,18,25,32]
Enter 2nd list : [30,40,10,25,15]
Elements of 1st list which are not in 2nd list : [20, 18, 32]
'''



'''
(Home  work)
Repeat   previous  program  with  comprehension
'''
a=eval(input('Enter 1st list :'))
b=eval(input('Enter 2nd list :'))
c=[i for i in a if i not in b]
print('Elements of 1st list which are not in 2nd list :',c)


'''
# output:
Enter 1st list : [10,20,15,18,25,32]
Enter 2nd list : [30,40,10,25,15]
Elements of 1st list which are not in 2nd list : [20, 18, 32]
'''





#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

a=[x for x in range(1,21) if x%2==0]
print('Even  numbers  between  1  and  20:',a)

'''
# Output:
Even numbers  between  1  and  20 : [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''


#Repeat  previous  program  with  comprehension  and  without  using  if

a=[x for x in range(2,21,2)]
print('Even  numbers  between  1  and  20:',a)

'''
# Output:
[Even  numbers  between  1  and  20: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
'''


# Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension

a=[x**2 for x in range(1,21) if x%2==0]
print('Squares  of  1  to  20  which  are  divisible  by   2 :',a)

'''
# Output:
Squares  of  1  to  20  which  are  divisible  by   2 : [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''

#  Repeat  previous  program  with  comprehension  and  without  using  if

a=[x**2 for x in range(2,21,2)]
print('Squares  of  1  to  20  which  are  divisible  by   2 :',a)

'''
# Output:
Squares  of  1  to  20  which  are  divisible  by   2 : [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]
'''


'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension

Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
					
Hint : Nested  for  loops
'''
a=eval(input('Enter 1st list :'))
b=eval(input('Enter 2nd list :'))
c=[]
for i in a:
	for j in b:
		c.append(i+j)
print(c)

'''
# output:
Enter 1st list :[10,20,15]
Enter 2nd list :[30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
'''



'''
(Home  work)
Repeat   previous  program  with  comprehension
'''
a=eval(input('Enter 1st list :'))
b=eval(input('Enter 2nd list :'))
c=[ i+j for i in a for j in b]
print(c)

'''
# output:
Enter 1st list :[10,20,15]
Enter 2nd list :[30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]
'''



'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension

Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']

Hint: Same  as  previous  program
'''

a=input('Enter 1st string :')
b=input('Enter 2nd string :')
c=[i+j for i in a for j in b]
print(c)

'''
# output:
Enter 1st string :HYD
Enter 2nd string :PUNE
['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']
'''



'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension

Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

a=eval(input('Enter nested string :'))
b=[]
for i in range(len(a)):
	for j in range(len(a[i])):
		b.append(a[i][j])
print(b)

'''
# output:
Enter nested string :[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''


'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''
a=eval(input('Enter nested string :'))
b=[a[i][j] for i in range(len(a))for j in range(len(a[i]))]
print(b)

'''
# output:
Enter nested string :[ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10, 20, 30, 40, 50, 60, 70, 80, 90]
'''


# Find  outputs (Home  work)

a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b)
# Output: [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]



#  Nested  comprehension  demo  program (Home  work)

a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
# Output: [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]




'''
Most  tricky  program
Input :   List  of  strings
              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]

Hint: Do  not  sort  the  lists

1) b = ['S' , 'A' , 'Z' , 'K' ]

2) c = []

3) Iteartion  1 :  d  = ['Swathi' , 'Srinivas']
                   c =  [['Swathi' , 'Srinivas']]

4) Iteartion  2 :  d  =  ['Anand' , 'Amar']
                   c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar']]

5) Iteartion  3 :  d  =  ['Zebra']
                   c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra']]

6) Iteartion  4 :  d  =  ['King']
                   c =   [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
'''
a=eval(input('Enter list of strings :'))
b=[]
c=[]
for i in a:
	m=i[0]
	if m not in c:
		d=[]
		for j in a:
			if j[0]==m:
				d.append(j)
		b.append(d)
		c.append(m)
print(b)

'''
# Output:
Enter list of strings :['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'], ['King']]
'''




'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list
                        0      1     2       3       4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
     List  'b'   --->  [5  ,  12  , 20   ,  37]
	                   0     1     2       3
	List  'c'   --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 :  Unsorted  lists  can  not  be  merged

Hint2 :  Use  single  while  loop
'''
a=eval(input('Enter 1st sorted list :'))
b=eval(input('Enter 2nd sorted list :'))
i=j=0
c=[]
while i < len(a) and j < len(b):
	if a[i]<=b[j]:
		c.append(a[i])
		i+=1
	else:
		c.append(b[j])
		j+=1
c.extend(a[i:])
c.extend(b[j:])
print('Merged Sorted List:',c)

'''
# output:
Enter 1st sorted list: [10, 20, 30, 40, 50]
Enter 2nd sorted list: [5, 12, 20, 37]
Merged Sorted List: [5, 10, 12, 20, 20, 30, 37, 40, 50]
'''		
	



'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''
a=eval(input('Enter list :'))
b=int(input('Enter which largest which to be shown:'))
a.sort(reverse=true)
print(f'{n}th largest element: {a[n-1]}')

'''
# output:
Enter list:[10,20,30,25,40,35,12,5]
Enter which largest which to be shown:4
4th  largest  element  :  25
'''



'''
Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method

Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
a=eval(input('Enter List:'))
b=[]
while a:
	m=min(a)
	b.append(m)
	a.remove(m)
print(b)

'''
# output:
Enter list: [10,20,15,12,5]
[5, 10, 12, 15, 20]
'''