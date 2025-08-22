#1. Write  a  program  to  create  a  list  with  cubes  of  2 , 4 , 6 , 8 , 10  with  list  comprehension (Home  work)
a = [ i**3 for i in range(2,11,2)]
print(a)



#2. Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  without  comprehension
a = eval(input("Enter  list  of  lower  case  strings : "))
b = []
for i in a:
    b += i[0].upper()
print(b)



#3. Write  a  program  to  extract  1st  character  of  each  string  in  capital  letters  in  a  list  of  srings  with  comprehension
a = eval(input("Enter  list  of  lower  case  strings : "))
b = [i[0].upper() for i in a]
print(b)





# 4. Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list(word  should  be  in  capital  letters)  without  comprehension
a = input("Enter  any sentence : ")
b = []
for i in a.split():
    c = i.upper(),len(i)
    b.append(list(c))
print(b)





#5. Write  a  program  to  append  each  word  of  the  sentence  and  its  length  to  a  list(word  should  be  in  capital  letters)  with  comprehension
a = (input("Enter any sentence : "))
b = [[i.upper(),len(i)] for i in a.split()]
print(b)



#6. Write  a  program  to  add  two  lists  of  unequal  length  without  comprehension
a = eval(input("Enter 1st list : ")) # [10 , 20 , 30 , 40 , 50 , 60 , 70]
b = eval(input("Enter 2nd list : "))# [100 , 200 , 300 , 400]
mini =  min(len(a),len(b))
c = []
for i in range(mini):
    c.append(a[i]+b[i])
print(c)





#7. Write  a  program  to  add  two  lists  of  unequal  length  with  comprehension
a = eval(input("Enter 1st list : ")) # [10 , 20 , 30 , 40 , 50 , 60 , 70]
b = eval(input("Enter 2nd list : "))# [100 , 200 , 300 , 400]
c = [(a[i]+b[i]) for i in range(min(len(a),len(b)))]
print(c)





#8. Write   a  program  to  initialize  a  nested  list  with  zeroes  without  comprehension
a = int(input("How  many  lists  ?  : "))
b = int(input("How  many  elements  in  each  list ?  : "))
c = []
for i in range(a):
    c.append([0]*b)
print(c) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]





#9. Write   a  program  to  initialize  a  nested  list  with  zeroes  with  comprehension
a = int(input("How  many  lists  ?  : "))
b = int(input("How  many  elements  in  each  list ?  : "))
c = [[0]*b for i in range(a)]
print(c) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]





#10. Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   without  comprehension
a = eval(input("Enter 1st list : ")) # [10,20,15,18,25,32]
b = eval(input("Enter 2nd list : ")) # [30,40,10,25,15]
c = []
for i in a:
    if i not in b:
        c.append(i)
print(c) # [20, 18, 32]





#11. Write  a  program  to  extract  those  elements  of  1st  list  which  are  not  in  2nd  list   with  comprehension
a = eval(input("Enter 1st list : ")) # [10,20,15,18,25,32]
b = eval(input("Enter 2nd list : ")) # [30,40,10,25,15]
c = [i for i in a if i not in b]
print(c) # [20, 18, 32]




#12. Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension
a = [i for i in range(1,21) if i % 2 == 0]
print(f'Even numbers  between  1  and  20 :  {a}') # Even numbers  between  1  and  20 :  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




#13. Write   a  program  to  print  even  numbers  between  1  and  20  with  comprehension and without if condition
a = [i for i in range(2,21,2)]
print(f'Even numbers  between  1  and  20 :  {a}') # Even numbers  between  1  and  20 :  [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]




#14. Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension
a = [i**2 for i in range(1,21) if i**2 % 2 == 0]
print(f'Squares  of  1  to  20  which  are  divisible  by   2 :  {a}') # Squares  of  1  to  20  which  are  divisible  by   2 :  [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]





#15. Write  a  program  to  print  those  squares  of  1 , 2 , 3 , 4 , ... 20  which  are  divisible   by  2  with  comprehension and without using if condition
a = [i**2 for i in range(2,21,2) ]
print(f'Squares  of  1  to  20  which  are  divisible  by   2 :  {a}') # Squares  of  1  to  20  which  are  divisible  by   2 :  [4, 16, 36, 64, 100, 144, 196, 256, 324, 400]






