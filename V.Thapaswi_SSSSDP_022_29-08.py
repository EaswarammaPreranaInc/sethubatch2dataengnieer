'''
1) Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function :',x,y,z)
	   '''
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(60)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(40, 50)
def  f1(x , y , z):
	print('Three argument function : ' , x , y , z)
f1(10 , 20 , 30)



'''
2) Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
   2
  3
 5
Number  of   prime  numbers : 4
How  to  read  a  number
How  to  print  all  prime  numbers  between  2  and  user  input
print('Number  of  prime numbers:',???)
'''
from Thapaswi_22_August_28 import prime
x = int(input("Enter a number: "))
count = 0
print("Prime numbers")
for i in range(2, x + 1):
    if prime(i):
        print(i)
        count += 1
print("Number of prime numbers:", count)



#3)  Find  outputs 
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) # a : 10 <tab> b : 20 <tab> c : 30
f1(25 , 10.8 , 'Hyd') # a : 25 <tab> b : 10.8 <tab> c : 'Hyd'
f1(b = 40.7 , a = 50.2 , c = 60.5)   # a : 50.2 <tab> b : 40.7 <tab> c : 60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')  # a : 10 <tab> b : <tab> c : 'Sec'
f1(c = 3 + 4j , a = True , b = None)  # a : True <tab> b : None <tab> c : 3 + 4j
f1(25 , c = 10.8 , b = 'Hyd')  # a : 25 <tab> b : 'Hyd' <tab> c : 10.8
#f1(a = 100 , 200 , 300)  #  Error
#f1(True , None , b = 'Hyd')  # Error as there are 2 values for b
#f1(10 , 20 , x =30) # Error as there is key word value for x i.e not valid
#f1(10,20) # Error as there are less arguments 



# 4) Find  outputs 
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Emp  Number : 25 <tab> Emp  Name :  'Rama Rao' <tab> Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)  # Emp  Number : 35 <tab> Emp  Name :  'Sita' <tab> Salary : 20000.0 
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x,y,z)   # Emp  Number : 'Rama Rao' <tab> Emp  Name : 30000.0  <tab> Salary : 20



# 5)  Tricky  program
# Find  outputs 
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8])) # 62
#print(f1([6 , 7 , 8])) # error as there is only 1 argument
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # 16
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))  # error as there is only 1 argument
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))  # error as there is only 1 argument
#print({{'c' : 2 , 'b' :  4 , 'a' : 6}})  # error as set cannot hold mutable elements
#print(f1({'c' : 2 , 'a' :4,'x':6})) # error as there is only 1 argument



# 6)Identify  Error 
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a)) # Error as pA is followed by kA
#print(sorted(a , rev = True)) # error
#print(25 , 10.8 , 'Hyd' , separator = '\t') #error as there is no keyword separator
#print(25 , 10.8 , 'Hyd' , endofline = '\t') # error as there is no keyword Endofline
#print(25 ,  sep = '\t' , 10.8 , end='\t','Hyd') ## Error as PA is followed by KA



#7)  Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # a : 10 <tab> b : 20
f1(b = 30 , a = 40) # a : 40 <tab> b : 30
#f1(50 , 60) # Error only Keyword arguments should be there after *
#f1(70 , b = 80) # Error only Keyword arguments should be there after *
#f1(a=15,25) # Error as PA is followed by KA



#8) Find  outputs 
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a : 10 <tab> b : 20 <tab> c : 30
f1(a = 40 , b = 50 , c = 60) # a : 40 <tab> b : 50 <tab> c : 60
f1(c = 100 , b = 90 , a = 80)  # a : 80 <tab> b : 90 <tab> c : 100
#f1(70 , 80 , c = 90) # Error as after * there should be Keyword Argument
#f1(70 , 80 , 90)  # Error as after * there should be Keyword Argument
#f1(c = 15,b=25,35) # Error as PA is followed by KA



# 9) Identify error 
#def   f1(a  , b , *): # Error as after * there should be atleat 1 argument
       #pass



# 10) Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # a : 10 <tab> b : 20
#f1(a = 30 ,  b = 40) # Error before / there should be Positional Arguments
#f1(50 , b = 60)  # Error before / there should be Positional Arguments
#f1(a=70,80) # Error as PA is followed by KA



#11) Find  outputs 
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a : 10 <tab> b : 20 <tab> c : 30
f1(40 , 50 , c = 60) # a : 40 <tab> b : 50 <tab> c : 60
#f1(a = 70 , b = 80 , c = 90)  # Error before / there should be Positional Arguments
#f1(a = 100 , b = 110 , 120) # Error before / there should be Positional Arguments
#f1(a = 130 , 140 , c = 150) # Error as PA is followed by KA
#f1(160 , b = 170 , 180) #  Error before / there should be Positional Arguments
#f1(190 , b =200,c=210)  # Error before / there should be Positional Arguments



