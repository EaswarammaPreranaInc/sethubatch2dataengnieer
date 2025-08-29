# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function') # No-argument function 
def  f1(x):
	print('Single  argument  function  : ' , x)   # Single argument function : 10
def  f1(x , y):
	print('Two  argument  function : ' , x , y)   # Two argument function : 10 20 
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)   # Three argument function : 10 20 30 
Function with more than 3 arguments : (1, 2 , 3 , 4)

'''
Write  a  program  to  generate  all   prime  numbers  between  2  and  n   and
also  print  how  many  prime  numbers  are  existing

Hint:  Use  the  prime()  function  defined  in   prog3a(prime).py  but  do  not  rewrite

What  are  the  outputs  if  input  is  10  ?  --->  Prime   numbers
																		   2
																		   3
																		   5
																		   7
																		  Number  of   prime  numbers : 4
'''
How  to  read  a  number
How  to  print  all  prime  numbers  between  2  and  user  input
print('Number  of  prime numbers  :  ' ,  ???)


from prog3a import prime

n = int(input("Enter a number : "))

count = 0
print("Prime numbers")

for i in range(2, n+1):
    if prime(i):   
        print(i)
        count += 1

print("Number of prime numbers :", count)



# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)          # a : 10    b : 20    c : 30
f1(25 , 10.8 , 'Hyd')                 # a : 25    b : 10.8    c : Hyd
f1(b = 40.7 , a = 50.2 , c = 60.5)    # a : 50.2    b : 40.7    c : 60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') # a : Cyb    b : Sec    c : Hyd
f1(c = 3 + 4j , a = True , b = None)  # a : True    b : None    c : (3+4j)
f1(25 , c = 10.8 , b = 'Hyd')         # a : 25    b : Hyd    c : 10.8
f1(a = 100 , 200 , 300)        #  Error
f1(True , None , b = 'Hyd')    # Error 
f1(10 , 20 , x = 30)           #  Error 

# Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)                     # Emp  Number :   25  	Emp  Name : Rama Rao       	Salary : 10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)   # Emp  Number :   35  	Emp  Name : Sita           	Salary : 20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z)    # Emp  Number : Rama  Rao  	Emp  Name : 30000.0        	Salary : 20

#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))    # 23
print(f1(*[6 , 7 , 8])) # 62
print(f1([6 , 7 , 8]))  # Error 
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))        # 16
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))  # 14
print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))  # Error 
print({{'c' : 2 , 'b' :  4 , 'a' : 6}})    # {'c': 2, 'b': 4, 'a': 6}
print(f1({'c' : 2 , 'a' : 4 , 'x' : 6}))   # Error


# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))     # print(sorted(a, reverse=True))
print(sorted(a , rev = True))         # print(sorted(a, reverse=True))
print(25 , 10.8 , 'Hyd' , separator = '\t')   # print(25, 10.8, 'Hyd', sep='\t')
print(25 , 10.8 , 'Hyd' , endofline = '\t')   # print(25, 10.8, 'Hyd', end='\t')
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')   # print(25, 10.8, 'Hyd', sep='\t', end='\t')


# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)   # a : 10     b :  20
f1(b = 30 , a = 40  ) # a : 40     b : 30
f1(50 , 60)      # Error 
f1(70 , b = 80)  # Error 
f1(a = 15 , 25)  # Error


#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)      # a : 10 	 b : 20 	 c : 30
f1(a = 40 , b = 50 , c = 60)  # a : 40 	 b : 50 	 c : 60
f1(c = 100 , b = 90 , a = 80) # a : 80 	 b : 90 	 c : 100
f1(70 , 80 , c = 90)   # Error 
f1(70 , 80 , 90)      # Error 
f1(c = 15 , b = 25 , 35)   # Error

# Identify error (Home  work)
def   f1(a  , b , *): Error 
        pass

