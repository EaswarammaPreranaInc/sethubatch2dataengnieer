# 1)  Variable  number  of  arguments  demo  program
def   f1(*t):
	print(t)
	print(type(t))
	print(len(t))
	print()
# End  of  the  function
f1(10 , 20 , 15 , 18)  #  Tuple  of  4  elements  (or)  args  are  passed  to  the  function
'''(10, 20, 15, 18)
<class 'tuple'>
4'''
f1()
'''()
<class 'tuple'>
0'''
f1([10 , 20] , (30 , 40 , 50) , {60 , 70 , 80 , 90})
'''([10, 20], (30, 40, 50), {80, 90, 60, 70})
<class 'tuple'>
3'''
f1('Hyd')
'''('Hyd',)
<class 'tuple'>
1'''
tpl = (100 , 200 , 150)
f1(tpl)
'''((100, 200, 150),)
<class 'tuple'>
1'''
#f1(t = (10 , 20 , 30))#error because 't' is keyword argument



#2) #  Write  a  function  to  determine  average  of  arguments  passed  to  the  function  
def  avg(*a):
#Write  code  to  return  average  of  arguments  passed  from  the  function  call  (single  line)
  return sum(a) / len(a) if a else 0	
# End  of  the  function
print(avg(10 , 20 , 15 , 18))                        # 63\4   15.75 
print(avg(25 , 10.8 , True))                         # 36.8\3  12.933
print(avg(10.8 , 20.6 , 15.2 , 14.9 , 9.8))          # 71.3\5   14.26       
print(avg())                                         # 0
print(avg(25))                                       # 25.0
print(avg(3 + 4j , 5 + 6j))                          # 4+5j
tpl = (10 , 20 , 15 , 18)                            # error becuase one single argument
#print(avg(tpl))                                      # unpack tuple



#3)  Write  a  function  to  concatenate  strings  passed  to  the  function 
def  concat(*a):
#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
     return ''.join(map(str, a)) if a else ''
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))                        # SankarDayalSarma
print(concat('Hyd', 'Is', 'Green', 'City'))                      # HydIsGreenCity
print(concat('Python', 'Is', 'A', 'Great', 'Language'))          # PythonIsAGreatLanguage
print(concat())                                                  # ' '
print(concat('Python'))                                          # python
print(concat(1,2,3))                                           # 1,2,3



#4) Find  outputs 
def   f1(a = 25  , *b):
        print(F'a : {a}  \t   b  :  {b} ')
# End  of  the  function
f1(10 , 20 , 30 , 40)#a : 10             b  :  (20, 30, 40)
f1(50 , 60)#a : 50             b  :  (60,)
f1(70)#a : 70             b  :  ()
f1(a = 80)#a : 80             b  :  ()
#f1(b = (10 , 20 , 30) , a = 40)#Error
f1()#a : 25            b  :  ()
#f1(a = 10 ,( 20 , 30 , 40))#Error because keyword argument after positional argument
#f1(25 , b = (10 , 20 , 30))#error because  keyword argument b not allowed
#f1(25 , a = (10 , 20 , 30))#error  becuase multiple values for argv 
f1((10 , 20 , 30) , 10 , 20 , 30)#a : (10, 20, 30)           b  :  (10, 20, 30)
#f1(a = (10 , 20 , 30) , 10 , 20 , 30)#Error because keyword argument after positional argument

#5) Find  outputs
def    f1(*a , b):
	print(F'a  :  {a}   \t   b  :  {b}')
# End  of  the  function
f1(10 , 20 , 30 , b = 40) #a:(10,20,30) b:40
f1(50 , b = 60)# a:(50,) b:60
f1(b = 70) #a:() b:70
#f1(b = 10 , a = (20 , 30 , 40)) # except 'b' nothing can be key word
# f1(b = 10 , (20 , 30 , 40)) no positional arg after key word
#f1() #error, need to pass 'b' value as it does not have any default value
#f1(10 , 20 , 30 , (10 , 20 , 30)) #a:(10,20,30) b:(10,20,30)
#f1(10 , 20 , 30 , 40) #a:(10,20,30) b:40
#f1(25) #a:() b:25
f1(10 , 20 , 30 , b = (10 , 20 , 30)) #a:(10,20,30) b:(10,20,30)


#6) Find  outputs 
def   f1(a , *b , c):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}')
# End  of  the  function
f1(10 , 20 , 30 , 40 , c = 50) #a:10    b:(20,30,40)    c:50
f1(60 , 70 , c = 80) #a:60  b:(70,) c:80
f1(90 , c = 100)#a:90   b:()    c:100
# f1(a = 1 , 2 , c = 3) #no positional arg after key word arg
#f1(1 , 2 , 3) #a:1  b:(2,)  c:30
# f1(a = 1 , b = 2 , c = 3) #error only a and c can be key word arg
# f1(a = 25 , 100 , 200 , 300 , c = 35) #no positional arg after keyword



