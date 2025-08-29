#1. Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(10)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(20,30)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(40,50,60)








#2. Find  outputs  (Home  work)
def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30) # a:10<\t>b:20<\t>c:30
f1(25 , 10.8 , 'Hyd') # a:25<\t>b:10.8<\t>c:'Hyd'
f1(b = 40.7 , a = 50.2 , c = 60.5) # a:50.2<\t>b:40.7<\t>c:60.5
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb') #a  :  Cyb<\t>b  :  Sec<\t>c :  Hyd
f1(c = 3 + 4j , a = True , b = None) # a:True<\t>b:None<\t>c:(3 + 4j)
f1(25 , c = 10.8 , b = 'Hyd') # a:25<\t>b:'HYD<\t>c:10.8
#f1(a = 100 , 200 , 300)  #  Error
#f1(True , None , b = 'Hyd') # Error due to multiple values for arg 'b'
#f1(10 , 20 , x = 30) # Error due to undefined arg 'x'
#f1(10 , 20) # Error due to expected 3 args but found 2










#3. Find  outputs (Home  work)
def    disp(empno , ename , sal):
        print(F'Emp  Number : {empno:4}  \t  Emp  Name : {ename:15}  \t  Salary : {sal}')
# End  of  the  function
disp(25 , 'Rama Rao' , 10000.0) # Emp Number: 25<tab>Emp Name:Rama Rao<tab>Salary:10000.0
disp(ename = 'Sita' , sal = 20000.0 , empno = 35) # Emp Number: 35<tab>Emp Name:Sita<tab>Salary:20000.0
x = 'Rama  Rao'
y = 30000.0
z = 20
disp(x , y , z) # Emp Number:Rama Rao<tab>Emp Name:30000.0<tab>Salary:20






#4.  Tricky  program
# Find  outputs (Home  work)
def    f1(a , b , c):
	return  a + b * c
#end  of  the  function
print(f1(3 , 4 , 5)) # 23
print(f1(*[6 , 7 , 8])) # 62 
#print(f1([6 , 7 , 8])) # Error due to expected 3 but got 1 arg
print(f1(*{1 : 2 , 3 : 4 , 5 : 6})) # 16
#print(f1({'c' : 2 , 'b' :  4 , 'a' : 6})) # Error due to expected 3 but got 1 arg
#print({{'c' : 2 , 'b' :  4 , 'a' : 6}}) # Error due to there is no key
#print(f1({'c' : 2 , 'a' : 4 , 'x' : 6})) # Error due to expected 3 but got 1 arg









#5. Identify  Error (Home  work)
a = [10 , 20 , 15 , 5 , 12]
#print(sorted(reverse = True , a)) # Error due to positional arguments will be not permitted after keyword arguments
#print(sorted(a , rev = True)) # Error due to for sorted function second argument should be named as reversed not rev
#print(25 , 10.8 , 'Hyd' , separator = '\t') # # Error due to for print function argument should be named as sep not seperator
#print(25 , 10.8 , 'Hyd' , endofline = '\t') # Error due to for print function  argument should be named as end not endofline
#print(25 ,  sep = '\t' , 10.8 , end = '\t' , 'Hyd') # Error due to positional arguments will be not permitted after keyword arguments








#6. Keyword  only   arguments  demo  program
def   f1(* , a , b):
        print(F'a  :  {a}  \t  b :  {b}')
# End  of  the  function
f1(a = 10 , b = 20) # a:10<tab>b:20
f1(b = 30 , a = 40) # a:40<tab>b:30
#f1(50 , 60) # Error due to '*' operator is defined in fuction header so positional arg should be before * and keyword arg should after *
#f1(70 , b = 80) # Error due to '*' operator is defined in fuction header so positional arg should be before * and keyword arg should after *
#f1(a = 15 , 25)  # Error due to '*' operator is defined in fuction header so positional arg should be before * and keyword arg should after *