#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # a : 10    b : 20
f1(a = 30 ,  b = 40) # Error 
f1(50 , b = 60) # Error 
f1(a = 70 , 80) # Error


# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a  :  10 	 b :  20 	 c  :  30
f1(40 , 50 , c = 60) # a  :  40 	 b :  50 	 c  :  60
f1(a = 70 , b = 80 , c = 90) # Error 
f1(a = 100 , b = 110 , 120) # Error 
f1(a = 130 , 140 , c = 150) # Error 
f1(160 , b = 170 , 180) # Error 
f1(190 , b = 200 , c = 210) # Error

# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a  :  10 	 b  :  20 	 c  :  30 	 d  :  40 	 e  :  50 	 f  :  60
f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error 
f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error 
f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error 
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) #a  :  10 	 b  :  20 	 c  :  30 	 d  :  40 	 e  :  50
f  :  60


# Identify error (Home  work)
def  f1(/ , a , b ,  c): # Error 
        pass
def   f2(a , b , c , *): # Error 
        pass


# Identify  error  (Home  work)
def  f4(* , a , b , c , /): #Error 
	        pass


# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)  # 3rd function  : 10 
f1(y = 20)  # Error 
f1(x = 30)  # Error

# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))        # 150
print(add(100 , 200))  # 330
print(add(100 , 200 , 300)) # 600
print(add(100 , c = 200))   # 320
print(add(c = 100 , b = 200 , a = 300)) # 600
print(add(c = 100 , a = 200))   # 320
print(add())   # Error 
print(add(a = 100 , 200))  # Error 
print(add(100 ,  , 300))   # Error 
print(add(100 ,  b , 300)) # Error


# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d): # Error 
	pass
def   f2(b , d , a = 10 , c = 20): # correct No Error 
	pass

#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)    # 20
f1()      # 10
f1(a = 30) # 30


# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))       # 330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400))  # 1000
print(add(b = 100 , a = 200))      # 330
print(add(100 , 200 , d = 300))    # 610
print(add(d = 100 , a = 200 , b = 300))   # 610
print(add(c = 100 , d = 200 , 300 , 400)) # Error 
print(add(100 , 200 , c = 300 , x = 400)) # Error 
print(add())    # Error


#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) # 10
print(f1())   # 25
print(f2(20)) # 20
print(f2())   # Error


# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)  # ------
disp('$')      # $$$$
disp()         # ****
disp(n = 5)    # *****
disp(5)        # 20
disp(n = 7 , ch = '%')  # %%%%%%%
disp(7 , '@')   # Error 
disp(7 , n = 6) # 42
disp(ch = '!' ,  5) # Error


# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) # 64
print(power(5))     # 25
print(power(b = 3 , a = 4.5))  # 91.125
print(power(3 + 4j))  # (-7+24j)
print(power(True))   # 1
def   power(b = 2 , a):  # Error 
 	 pass


# Find outputs  (Home  work)
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
print(add(10 , 20 , 30 , 40))  # 4-argument  function
100
print(add(50 , 60 , 70))    # 4-argument  function
184
print(add(80 , 90))    # 4-argument  function
177
print(add(100))   # 4-argument  function
109
print(add())     # 4-argument  function
10

# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :   10 20 30
disp(40 , 50 , 60 , 70) # Error 
disp(80 , 90) # 3-argument  function  :   80 90 25


# Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40))   # 70
print(add())    # 30
print(add(a = 50))   #  70
print(add(b = 60 , a = 70))  # 130
print(add(80 , 90))   # Error


# Find  outputs(Home  work)
def   add(a = 10 , b , c):
        pass
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50))   # 120
print(add(b = 60 , c = 70))     # 140
print(add(c = 80 , b = 90 , a = 100))  # 270
print(add(c = 25 , a = 43))    # Error 
print(add(1 , 2 , 3)) # Error 
def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f): # Error 
		pass




f1(10 , 20)  # Error