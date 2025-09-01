# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension(Home work)
print([x**3 for x in range(2,11,2)])                                                
# Output: [8, 64, 216, 512, 1000]

# Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension 
a=eval(input("Enter list of lower case strings: "))
b=[]
for x in a:
    b.append(x[0].upper())
print(b)
# output   --->Enter  list  of  lower  case  strings :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
# ['H', 'P', 'C', 'V']
# Repeat   previous  program  with  comprehension
a=eval(input("Enter list of lower case strings: "))
print([x[0].upper() for x in a])

# Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list (word  should  be  in  capital  letters)  without  comprehension
a = input("Enter  any  sentence : ")
b = []
for x in a.split():
     b.append([x.upper(),len(x)])
print(b)
'''Output:
Enter  any  sentence : Students are getting bored
[['STUDENTS', 8], ['ARE', 3], ['GETTING', 7],['BORED', 5]]
'''
# Repeat   previous  program  with  comprehension
print([(x.upper(),len(x)) for x in a.split()])

#Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
a = eval(input('Enter  1st  list  :  ')) # Reads  1st  list
b = eval(input('Enter  2nd  list  :  '))  #  Reads  2nd   list
small = min(len(a) , len(b))  #  Small  length of  the  two  lists
c = []  #   Empty  list
for   i  in   range(small):
	c . append(a[i] + b[i])  #  Appends  result  of   a[i] + b[i]  to  list  'c'
print(c)
'''Output:
Enter  1st  list  :  [10,20,30,40,50,60,70]
Enter  2nd  list  :  [1,2,3,4]
[11, 22, 33, 44]'''

# Repeat   previous  program  with  comprehension
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
small = min(len(a) , len(b))
c = [a[i] + b[i]  for   i  in   range(small)]
print(c)

# Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
m = int(input('How  many  lists  ?  :  '))
n = int(input('How  many  elements  in  each  list ?  :  '))
a = []
for  i  in   range(m):   #  Appends  'm'  lists  to  list  'a'
	a .  append([0] * n)  #  Appends  list of 'n'  zeroes  to  list  'a'
print(a)
'''Output:
How  many  lists  ?  :  3
How  many  elements  in  each  list ?  :  5
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0,0,0,0,0]]
''' 
# Repeat   previous  program  with  comprehension
m = eval(input('How  many  lists ?  :  '))
n = eval(input('How  many  elements  in  each  list ?  :  '))
a = [[0] *  n   for  i  in   range(m)]
print(a)

#Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
result = []
for x in a:
    if x not in b:
        result.append(x)
print(result)
'''Output:
Enter 1st  list  :  [10,20,15,18,25,32]
Enter 2nd  list  :  [30,40,10,25,15]
Elements  of  1st  list  which  are  not  in  2nd  list  : [20,18,32]
'''
# Repeat   previous  program  with  comprehension
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
result = [x for x in a if x not in b]
print(result)

#  Write   a  program  to  print  even  numbers  between  1  and  20  with comprehension
print([x for x in range(1,21) if x%2==0 ]) # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Repeat  previous  program  with  comprehension  and  without  using  if
print([x for x in range(2, 21, 2)])
                     
# Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
print([x**2 for x in range(1,21) if x%2==0 ])   # [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]

# Repeat  previous  program  with  comprehension  and  without  using  if
print([x**2 for x in range(2,21,2)])
 
# Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
result = []
for x in a:            
    for y in b:         
        result.append(x + y)
print("Result:", result)
'''Output
Enter 1st list : [10,20,15]
Enter 2nd list : [30,40,35,12]
[40, 50, 45, 22, 50, 60, 55, 32,45,55,50,27]
'''
# Repeat   previous  program  with  comprehension
a = eval(input('Enter  1st  list  :  '))
b = eval(input('Enter  2nd  list  :  '))
result = [x + y for x in a for y in b]
print("Result:", result)

#Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
s1 = input('Enter 1st string: ')
s2 = input('Enter 2nd string: ')
result = [x+y for x in s1 for y in s2]
print(result)
'''Output:
Enter 1st string:  HYD  
Enter 2nd string:  PUNE
['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']
'''
# Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
a = eval(input("Enter nested list : ")) #  Reads  a  nested  list
b = []  #  Empty list
for  x  in  a:   #  'x'  is  each  inner  list   of  list  'a'
	b . extend(x)  #  Appends  elements  of   each  inner  list  to  list  'b'
print(b)
'''Output:
Enter nested list : [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
[10 , 20 , 30 , 40 , 50 , 60 , 70, 80 , 90]'''

# Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
a = eval(input("Enter nested list : "))
b = [y for x in a for y in x]
print(b)

# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y in x]
print(b)
'''Output:
[[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]'''
#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)
# [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]
'''Most  tricky  program
Input :   List  of  strings
Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
Output :  Nested  list
i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
Hint: Do  not  sort  the  lists
1) b = ['S' , 'A' ,  , 'Z' , 'K' ]
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
a = eval(input('Enter  list  of  strings :  '))  #  Reads  a  list  of  strings
b = []  #  Empty  list
for  str  in  a:  #  str  is  each  string  of  list  'a'
	firstchar = str[0]  #  First  char  of each  string  in  list  'a'
	if  firstchar  not  in  b:
		b . append(firstchar)  #   Appends  first  char  to  list  'b'  if  it is  not in  list  'b'
c = []  #  Empty  list
for  ch  in  b:  #  ch  is   each   char  of  list  'b'
	d = [] #  Empty  list
	for   str  in  a:    #  str  is  each  string  of  list  'a'
		if  str . startswith(ch):
			d . append(str)  #  Appends  the  string  to  list  'd'   if  it  starts  with  the  char  ch
	c . append(d)    #   Appends   list 'd'  to  list  'c'
print(c)
'''Output:
Enter  list  of  strings :  ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
[['Swathi', 'Srinivas'], ['Anand', 'Amar'], ['Zebra'],['King']]'''

'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list

                                0      1      2       3         4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
	                            0     1       2       3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 :  Unsorted  lists  can  not  be  merged
Hint2 :  Use  single  while  loop
'''
a = eval(input('Enter  1st  list  : '))  #  Reads  1st  list
b = eval(input('Enter  2nd  list  : ')) #  Reads  2nd  list
a  . sort()  #  Sorts  1st  list
b  . sort() #  Sorts  2nd  list
c = []  #  Empty   list
i = j = 0  #  Index  of  first  element in   the  two  lists
while  i <  len(a)  and  j <  len(b):  #  Repeat  until  at least  one   list  is  exhausted
	if  a[i] < b[j]:  # Appends  smallest  element  of   a[i]  and  b[j]  to  list  'c'
		c . append(a[i])
		i += 1   #  Moves  to  next  element  of  list  'a'
	else:
		c . append(b[j])
		j += 1 #    Moves  to  next  element  of  list  'b'
c . extend(a[i:]) #  Appends  remaining  elements  of  list  'a'  to  list  'c'
c . extend(b[j:])  #  Appends  remaining  elements  of  list  'b'  to  list  'c'
print(c)
'''
Write  a  program  to  determine  n-th  largest  element   of   a   list

Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''
try:
	list = eval(input('Enter list:'))  #   Reads  a  list
	n = eval(input('Enter  value  of  n : '))
	s = set(list)  #  Convets  list  to  set  to  avoid  duplicates
	for  i  in  range(n):  #  Execute  loop  'n'  times
		large = max(s)  #  Largest  element  of  the  set
		s . remove(large)   #   Removes  largest  element  from  set
	print(F'{n}th  largest  element  :  {large}')
except: #   Executed  when  n >  len(list)
	print('Invalid  input')

'''Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method
Input :  [10,20,30,25,40,35,12,5]
Output :  [5,10,12,20,25,30,35,40]
'''
list = eval(input('Enter list:'))    #   Reads  list
new = [] #  Empty  list
while  list:  # Repeat until  list  is  empty
	small = min(list)  #   Smallest   element  of  the  list
	new . append(small)  #  Appends  smallest  element  of  the  list  to  a  new  list
	list. remove(small)  #   Removes  smallest  element  of  the  list
print(new) #  Sorted  list

                           
                           
                           
                           
                           