# 12)Find outputs
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a : 10 <tab> b : 20 <tab> c : 30 <tab> d : 40 <tab> e : 50 <tab> f : 60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 ,f=6)#error
#f1(1,2,3,4,5,f=6)#error
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error as PA is followed by KA
f1(10 , 20 , 30 , 40 , e=50,f=60)  # a : 10 <tab> b : 20 <tab> c : 30 <tab> d : 40 <tab> e : 50 <tab> f : 60



#13) Identify error 
#def  f1(/ , a , b ,  c): # Error before / there should be atleast 1 argument    after *  there should be Keyword Arguments
        #pass
#def   f2(a , b , c , *): # Error after * there should be atleast 1 argument 
        #pass



# 14) Identify  error 
#def  f4(* , a , b , c , /): # Error as cannot use '/' after '*'
        #pass




# 15) Find  outputs  
def  f1(x): # Discarded
	print('1st  function : ' , x)
def  f1(y): # Discarded
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) # 3rd  function : 10
#f1(y =20) # Error as there is no argument y in function header
#f1(x=30) # Error as there is no argument x in function header



#16) Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100)) # 150
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) # 600
print(add(100 , c = 200)) # 320
print(add(c = 100 , b = 200 , a = 300)) # 600
print(add(c = 100 , a = 200)) # 320
#print(add()) # error as there is no default value nor argument is sent
#print(add(a = 100 , 200)) # Error as PA is followed by KA
#print(add(100 ,  , 300)) # error 
#print(add(100,b,300)) # Error as there is no value of b



#17) Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d): # Error as default argument is followed by non default argument
	#pass
#def   f2(b , d , a = 10 ,c=20):
	#pass



 # 18) Find  outputs 
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20) # 20
f1() # 10
f1(a=30) # 30



# 19) Find  outputs 
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400)) # 1000
print(add(b = 100 , a = 200)) # 330
print(add(100 , 200 , d = 300)) # 610
print(add(d = 100 , a = 200 , b = 300)) # 610
#print(add(c = 100 , d = 200 , 300 , 400)) # Error PA is followed by KA
#print(add(100 , 200 , c = 300 , x = 400)) # Error as there is no argument x
#print(add()) # error required 2 arguments 



# 20) Find  outputs 
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) # 10
print(f1()) # 25
print(f2(20)) # 20
#print(f2()) # Error as argument is not sent to the function



#21) Find  outputs 
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6) # ------
disp('$') # $$$$
disp() # ****
disp(n = 5) # *****
disp(5) # 20
disp(n = 7 , ch = '%') # %%%%%%%
disp(7 , '@') # @@@@@@@
disp(7 , n = 6) # 42
#disp(ch='!',5) # Error as PA is followed by KA



#22) Find  outputs 
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) # 64
print(power(5))  # 25
print(power(b = 3 , a = 4.5)) # 4.5 ^ 3 =91.125
print(power(3 + 4j)) # (-7+24j)
print(power(True)) # 1
#def   power(b =2,a): # Error as default argument is followed by non default argument
	   #pass



#23)  Find outputs  
def   add(a , b):
	print('2-argument  function')
	return a + b
def  add(a , b , c):
	print('3-argument  function')
	return a + b + c
def  add(a  = 1 , b  = 2 , c   = 3 , d = 4):
	print('4-argument  function')
	return a + b  + c + d
# End  of  the  function
# last function will be called
print(add(10 , 20 , 30 , 40)) #4-argument  function
                            #100
print(add(50 , 60 , 70)) #4-argument  function
                         #184
print(add(80 , 90)) #4-argument  function
                    #177
print(add(100)) #4-argument  function
                #109
print(add())#4-argument  function
            #10



# 24) Find outputs  
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function : 10 <space> 20 <space> 30 
#disp(40 , 50 , 60 , 70) # Error as there are 4 arguments but required only 3
#disp(80,90)  # Error as there are 2 arguments but required only 3



#25)  Find outputs
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # 70
print(add()) # 30
print(add(a = 50)) # 70
print(add(b = 60 , a = 70)) # 130
#print(add(80,90)) #  error  only Keyword arguments should be sent to the function



# 26)Find  outputs
#def   add(a = 10 , b , c): # Error as non default argument is followed by defalut argument
        #pass
def   add( * , a = 10 , b , c ): 
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) # 120
print(add(b = 60 , c = 70))#140
print(add(c = 80 , b = 90 , a = 100))#270
#print(add(c = 25 , a = 43))#error
#print(add(1 , 2 , 3))#error
#def   add(a , b = 10 ,  c ,  * , d  , e =20,f):# Error as non default argument is followed by defalut argument
		#pass