#7. Find  outputs (Home  work)
def  f1(a , * , b , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , b = 20 , c = 30) # a:10<tab>b:20<tab>c:30
f1(a = 40 , b = 50 , c = 60) # a:40<tab>b:50<tab>c:60
f1(c = 100 , b = 90 , a = 80) # a:80<tab>b:90<tab>c:100 
#f1(70 , 80 , c = 90) # Error due to '*' operator is defined in fuction header so positional arg should be before * and keyword arg should after *
#f1(70 , 80 , 90) # Error due to '*' operator is defined in fuction header so positional arg should be before * and keyword arg should after *
#f1(c = 15 , b = 25 , 35) # Error due to '*' operator is defined in fuction header so positional arg should be before * and keyword arg should after *







#8. Identify error (Home  work)
#def   f1(a  , b , *):
#        pass # * should not defined at last argument in a function





#9.  Positional  only  arguments  demo  program
def   f1(a , b , /):
        print(F'a  :  {a}  \t  b  :  {b}')
# End  of   the  function
f1(10 , 20) # a:10<tab>b:20
#f1(a = 30 ,  b = 40) # Error due to '/' operator is defined in fuction header so positional arg should be before / and keyword arg should after /
#f1(50 , b = 60) # Error due to '/' operator is defined in fuction header so positional arg should be before / and keyword arg should after /
#f1(a = 70 , 80) # Error due to '/' operator is defined in fuction header so positional arg should be before / and keyword arg should after /






#10. Find  outputs (Home  work)
def  f1(a , b , / , c):
        print(F'a  :  {a}  \t  b :  {b}  \t  c  :  {c} ')
# End  of  function
f1(10 , 20 , 30) # a:10<tab>b:20<tab>c:30
f1(40 , 50 , c = 60) # a:40<tab>b:50<tab>c:60
#f1(a = 70 , b = 80 , c = 90) # Error due to '/' operator is defined in fuction header so positional arg should be before / and keyword arg should after / 
#f1(a = 100 , b = 110 , 120) # Error due to '/' operator is defined in fuction header so positional arg should be before / and keyword arg should after /
#f1(a = 130 , 140 , c = 150) # Error due to '/' operator is defined in fuction header so positional arg should be before / and keyword arg should after /
#f1(160 , b = 170 , 180) # Error due to '/' operator is defined in fuction header so positional arg should be before / and keyword arg should after /
#f1(190 , b = 200 , c = 210) # Error due to '/' operator is defined in fuction header so positional arg should be before / and keyword arg should after /






#11. Find outputs(Home  work)
def  f1(a , b , / , c , d , * , e  , f):
        print(F'a  :  {a}  \t  b  :  {b}  \t  c  :  {c}  \t  d  :  {d}  \t  e  :  {e}  \t  f  :  {f}')
# End of the function
f1(10 , 20 , 30 , d = 40 , e = 50 , f = 60) # a:10<tab>b:20<tab>c:30<tab>d:40<tab>e:50<tab>f:60
#f1(1 , b = 2 , c = 3 , d = 4 , e = 5 , f = 6) # Error
#f1(1 , 2 , 3 , 4 , 5 , f = 6) # Error
#f1(10 , 20 , c = 30 , 40 , e = 50 , f = 60) # Error
f1(10 , 20 , 30 , 40 , e = 50 , f = 60) # a:10<tab>b:20<tab>c:30<tab>d:40<tab>e:50<tab>f:60 




#12. Identify error (Home  work)
#def  f1(/ , a , b ,  c):
#        pass # Error due to / should be preceded by positional arg not before
#def   f2(a , b , c , *):
#        pass # # Error due to * should be follwed by keyword args not before





#13. Identify  error  (Home  work)
#def  f4(* , a , b , c , /):
#	        pass # Error 





#14. Find  outputs  (Home  work)
def  f1(x):
	print('1st  function : ' , x)
def  f1(y):
	print('2nd  function : ' , y)
def  f1(z):
	print('3rd  function : ' , z)
f1(z = 10) # 3rd  function : 10
#f1(y = 20) # Error due to undefined arg 'y'
#f1(x = 30) # Error due to undefined arg 'x'








#15. Default  arguments  demo  program
def   add(a  , b = 20 , c = 30):
        return   a + b + c
