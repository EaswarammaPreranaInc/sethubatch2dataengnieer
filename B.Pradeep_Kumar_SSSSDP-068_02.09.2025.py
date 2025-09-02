#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
'''
(10,20,15,18)
<class 'tuple'>
4
'''
f1()
'''
(,)
class tuple
0
'''
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
'''
([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
class 'tuple'
3
'''
f1('Hyd')
'''
('Hyd',)
class 'tuple'
1
'''
tpl = (100 , 200 , 150)
f1(tpl)
'''
((100,200,150),)
clas 'tuple'
1
'''
f1(t = (10 , 20 , 30))  #  Error 



#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
try:
    def  avg(*a):
        return sum(a)/len(a)
        #Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
    # End  of  the  function
    print(avg(10 , 20 , 15 , 18))
    print(avg(25 , 10.8 , True))
    print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
    print(avg())
    print(avg(25))
    print(avg(3 + 4j , 5 + 6j))
    tpl = (10 , 20 , 15 , 18)
    print(avg(tpl))
except:
    print("Enter atleast Two Numbers")


#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
    return " ".join(f"{x}" for x in a)
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))



#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)  #  a : 10    b : (20 , 30 , 40)
f1(50 , 60)  #  a : 50    b : (60,)
f1(70)  #  #  a : 25    b : (70)
f1(a = 80)  #  a : 8-    b : ()
f1(b = (10 , 20 , 30) , a = 40)  #  Error due to b
f1()  #  #  a : 25    b : ()
f1(a = 10 , (20 , 30 , 40))  #  Error due to Positional argument folloows keyword arguement
f1(25 , b = (10 , 20 , 30)) #  Error due to b is unexpected keyword argument
f1(25 , a = (10 , 20 , 30))  # Error due to a have multiple values
f1((10 , 20 , 30) , 10 , 20 , 30)  #  a : (10,20,30)    b : (10,20,30)
f1(a = (10 , 20 , 30) , 10 , 20 , 30)   #  Error due to Positional argument folloows keyword arguement



#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)  #  a : (10,20,30)    b : 40
f1(50 , b = 60)  #  a : (50,)   b : 60
f1(b = 70)  #  a : ()   b : 70
f1(b = 10 , a = (20 , 30 , 40))  #  Error due to a
f1(b = 10 , (20 , 30 , 40))  #  Error due to Positional argument follows Keyword argument
f1()  #  Error due to b  value not givened
f1(10 , 20 , 30 , (10 , 20 , 30))  #  Error due to b value not givened
f1(10 , 20 , 30 , 40)  #  Error due to b value not givened
f1(25)  #  Error due to b value not givened
f1(10 , 20 , 30 , b = (10 , 20 , 30))  #   a : (10,20,30)   b : (10,20,30)



#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)  #  a : 10   b : (20,30,40)  c : 50
f1(60 , 70 , c = 80)  #   a : 60    b : (70,)   c : 80
f1(90 , c = 100)  #  a : 90     b : ()   c : 100
f1(a = 1 , 2 , c = 3)  #  Error due to Positional argument follows Keyword argument
f1(1 , 2 , 3)  #  Error due to c is missed
f1(a = 1 , b = 2 , c = 3)  #  Error due to b
f1(a = 25 , 100 , 200 , 300 , c = 35)  #  Error due to Positional argument follows Keyword argument



# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):  #  Error due to only one * allowed
        pass
def  f2(*a , b):  #  Valid
        pass
def  f3(a , *b):  #  Valid
        pass
def  f4(a , b):  #  Valid
        pass
def    f5(a , *b , c):  #  valid
        pass
def   f6( * , a , *b , c):  #  Error due to only one * allowed
       pass
def   f7(a , *b , c ,  /):  #  error
       pass



# Find  outputs  (Home  work)
def   f1(*a):
	print(a)  #  ([10 , 20] , {30 , 40} , (50 , 60))
	print(type(a))  #  class 'tuple'
	for  x  in  a:
		print(x)  #  [10 , 20]  {30 , 40}  (50 , 60)
		print(type(x))  #  class list,set,tuple
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))



# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
disp()

'''
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}

Results
<class 'dict'>
{'EmpNo': 25, 'EmpName': 'Sita', 'Salary': 10000.0}

Results
<class 'dict'>
{'AcNo': 30, 'CustName': 'Kiran', 'Balance': 20000.0, 'Gender': 'm'}

Results
<class 'dict'>
{}
'''


# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')  #  
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
'''
Results
Empno ... 25
Empname ... Rama  Rao
Salary ... 10000.0
Gender ... m
'''
f1()  #  Results



# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))  #  class 'tuple'
	print(a)  #  (25 , 10.8 , 'Hyd' , True)
def   f2(**a):  
	print(type(a))  #  class 'dict'
	print(a)  #  {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()  #  < next line >
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0) 



#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
    #  Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
def   f2(**a):
	print(a)  #  {'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
              #  {'eno': 25, 'empname': 'Sita', 'salary': 10000.0}
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)  #  Error due to eno , empname , salary not in funcion
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)



# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a) 
	if   b:
		print(b) 
	if  c:
		print(c)  
