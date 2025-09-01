# Q1 Vowel Frequency
s = input("Enter String:")
s = s.upper()
vowels = "AEIOU"
freq = {v: s.count(v) for v in vowels if s.count(v) > 0}
print(freq)

# Q2
a = [ ('R' , 'Red') , ('G' , 'Green') , ('B' , 'Blue')]
b = {'Y' : 'Yellow', 'G' : 'Gray'}
b.update(a)
print(b)
a.update(b)

# Q3
a = [ (10 , 20 , 30) , (40 , 50 , 60) , (70 , 80 , 90)]
b = {}
b.update(a)
print(b)
c = [(10,) , (20,) , (30,)]
b.update(c)
print(b)

# Q4
d = {x : x ** 3   for    x   in  range(5)}
print(d)
print(type(d))

# Q5
d = { x :  2 * x    for    x   in   range(5) }
print(d)

# Q6
a = {10 : 'Rama' , 15 : 'Sita' , 18 : 'Rajesh' , 17 : 'Kiran' , 12 : 'Rama Rao'}
b = { k :  v  for   k , v  in   a .items()   if    k % 2 != 0}
print(b)
c = {k : a[k]   for   k   in    a    if   a[k] . startswith('R')}
print(c)

# Q7
def   f1():
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Begin')
x = f1()
print(x)
print(type(x))
print('End')

# Q8
def  f1():
	return  10 , 20 , 30
x = f1()
print(x)
print(type(x))
a , b , c =  f1()
print(a)
print(b)
print(c)
print('for  loop')
for  k   in   f1():
	print(k)

# Q9
def    f1():
        return  10
        return  20
        return  30
print('Begin')
x = f1()
print(x)
print('End')
return   100

# Q10
f1()
def   f1():
        print('Hello')
print(f1())
print(f1)

# Q11
print('Hello')
def  f1():
        print('f1  function')
print('Hi')
print(f1())
print(f1)
print('Bye')

# Q12
def    f1():
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Begin')
print(type(f1))
print(id(f1))
print('End')

# Q13
def   add(a , b):
        return  a + b
print(add(10 , 20))
print(add('Hyder' , 'abad'))
print(add(10.8 , 20.6))
print(add(True , False))
print(add(3 + 4j , 5 + 6j))
print(add(25 , 10.8))
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec']))
print(add(10 , '20'))

# Q14
def  f1():
	print('No-argument  function')
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
f1(40 , 50)
f1(60)
f1()

# Q15 Prime Number Function
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

try:
    n = int(input("Enter number: "))
    if prime(n):
        print("Prime number")
    else:
        print("Composite number")
except:
    print("Invalid input")

# Q16
def   disp(empno , ename , sal):
        print(F'Emp  Number  :  {empno} \t  Emp Name  :  {ename} \t  Salary  :  {sal}')
disp(25 , 'Rama  Rao' , 10000.0)
disp('Sita' , 20000.0 , 35)
