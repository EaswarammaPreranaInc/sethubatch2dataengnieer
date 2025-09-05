#1st program
'''
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
#  Write  a  function  to  concatenate  strings  passed  to  the  function  (Home  work)
def  concat(*a):
	#Write  code  to  return  join  of  all  the  strings  passed  from  the  function  call  (1  line)
     for i in a: 
          return ''+i 
# End   of  the   function
print(concat('Sankar', 'Dayal', 'Sarma'))
print(concat('Hyd', 'Is', 'Green', 'City'))
print(concat('Python', 'Is', 'A', 'Great', 'Language'))
print(concat())
print(concat('Python'))
print(concat(1, 2, 3))


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
'''

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
f1(10 , 20 , 30 , 40 , c = 50)
f1(60 , 70 , c = 80)
f1(90 , c = 100)
f1(a = 1 , 2 , c = 3)
f1(1 , 2 , 3)
f1(a = 1 , b = 2 , c = 3)
f1(a = 25 , 100 , 200 , 300 , c = 35)