#7)  Which  of  the  following  are  valid  ?  
''' def   f1(*a , *b): 
        pass     '''  # not valid 
def  f2(*a , b):
        pass      # valid
def  f3(a , *b):
        pass      #Valid
def  f4(a , b):
        pass     #valid 
def    f5(a , *b , c):
        pass     #valid
''' def   f6( * , a , *b , c):
        pass     # error, everything after * should be keyword and *b indicates to have positional arg which is contradicting  so error
def   f7(a , *b , c ,/):
       pass   '''  #invalid


# 8) Find  outputs  
def   f1(*a):
	print(a)
	print(type(a))
	for  x  in  a:
		print(x)
		print(type(x))
# End  of  the  function
f1([10 , 20] , {30 , 40} , (50 , 60)) 
'''([10, 20], {40, 30}, (50, 60))
<class 'tuple'>
[10, 20]
<class 'list'>
{40, 30}
<class 'set'>
(50, 60)
<class 'tuple'>'''



# 9) Variable  number  of  keyword  arguments  demo  program
def   disp(**a):
	print('Results')
	print(type(a))
	print(a)
	print()
#End  of  the  function
disp(RollNo = 10 , StudName = 'Rama  Rao')  
#Results   <class 'dict'>    {RollNo:10, StudName:'Rama Rao'}
disp(EmpNo = 25 , EmpName = 'Sita' , Salary = 10000.0)
#Results   <class 'dict'>   {EmpNo:25, EmpName='Sita',Salary:10000.0}
disp(AcNo = 30 , CustName = 'Kiran' , Balance = 20000.0 , Gender = 'm')
#Results  <class 'dict'>   {AcNo:30,CustName:'Kiran',Balance:20000.0,Gender:'m'}
disp() 
#Results  <class 'dict'>   {}

'''
<class  'dict'>
{'RollNo' : 10 , 'StudName' : 'Rama Rao'}
'''


#10)  Find  outputs 
def  f1(**a):
	print('Results')#Results
	for  k , v   in   a . items():
		print(k , v , sep = ' ... ')
# End  of  the  function
f1(Empno = 25 , Empname = 'Rama  Rao' , Salary = 10000.0 , Gender = 'm')
# Empno...25
#Empname...Rama Rao
#Salary...10000.0
#Gender...m
f1()


# 11) Find  outputs 
def   f1(*a):
	print(type(a))
	print(a)
def   f2(**a):
	print(type(a))
	print(a)
# End  of  the  function
f1(25 , 10.8 , 'Hyd' , True)#<class 'tuple'>  (25, 10.8, 'Hyd', True)
print()
f2(EmpNum = 25 , EmpName =  'Sita' , Salary = 10000.0)
#<class 'dict'>     {'EmpNum': 25, 'EmpName': 'Sita', 'Salary': 10000.0}



# 12) Find  outputs 
def   f1(empno , ename , sal):
	print(F'Emp  Number  :  {empno}  \t  Emp  Name  :  {ename}  \t  Salary  :	{sal}')
def   f2(**a):
	print(a)
# End  of  the  function
f1(empno = 25 , ename = 'Sita' , sal = 10000.0)#Emp Number: 25 Emp Name: Sita  Salary: 10000.0
# f1(eno = 25 , empname = 'Sita' , salary = 10000.0)#error, f1 does not have argument 'eno'
f2(empno = 25 , ename = 'Sita' , sal = 10000.0)# {empno : 25 , ename : 'Sita' , sal : 10000.0}
f2(eno = 25 , empname = 'Sita' , salary = 10000.0)# {eno : 25 , empname : 'Sita' , salary : 10000.0}



# 13)Find  outputs   
def    f1(a ,  *b , **c):
	print(a)
	if   b:
		print(b)
	if  c:
		print(c)
# End  of  the  function
f1(25) #25
print()
f1('Hyd' , 10 , 20 , 30) #'Hyd'  (10,20,30)
print()
f1(10.8 , 25 , 'Hyd' , True , EmpNo = 12 , EmpName = 'Rama  Rao' , Salary = 10000.0)
#10.8   (25, 'Hyd',True)      {EmpNo : 12 , EmpName : 'Rama  Rao' , Salary : 10000.0}



# 14) Find  outputs 
def   f1():
	a = 20
	print(a)
	a += 1
#End  of  the  function
a = 10
print(a) #10
a += 1
f1() #20
print(a) #11

# 15) Find  outputs 
a = 10
def   f1():
	b = 40
	print('a : ' , a) 
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a) #a:10
print('b : ' , b)#b:20
print('c : ' , c)#c:30
print()
a +=  1 
b +=  1
c +=  1
f1() #a: 11 b:40 c: 31
a +=  1
b +=  1
c +=  1
f2() #50 21 31
print('Bye') #Bye