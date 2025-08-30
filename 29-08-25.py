
#1st program
# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
def  f2(x):
	print('Single  argument  function  : ' , x)
def  f3(x , y):
	print('Two  argument  function : ' , x , y)
def  f4(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1()
f2(10)
f3(10 , 20)
f4(10 , 20 , 30)

#2nd program


#3rd program
# Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)#{a: 10 , b: 20 , c: 30}
f1(25 , 10.8 , 'Hyd')#{a: 25 , b: 10.8 , c: 'Hyd'}
f1(b = 40.7 , a = 50.2 , c = 60.5)#{a: 50.2 , b: 40.7 , c: 60.5}
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')#{a: 'Cyb' , b: 'Sec' , c: 'Hyd'}
f1(c = 3 + 4j , a = True , b = None)#{a: True , b: None , c: 3 + 4j}
f1(25 , c = 10.8 , b = 'Hyd')#{a: 25 , b: 'Hyd' , c: 10.8}
#f1(a = 100 , 200 , 300)  #  Error
#f1(True , None , b = 'Hyd')# Error
#f1(10 , 20 , x = 30)# Error
#f1(10 , 20)# Error
  

#4th program
#    # Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0)#{empno: 25 , ename: 'Rama Rao' , sal: 10000.0}
disp(ename = 'Sita' , sal = 20000.0 , empno = 35)#{empno: 35 , ename: 'Sita' , sal: 20000.0}
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) #{empno: 'Rama Rao' , ename: 30000.0 , sal: 20}


#5th program
#  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5))#  23
print(f1(*[6 , 7 , 8]))#  62
#print(f1([6 , 7 , 8]))#  Error
print(f1(*{1 : 2 , 3 : 4 , 5 : 6}))#  16
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#  Error
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6}))#  Error
#print({{'c' : 2 , 'b' :  4 , 'a' : 6}})#  Error
#print(f1({'c' : 2 , 'a' : 4 , 'x' : 6}))#  Error


#6th program
# Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
print(sorted(reverse = True , a))#  Error
print(sorted(a , rev = True))#  Error there is no rev parameter
print(25 , 10.8 , 'Hyd' , separator = '\t')#  Error there is no separator parameter
print(25 , 10.8 , 'Hyd' , endofline = '\t')#Error there is no endofline parameter  
print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd')#


#7th program
# Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20)#{a: 10 , b: 20}
f1(b = 30 , a = 40)#{a: 40 , b: 30}
#f1(50 , 60)# Error
#f1(70 , b = 80)# Error
#f1(a = 15 , 25)# Error


#8th program
#Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30)#{a: 10 , b: 20 , c: 30}
f1(a = 40 , b = 50 , c = 60)#{a: 40 , b: 50 , c: 60}
f1(c = 100 , b = 90 , a = 80)#{a: 80 , b: 90 , c: 100}
#f1(70 , 80 , c = 90)# Error
#f1(70 , 80 , 90)# Error
#f1(c = 15 , b = 25 , 35)# Error


#9th program
# Identify error (Home  work)
def   f1(a  , b , *):
        pass
#*after parameter  is  not  allowed


#10th program
#  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20)#{a: 10 , b: 20}
f1(a = 30 ,  b = 40)# Error
f1(50 , b = 60)# Error
f1(a = 70 , 80)# Error


#11th program
# Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30)#{a: 10 , b: 20 , c: 30}
f1(40 , 50 , c = 60)#{a: 40 , b: 50 , c: 60}
f1(a = 70 , b = 80 , c = 90)# Error
f1(a = 100 , b = 110 , 120)# Error
f1(a = 130 , 140 , c = 150)# Error
f1(160 , b = 170 , 180)3# Error
f1(190 , b = 200 , c = 210)# Error


#12th program
# Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60)#{a: 10 , b: 20 , c: 30 , d: 40 , e: 50 , f: 60}
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6)# Error
#f1(1 , 2 , 3 , 4 , 5 , f = 6)#Error
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60)#Error
#f1(10 , 20 , 30 , 40 , e = 50 , f = 60)#Error

#13th program
# Identify error (Home  work)
def  f1(/ , a , b ,  c):#Error because / should be at the end of positional only parameters
        pass
def   f2(a , b , c , *):#Error because * should be at the end of parameters
        pass
 

#14th program
# Identify  error  (Home  work)
def  f4(* , a , b , c , /):
	        pass#Error because / should be at the end of positional only parameters

#15th program
# Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10)#10
#f1(y = 20)
#f1(x = 30)


#16th program
# Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100))# 150
print(add(100 , 200))# 330
print(add(100 , 200 , 300))# 600
print(add(100 , c = 200))# 320
print(add(c = 100 , b = 200 , a = 300))# 600
print(add(c = 100 , a = 200))# 320
#print(add())# Error
#print(add(a = 100 , 200))# Error
#print(add(100 ,  , 300))# Error
#print(add(100 ,  b , 300))# Error


#17th program
# Identify  Error
def   f1(a = 10 ,  b ,  c = 20 ,  d):#Error becoz non-default  parameters  should  be  first
	pass
def   f2(b , d , a = 10 , c = 20):
	pass


#19th program
#  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20)#20
f1()#10
f1(a = 30)#30

#20th program
# Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200))# 330
print(add(100 , 200 , 300))# 620
print(add(100 , 200 , 300 , 400))# 1000
print(add(b = 100 , a = 200))# 330
print(add(100 , 200 , d = 300))# 610
print(add(d = 100 , a = 200 , b = 300))# 610
#print(add(c = 100 , d = 200 , 300 , 400))#Error
#print(add(100 , 200 , c = 300 , x = 400))# Error
#print(add())# Error


#21th program
#  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10))#10
print(f1())#25
print(f2(20))#20
#print(f2())#Error

#22nd program
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_primes(n):
    primes = []
    for number in range(2, n + 1):
        if is_prime(number):
            primes.append(number)
    return primes
# Main program
n = int(input("Enter the value of n: "))
prime_numbers = generate_primes(n)

print("\nPrime numbers between 2 and", n, "are:")
print(prime_numbers)
print("\nTotal number of prime numbers:", len(prime_numbers))
