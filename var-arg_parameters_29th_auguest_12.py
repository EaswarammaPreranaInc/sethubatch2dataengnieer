#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)#(10 , 20 , 15 , 18)
	print(type(t))#class tuple
	print(len(t))#4
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()#()
Class tuple 
0

f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})#([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
Class tuple
3
f1('Hyd')#('hyd')
Class tuple
1

tpl = (100 , 200 , 150)
f1(tpl)#((100 , 200 , 150))
Class tuple 
3
f1(t = (10 , 20 , 30))# error

'''
(10,20,15,18)
<class 'tuple'>
4
'''




#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a:25. B: (10 , 20 , 30 , 40)
f1(50 , 60)#a:25.     b:(50,60)
f1(70)#a:25.     b:(70)
f1(a = 80)#a:80.     b:()
f1(b = (10 , 20 , 30) , a =40)#a=40.     b=(10 , 20 , 30)
f1()#a=25     b=()
f1(a = 10 , (20 , 30 , 40))#a=10     b=(20 , 30 , 40)
f1(25 , b = (10 , 20 , 30))#a=25   b=(10 , 20 , 30)
f1(25 , a = (10 , 20 , 30))#error
f1((10 , 20 , 30) , 10 , 20 , 30)#error
f1(a = (10 , 20 , 30) , 10 , 20 , 30)#error




#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40)#a=(10 , 20 , 30).     b=40 
f1(50 , b = 60)a=(50,)     b=60
f1(b = 70)#a=()     b=70
f1(b = 10 , a = (20 , 30 , 40))#a=(20,30,40)     b=10
f1(b = 10 , (20 , 30 , 40))#a=(20,30,40)     b=10
f1()#error
f1(10 , 20 , 30 , (10 , 20 , 30))#a=(10,20,30)     b=10,20,30
f1(10 , 20 , 30 , 40)#error
f1(25)#error
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a=(20,30,40)     b=10,20,30



#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#error
f1(60 , 70 , c = 80)#a=60  b=(10,).    C:80
f1(90 , c = 100)#error
f1(a = 1 , 2 , c = 3)#a:1  b=(2,).    C:100
f1(1 , 2 , 3)#a:1  b=(2,).    C:3
f1(a = 1 , b = 2 , c = 3)#error
f1(a = 25 , 100 , 200 , 300 , c = 35)#a:25  b=(,100,200,).    C:300


# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):
        pass#valid
def  f2(*a , b):
        pass# valid
def  f3(a , *b):
        pass#vakid
def  f4(a , b):
        pass#valid
def    f5(a , *b , c):
        pass# valid
def   f6( * , a , *b , c):
       pass# invalid 
def   f7(a , *b , c ,  /):
       pass# invalid




# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))#([10 , 20] , {30 , 40} , (50 , 60))
Class tuple
[10 , 20]
{30 , 40}
(50 , 60)
Class Tuple




# Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')   #  Dictionary  is  passed  to  the  function
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)#
Results:
{EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0}
Class dict

disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')#
Results
{AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm}
Class dict
disp()#resutls
{}
Class dict




#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)#{empno = 25 , ename = 'Sita' , sal = 10000.0}
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)#error
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)#{empno = 25 , ename = 'Sita' , sal = 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)#{eno = 25 , empname = 'Sita' , salary = 10000.0}


# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
#class tuple
{25 , 10.8 , 'Hyd' , True}
#class dict
{EmpNum : 25 , EmpName : 'Sita' , Salary : 10000.0}


#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)#{
'Emp  Number  =  25\t  Emp  Name  =  'Sita'  \t  Salary  =	10000.0
f1(eno = 25 , empname = 'Sita' , salary = 10000.0)#
{EmpNum : 25 , EmpName : 'Sita' , Salary : 10000.0}
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)#
{EmpNum : 25 , EmpName : 'Sita' , Salary : 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)#
{EmpNum : 25 , EmpName : 'Sita' , Salary : 10000.0}



# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)
print()
#25
f1('Hyd' , 10 , 20 , 30)
print()
#(Hyd' , 10 , 20 , 30)
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
#(10.8 , 25 , 'Hyd' , True)
{EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0}



#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a)#a:10
	print('b : ' , b)#40
	print('c : ' , c)#error
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)#50
	print('b : ' , b)#20
	print('c : ' , c)# error
# End  of  f2()  function
c = 30
print('a : ' , a)#error
print('b : ' , b)#error
print('c : ' , c)#30
print()
a +=  1
b +=  1
c +=  1
f1()#11
41
Error
a +=  1
b +=  1
c +=  1
f2()#
51
21
31
Bye
print('Bye')




# Find  outputs (Home  work)
def   f1():
	a = 20
	print(a)#20
	a += 1
#End  of  the  function
a = 10
print(a)#10
a += 1
f1()#20
print(a)#11



#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
    print(" ".join(a))
   	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat("1"," 2"," 3"))



#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	return sum(a) / len(a) if a else 0
# End  of  the  function
print(avg(10 , 20 , 15 , 18))
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))

15.75
12.933333333333334
14.26
0
25.0
(4+5j)
15.75