# End  of  the  function
f1(25)  #  
print()
f1('Hyd' , 10 , 20 , 30)
print()  
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)

'''
25

Hyd
(10, 20, 30)

10.8
(25, 'Hyd', True)
{'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}
'''



# ---------------------  Exam sums -----------------------------------------------

'''
Write  a   program  to  print  roman  equivalent  of  a  number
1000 -  M
900  -  CM
500 -  D
400 - CD
100 -   C
90  -  XC
50  -  L
40  -  XL
10  -  X
9  -  IX
5  -  V
4  -  IV
1  -  I

1) What  is  the  output  if  input  is  3878 ? ---> MMMDCCCLXXVIII

2) What  is  the  result  of  3878 // 1000 ?  --->  3
    How  many  M's  are  concatenated  to  the  sting ?  --->  Three  becoz  3878 / 1000  is  3
    What  is  the  result  of  3878 % 1000 ?  --->  878

3) What  is  the  result  of  878 // 900 ?  --->  0
    How  many  CM's  are  concatenated  to  the  string ?  ---> Zero  becoz  878 / 900  is  0
    What  is  the  result  of  878 % 900 ?  --->  878

4) What  is  the  result  of  878 // 500 ?  ---> 1
     How  many  D's  are  concatenated  to  the  string ?  ---> One  becoz  878 / 500  is  1
     What  is  the  result  of  878 % 500 ?  ---> 378
    and  so  on
'''
a = int(input("Enter a number: "))
c = ''

while a > 0:
    if a // 1000 >= 1:
        c += 'M' * (a // 1000)
        a = a % 1000
    elif a // 900 >= 1:
        c += 'CM' * (a // 900)
        a = a % 900
    elif a // 500 >= 1:
        c += 'D' * (a // 500)
        a = a % 500
    elif a // 400 >= 1:
        c += 'CD' * (a // 400)
        a = a % 400
    elif a // 100 >= 1:
        c += 'C' * (a // 100)
        a = a % 100
    elif a // 90 >= 1:
        c += 'XC' * (a // 90)
        a = a % 90
    elif a // 50 >= 1:
        c += 'L' * (a // 50)
        a = a % 50
    elif a // 40 >= 1:
        c += 'XL' * (a // 40)
        a = a % 40
    elif a // 10 >= 1:
        c += 'X' * (a // 10)
        a = a % 10
    elif a // 9 >= 1:
        c += 'IX' * (a // 9)
        a = a % 9
    elif a // 5 >= 1:
        c += 'V' * (a // 5)
        a = a % 5
    elif a // 4 >= 1:
        c += 'IV' * (a // 4)
        a = a % 4
    else:
        c += 'I' * (a // 1)
        a = 0   
print(c)


'''
Write  a  program  to  print  each  digit  of  the  number  in  words

Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven

a = ['Zero' , 'One' , 'Two' ,....  'Nine']

Iteration     ch     int(ch)       a[int(ch)]         s
--------------------------------------------------------
                                                                     ''
     1              '9'       9               'Nine'          '' + 'Nine' + ' '

	 2             '2'       2               'Two'          'Nine ' + 'Two' + ' '

	 3             '4'       4               'Four'          'Nine Two ' + 'Four' + ' '

	 4             '7'       7               'Seven'        'Nine Two Four ' + 'Seven' + ' '
'''
a=input("Enter a number : ")
b = ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
c=''
for i in a:
    if int(i)>=0:
        c+=b[int(i)]+' '
print(c)
        


'''
Write  a  program  to  print  all  the  rotations  of  the  string

 1) Let  input  be     S   P  A   C   E
                               0   1   2   3   4
    What  are  the  outputs ?  --->  SPACE
	                                                  PACES
									                  ACESP
												      CESPA
												      ESPAC

2) What  are  the  indexes  of  SPACE ?  ---> 0  to  4
     What  are  the  indexes  of  PACES ?  ---> 1  to  4 , 0  to  0
     What  are  the  indexes  of  ACESP ?  ---> 2  to  4 , 0  to  1
     What  are  the  indexes  of  CESPA ?  ---> 3  to  4 , 0  to  2
     What  are  the  indexes  of  ESPAC ?  ---> 4  to  4 , 0  to  3

3) What  are  the  indexes  in  general ?  --->  i  to  length - 1   and   0  to  i - 1
'''        
x=input("Enter a input : ")
i=0
while i<=len(x)-1:
    print(x[i:len(x):]+x[0:i])
    i=i+1


'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       						 7 * 2 = 14
			  								 7 * 3 = 21
												 .....
											 7 * 10 = 70
'''
a=int(input("Enter table nuber : "))
for i in range(1,11):
    print(f"{a}*{i}={a*i}")


'''
Write a  program to print following pyramid
Input: 5

             A
            A B
           A B C
          A B C D
         A B C D E


	   i         ch
---------------------
       1         'A'

	   2         'A'  to  'B'

	   3         'A'  to  'C'

	   4         'A'  to  'D'

	   5         'A'  to  'E'
'''

a = int(input("Enter a number: "))
for i in range(a):
    print(" " * (a - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    print()

