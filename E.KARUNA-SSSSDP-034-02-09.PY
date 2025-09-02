#1st program
#  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
f1()
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
f1('Hyd')
tpl = (100 , 200 , 150)
f1(tpl)
#f1(t = (10 , 20 , 30))#error, due to * only positional arguments are allowed
'''
(10,20,15,18)
<class 'tuple'>
4

()
<class'tuple'>
0

([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
<class 'tuple'>
3

('Hyd',)
<class 'tuple'>
1

((100 , 200 , 150),)
<class 'tuple'>
1

'''

#2nd program
#  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  (Home  work)
def  avg(*a):
	#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
    return sum(a)/len(a) if len(a) != 0 else 0
# End  of  the  function
print(avg(10 , 20 , 15 , 18))
print(avg(25 , 10.8 , True))
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))
print(avg())
print(avg(25))
print(avg(3 + 4j , 5 + 6j))
tpl = (10 , 20 , 15 , 18)
print(avg(tpl))


#3rd program
def concat(*a):
    return ''.join(str(i) for i in a)
# End of the function

print(concat('Sankar', 'Dayal', 'Sarma'))              # SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))            # HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))# PythonIsAGreatLanguage
print(concat())                                        # (Empty string)
print(concat('Python'))                                # Python
print(concat(1, 2, 3))                                 # 123

#4th program
#Find  outputs (Home  work)
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10      b  :  (20 , 30 , 40)
f1(50 , 60)#a : 50      b  :  (60,)
f1(70)#a : 70      b  :  ()
f1(a = 80)#a : 80      b  :  ()
#f1(b = (10 , 20 , 30) , a = 40)#error,b cannot keyword argument
f1()#a : 25      b  :  ()
#f1(a = 10 , (20 , 30 , 40))#error, positional argument follows keyword argument
#f1(25 , b = (10 , 20 , 30))#error, b is not a keyword parameter
#f1(25 , a = (10 , 20 , 30))#a got multiple values
f1((10 , 20 , 30) , 10 , 20 , 30)#a:(10,20,30) b:(10,20,30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)#error, positional argument follows keyword argument


#5th program
#Find  outputs (Home  work)
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) #a : (10 , 20 , 30)    b  :  40
f1(50 , b = 60)#a : (50,)    b  :  60
f1(b = 70)#a : ()    b  :  70
#f1(b = 10 , a = (20 , 30 , 40))#error, a is not a keyword parameter
#f1(b = 10 , (20 , 30 , 40))#error, positional argument follows keyword argument
#f1()#error,b is a required keyword-only argument
#f1(10 , 20 , 30 , (10 , 20 , 30))#error,1 missing keyword only argument: 'b'
#f1(10 , 20 , 30 , 40)#error,1 missing keyword only argument: 'b'
#f1(25)#error,1 missing keyword only argument: 'b'
f1(10 , 20 , 30 , b = (10 , 20 , 30))#a:(10,20,30) b:(10,20,30)

#6th program
#Find  outputs (Home  work)
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50)#a  :  10          b  :  (20, 30, 40)      c  :  50
f1(60 , 70 , c = 80)#a  :  60          b  :  (70,)     c  :  80
f1(90 , c = 100)#a  :  90          b  :  ()        c  :  100
#f1(a = 1 , 2 , c = 3) #error,positional argument follows keyword argument
#f1(1 , 2 , 3)#error, missing 1 keyword argument
#f1(a = 1 , b = 2 , c = 3)# b cannot be keyword argument
#f1(a = 25 , 100 , 200 , 300 , c = 35)#error,positional argument follows keyword argument


#7th program
# Which  of  the  following  are  valid  ?  (Home  work)
def   f1(*a , *b):#not valid, only 1 * is permitted
        pass
def  f2(*a , b):#valid
        pass
def  f3(a , *b):#valid
        pass
def  f4(a , b):#valid
        pass
def    f5(a , *b , c):#valid
        pass
def   f6( * , a , *b , c):#not valid, only 1 * is permitted
       pass
def   f7(a , *b , c ,  /):#not valid, * cannot be preceeding to /
       pass


#8th program
# Find  outputs  (Home  work)
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60))
'''
([10 , 20] , {30 , 40} , (50 , 60))
<class'tuple'>
[10,20]
<class'list'>
{30,40}
<class'set'>
(50,60)
<class'tuple'>

'''


#9th program
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
Results
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

#10th program
# Find  outputs  (Home  work)
def  f1(**a):
	print('Results')
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')#Results \n Empno...25 \n Empname...Rama Rao \n Salary...10000.0 \n Gender...m
f1 () #Results



#11th program
# Find  outputs (Home  work)
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)#<class'tuple'> \n (25,10.8,'Hyd', True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)#<class 'dict'> \n {'EmpNum': 25, 'EmpName': 'Sita' , 'Salary':10000.0}


#12th program
#  Find  outputs (Home work)
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)#Emp  Number  :  25        Emp  Name  :  Sita      Salary  :     10000.0
#f1(eno = 25 , empname = 'Sita' , salary = 10000.0) #error, there is no parameter eno , salary
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)#{'empno': 25, 'ename': 'Sita', 'sal': 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)#{'eno': 25, 'empname': 'Sita', 'salary': 10000.0}


#13th program
# Find  outputs   (Home  work)
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25)#25
print()
f1('Hyd' , 10 , 20 , 30)#'Hyd' \n (10,20,30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)#10.8\n (25 , 'Hyd' , True) \n {'EmpNo': 12, 'EmpName': 'Rama  Rao', 'Salary': 10000.0}