#end  of  the  functiom
print(add(100)) # 150
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) # 600
print(add(100 , c = 200)) # 320
print(add(c = 100 , b = 200 , a = 300)) # 600
print(add(c = 100 , a = 200)) # 320
#print(add()) # Error due to missing args
#print(add(a = 100 , 200)) # Error PAs followed by KAs
#print(add(100 ,  , 300)) # Error
#print(add(100 ,  b , 300)) # Error due to 'b' is not defined




#16. Identify  Error
#def   f1(a = 10 ,  b ,  c = 20 ,  d):
#	pass # Error due to default args should be after normal agrs
def   f2(b , d , a = 10 , c = 20):
	pass





#17.  Find  outputs (Home  work)
def   f1(a = 10):
        print(a)
# End  of  the  function
f1(20) # 20
f1() # 10
f1(a = 30) # 30 



#18. Find  outputs (Home  work)
def  add(a , b , c = 10 , d = 20):
        return  a + b + c + d
# End  of  the  function
print(add(100 , 200)) # 330
print(add(100 , 200 , 300)) # 620
print(add(100 , 200 , 300 , 400)) # 1000
print(add(b = 100 , a = 200)) # 330
print(add(100 , 200 , d = 300)) # 610
print(add(d = 100 , a = 200 , b = 300)) # 610
#print(add(c = 100 , d = 200 , 300 , 400)) # Error due to PAs followed by KAs but here not followed
#print(add(100 , 200 , c = 300 , x = 400)) # Error due to 'x is not defined'
#print(add()) # Error due to no args



#19.  Find  outputs (Home  work)
def    f1(x = 25):
        return  x
def   f2(x):
        return  x
# End  of  the  function
print(f1(10)) # 10
print(f1()) # 25
print(f2(20)) # 20
#print(f2()) # Error due to missing value





#20. Find  outputs (Home  work)
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
#disp(ch = '!' ,  5) # Error due to PAs follwed by KAs but here not followed




#21. Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6)) # 64
print(power(5)) # 25
print(power(b = 3 , a = 4.5)) # 91.125
print(power(3 + 4j)) # (-7+24j)
print(power(True)) # 1
#def   power(b = 2 , a): # Error due to arg without value followed by arg with value but here not followed
# 	 pass




#22. Find outputs  (Home  work)
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
print(add(10 , 20 , 30 , 40)) # 4-argument  function <nextline> 100
print(add(50 , 60 , 70)) # 4-argument  function <nextline> 184
print(add(80 , 90)) # 4-argument  function <nextline> 177
print(add(100)) # 4-argument  function <nextline> 109
print(add()) # 4-argument  function <nextline> 10



#23. Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30) # 3-argument  function  :  10 20 30
#disp(40 , 50 , 60 , 70) # Error due to expected args are 3 but got 4
#disp(80 , 90) # Error due to expected args are 3 but got 2




#24. Find outputs(Home  work)
def   add(* , a = 10 , b = 20):
        return  a + b
# End of  the  function
print(add(a = 30 , b = 40)) # 70
print(add()) # 30
print(add(a = 50)) # 70
print(add(b = 60 , a = 70)) # 130
#print(add(80 , 90)) # Error



#25. Find  outputs(Home  work)
#def   add(a = 10 , b , c):
#        pass # error due to arg without value followed by arg with value but here not followed
def   add( * , a = 10 , b , c ):
        return  a + b + c
# End  of  the  function
print(add(a = 30 , b = 40 , c = 50)) # 120
print(add(b = 60 , c = 70)) # 140 
print(add(c = 80 , b = 90 , a = 100)) # 270
#print(add(c = 25 , a = 43)) # Error 
#print(add(1 , 2 , 3)) # Error
#def   add(a , b = 10 ,  c ,  * , d  , e = 20 , f):
#		pass # Error due to PAs followed by KAs but here not followed







#26.Write  a  program  to  generate  all   prime  numbers  between  2  and  n   andalso  print  how  many  prime  numbers  are  existing

def prime(n):
    count = 0
    for i in range(2,n+1):
        c = 0
        for j in range(1,i+1):
            if i % j == 0:
                c += 1
        if c == 2:
            print(i)
            count += 1
    print(f'Number of prime numbers between 2 and {n} are : {count}')
n = int(input("Enter any integer input : "))
prime(n)
 