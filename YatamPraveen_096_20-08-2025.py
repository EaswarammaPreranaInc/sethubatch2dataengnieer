# Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
lst=[i**3 for i in range(2,11,2)]
print(lst)





'''
(Home  work)
Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
Let  input  be   ['hyd' , 'pune' , 'chennai' , 'vijayawada']
What  is  the  output ?  ---> ['H' , 'P' , 'C' , 'V']
'''

lst, lst1=eval(input('Enter the list : ')), []
for i in lst:
    lst1.append(i[0].upper())
print(lst1)





'''
(Home  work)
Repeat   previous  program  with  comprehension
Input :  ['hyd' , 'pune' , 'chennai' , 'vijayawada']
Output :  ['H' , 'P' , 'C' , 'V']
'''

lst=eval(input('Enter the list : '))
lst1=[i[0].upper() for i in lst]
print(lst1)




'''
Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
Let  1st  list  be  [10 , 20 , 30 , 40 , 50 , 60 , 70]  and  2nd  list  be  [100 , 200 , 300 , 400]
What  is   the  result ?  ---> [10 + 100 , 20 + 200 , 30 + 300 , 40 + 400]
'''

lst1, lst2, lst3= eval(input('Enter the 1st list : ')), eval(input('Enter the 2nd list : ')), []
temp = min(len(lst1), len(lst2))
for i in range(temp):
    lst3.append(lst1[i] + lst2[i])
print(lst3)    





'''
(Home  work)
Repeat   previous  program  with  comprehension
Input1 : [10 , 20 , 30 , 40 , 50 , 60 , 70]
Input2 :  [100 , 200 , 300 , 400]
Output :  [110 , 220 , 330 , 440]
'''

lst1, lst2 = eval(input('Enter the 1st list : ')), eval(input('Enter the 2nd list : '))
temp = min(len(lst1), len(lst2))
lst3 = [lst1[i] + lst2[i] for i in range(temp)]
print(lst3)    





'''
Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
Let inputs  be  3  and  4
What  is  the  output ?  --->  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
Hint:  Use  repetition  operator  *
'''

ip1, ip2, e_lst = int(input('Enter the number of elements : ')), int(input('Enter the number of elements in inner element : ')), []
for i in range(ip1):
    e_lst.append([0]*ip2)
print(e_lst)    





'''
(Home  work)
Repeat   previous  program  with  comprehension
Inputs :  3  and  4
Output :  [[0 , 0 , 0 , 0] , [0 , 0 , 0 , 0] , [0 , 0 , 0 , 0]]
'''

ip1, ip2 = int(input('Enter the number of elements : ')), int(input('Enter the number of elements in inner element : '))
e_lst = [[0]*ip2 for i in range(ip1)]
print(e_lst)    




'''
Write  a  program  to  append  each  word  of  the  sentence  and its  length  to  a  list
(word  should  be  in  capital  letters)  without  comprehension

Let  input  be   hyd  is  green  city
What  is  the  output ?  --->  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY', 3]]
'''

lst, lst1 = input('Enter the list : ').split(), []
for i in lst:
    lst1.append([i.upper(),len(i)])
print(lst1)





'''
(Home  work)
Repeat   previous  program  with  comprehension
Input :  hyd  is  green  city
Output :  [['HYD' , 3] , ['IS' , 2] , ['GREEN' , 5] , ['CITY' , 4]]
'''
lst = input('Enter the list : ').split()
lst1 = [[i.upper(),len(i)] for i in lst]
print(lst1)    





'''
Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
Let  1st  list  be  [10 , 20 , 15 , 18 , 25 , 32]  and  2nd  list  be  [30 , 40 , 10 , 25 , 15]
What  is  the  output ?  --->  [20 , 18 ,  32]
'''

lst1, lst2, temp = eval(input('Enter the 1st list : ')), eval(input('Enter the 2nd list : ')), []
for i in lst1:
    if i not in lst2:
        temp.append(i)
print(temp)        





'''
(Home  work)
Repeat   previous  program  with  comprehension
Input1 :   [10 , 20 , 15 , 18 , 25 , 32]
Input2 :  [30 , 40 , 10 , 25 , 15]
Output :  [20 , 18 , 32]
'''

lst1, lst2 = eval(input('Enter the 1st list : ')), eval(input('Enter the 2nd list : '))
temp = [i for i in lst1 if i not in lst2]
print(temp) 





#  Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension

lst = [i for i in range(1, 21) if i%2==0]
print('Even numbers  between  1  and  20 : ', lst)





'''
Repeat  previous  program  with  comprehension  and  without  using  if
Output: [Even  numbers  between  1  and  20]
'''