#16. Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  without  comprehension
a = eval(input("Enter 1st list : ")) # [10,20,15]
b = eval(input("Enter 2nd list : ")) # [30,40,35,12]
c = []
for i in a:
    for j in b:
        c.append(i+j)
print(c) # [40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]






#17. Write  a  program  to  add  each  element  of  1st  list  with  all  the  elements  of  2nd  list  with  comprehension
a = eval(input("Enter 1st list : ")) # [10,20,15]
b = eval(input("Enter 2nd list : ")) # [30,40,35,12]
c = [(i+j) for i in a for j in b]
print(c) # [40, 50, 45, 22, 50, 60, 55, 32, 45, 55, 50, 27]






#18. Write  a  program  to  concatenate  each  character  of  1st  string  with  every  character  of   2nd  string  with  comprehension
a = (input("Enter 1st string : ")) # HYD
b = (input("Enter 2nd string : ")) # PUNE
c = [(i+j) for i in a for j in b]
print(c) # ['HP', 'HU', 'HN', 'HE', 'YP', 'YU', 'YN', 'YE', 'DP', 'DU', 'DN', 'DE']





#19. Write  a  program  to  convert  a  nested  list  to  list  without  comprehension
a = eval(input("Enter nested list : ")) # [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = []
for i in a:
    for j in i:
        b.append(j)
print(b) # [10, 20, 30, 40, 50, 60, 70, 80, 90]






#20. Write  a  program  to  convert  a  nested  list  to  list  with  comprehension
a = eval(input("Enter nested list : ")) # [ [10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ j for i in a for j in i ]
print(b) # [10, 20, 30, 40, 50, 60, 70, 80, 90]







#21. Find  outputs (Home  work)
a = [[10 , 20] , [30 , 40 , 50] , [60 , 70 , 80 , 90]]
b = [ x  for  x  in  a  for  y  in  x]
print(b) # [[10, 20], [10, 20], [30, 40, 50], [30, 40, 50], [30, 40, 50], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90], [60, 70, 80, 90]]





#22.  Nested  comprehension  demo  program (Home  work)
a = [ [ j  for   j  in   range(i)]   for   i   in   range(5)]
print(a) # [[], [0], [0, 1], [0, 1, 2], [0, 1, 2, 3]]




#23. Write  a  program  to  merge  two  sorted  lists  to  pvroduce  another  sorted  list
a = eval(input("Enter  1st list : ")) # [10,20,30,40,50]
b = eval(input("Enter  2nd list : ")) # [5,12,20,37]
max = 0
c = []
i = 0
j = 0
while i<len(a) or j < len(b):
    if j == len(b) or (i < len(a) and a[i] <= b[j]):
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1
print(c) # [5, 10, 12, 20, 20, 30, 37, 40, 50]






#24. Write  a  program  to  determine  n-th  largest  element   of   a   list
a = eval(input("Enter list : ")) # [10,20,30,25,40,35,12,5]
b = int(input("Enter which largest which to be shown : "))
a.sort()
print(f'{b}th  largest element is {a[-b]}') # 3th  largest element is 30




# 25. Write  a  program  to  sort a  list  without  using  sorted()  function  and  sort()  method
a = eval(input("Enter a List : ")) # [10,20,30,25,40,35,12,5]
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
print(a) # [5, 10, 12, 20, 25, 30, 35, 40]



#26. 
#Input :   List  of  strings
#              Eg: ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
#Output :  Nested  list
#		        i.e.  [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]
a = eval(input("Enter a list : ")) # ['Swathi' , 'Anand' , 'Srinivas' , 'Zebra' , 'King' , 'Amar' ]
b = []
for i in a:
    start = i[0]
    if i[0] not in b:
        b.append(i[0])
c = []
for i in b:
    d = []
    for ch in a:
        if ch.startswith(i):
            d.append(ch)
    c.append(d)
print(c) # [['Swathi' , 'Srinivas'] , ['Anand' , 'Amar'] , ['Zebra'] , ['King']]