lst = [i for i in range(2, 21, 2)]
print('Even numbers  between  1  and  20 : ', lst)





'''
Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
What  is  the  output ?  ---> [4 , 16 , 36 , ... ,  400]
'''

lst = [i**2 for i in range(1, 21) if (i**2)%2 ==0]
print(lst)





#  Repeat  previous  program  with  comprehension  and  without  using  if

lst = [i**2 for i in range(2, 21, 2)]
print(lst)





'''
Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
Let  1st  list  be  [10 , 20 , 15]  and  2nd  list  be  [30 , 40 , 35 , 32]
What  is  the  result ?  --->
					[10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
Hint : Nested  for  loops
'''

lst1, lst2, temp = eval(input('Enter the 1st list : ')), eval(input('Enter the 2st list : ')), []
for i in lst1:
    for j in lst2:
        temp.append(i+j)
print(temp) 





'''
(Home  work)
Repeat   previous  program  with  comprehension
Input1 :  [10 , 20 , 15]
Input2 :  [30 , 40 , 35 , 32]
Output :  [10 + 30 , 10 + 40 , 10 + 35 , 10 + 32 , 20 + 30 , 20 + 40 , 20 + 35 , 20 + 32 , 15 + 30 , 15 + 40 , 15 + 35 , 15 + 32]
'''

lst1, lst2 = eval(input('Enter the 1st list : ')), eval(input('Enter the 2st list : '))
lst3 = [i+j for i in lst1 for j in lst2]
print(lst3)





'''
Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
Let  1st string  be  HYD  and   2nd string  be   PUNE
What  is  the  result  ?  --->  ['HP' , 'HU' , 'HN' , 'HE' , 'YP' , 'YU' , 'YN' , 'YE' , 'DP' , 'DU' , 'DN' , 'DE']
Hint: Same  as  previous  program
'''

lst1, lst2 = input('Enter the 1st list : '), input('Enter the 2st list : ')
lst3 = [i+j for i in lst1 for j in lst2]
print(lst3)





'''
Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

lst, temp = eval(input('Enter the list : ')), []
for i in lst:
    temp.extend(i)
print(temp)    





'''
Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
Let  input  be  [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
What  is  the  output ?  --->  [10 , 20 , 30 , 40 , 50 , 60 , 70 , 80 , 90]
'''

lst = eval(input('Enter the list : '))
lst2 = [j for i in lst for j in i]
print(lst2)    





# Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [x for x in a for y in x]
print(b)        	#[[10 , 20], [10 , 20], [30 , 40 , 50], [30 , 40 , 50], [30 , 40 , 50], [60 , 70 , 80 , 90]. [60 , 70 , 80 , 90]. [60 , 70 , 80 , 90]. [60 , 70 , 80 , 90]]





#  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a)        	#[[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]





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

lst = eval(input('Enter the list : '))
chr_lst = []
for i in lst:
    if i[0] not in chr_lst:
        chr_lst.append(i[0])
res_lst = []        
for i in chr_lst:
    temp_lst = []
    for j in lst:
        if j[0] == i:
            temp_lst.append(j)
    res_lst.append([temp_lst])
print(res_lst)





'''
Write  a  program  to  merge  two  sorted  lists  to  produce  another  sorted  list
                        0      1     2       3       4
Eg:  List  'a'   --->  [10  ,  20  , 30   ,  40   ,  50]
       List  'b'   --->  [5  ,  12  , 20   ,  37]
       
	                    0    1    2    3
	   List  'c' --->  [5 , 10 , 12 , 20 , 20 , 30 , 37 , 40 , 50]

Hint1 :  Unsorted  lists  can  not  be  merged
Hint2 :  Use  single  while  loop
'''
lst1 = sorted(eval(input('Enter the 1st list : ')))
lst2 = sorted(eval(input('Enter the 2nd list : ')))
lst3 = []
l = min(len(lst1), len(lst2))
for i in range(l):
    if lst1[i] >= lst2[i]:
        lst3.append(lst2[i])
        lst3.append(lst1[i])
    else:
        lst3.append(lst1[i])
        lst3.append(lst2[i])
if len(lst1) == l:
    print(lst3 + lst2[l:])
else:
    print(lst3 + lst1[l:])





'''
Write  a  program  to  determine  n-th  largest  element   of   a   list
Input1 :  [10,20,30,25,40,35,12,5]
Input2 :  3  (3rd  largest)
Output :  30
'''

lst = sorted(eval(input('Enter the list : ')))
ip2 = int(input('Enter the number of largest input : '))
print(lst[-ip2])