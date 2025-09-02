# 1) Distinct vowels of string (ignoring case)
s = input("Enter mixed case string : ")
vowels = "AEIOUaeiou"
result = set(ch.upper() for ch in s if ch in vowels)
print("Distinct vowels :", "".join(sorted(result, reverse=True)))


# 2) Frequency of vowels in alphabetical order
s = input("Enter String: ")
s = s.upper()
vowels = "AEIOU"
freq = {v: s.count(v) for v in vowels if v in s}
print(freq)


# 3) Dictionary update with list of tuples
a = [('R','Red'), ('G','Green'), ('B','Blue')]
b = {'Y':'Yellow','G':'Gray'}
b.update(a)
print(b)


# 4) Updating dict with tuple-lists
a = [(10,20,30), (40,50,60), (70,80,90)]
b = {}
b.update(a)
print(b)

c = [(10,), (20,), (30,)]
b.update(c)
print(b)


# 5) Dict comprehension (cubes)
d = {x: x**3 for x in range(5)}
print(d)
print(type(d))


# 6) Dict comprehension (double values)
d = {x: 2*x for x in range(5)}
print(d)


# 7) Filter dict by condition
a = {10:'Rama', 15:'Sita', 18:'Rajesh', 17:'Kiran', 12:'Rama Rao'}
b = {k:v for k,v in a.items() if k % 2 != 0}
print(b)

c = {k:a[k] for k in a if a[k].startswith('R')}
print(c)


# 8) Function without return
def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')

print('Begin')
x = f1()
print(x)
print(type(x))
print('End')


# 9) Function returning multiple values
def f1():
    return 10, 20, 30

x = f1()
print(x)
print(type(x))

a,b,c = f1()
print(a); print(b); print(c)

print("for loop")
for k in f1():
    print(k)


# 10) Multiple return statements
def f1():
    return 10
    return 20
    return 30

print("Begin")
x = f1()
print(x)
print("End")


# 11) Function called before definition
# f1()    Error (NameError)
def f1():
    print("Hello")

print(f1())
print(f1)


# 12) Function after print statements
print("Hello")
def f1():
    print("f1 function")

print("Hi")
print(f1())
print(f1)
print("Bye")


# 13) Function object details
def f1():
    print("Hyd")
    print("Sec")
    print("Cyb")

print("Begin")
print(type(f1))
print(id(f1))
print("End")


# 14) Function add with different datatypes
def add(a,b):
    return a+b

print(add(10,20))
print(add("Hyder","abad"))
print(add(10.8,20.6))
print(add(True,False))
print(add(3+4j,5+6j))
print(add(25,10.8))
print(add([25,10.8,"Hyd"], [True,None,3+4j,"Sec"]))
# print(add(10,"20"))   #  Error


# 15) Function redefinition (last one overrides others)
def f1():
    print("No-argument function")
def f1(x):
    print("Single argument function :", x)
def f1(x,y):
    print("Two argument function :", x,y)
def f1(x,y,z):
    print("Three argument function :", x,y,z)

f1(10,20,30)
# f1(40,50)     #  Error
# f1(60)        #  Error
# f1()          #  Error


# 16) Prime number check function
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Examples
nums = [25, 11, 2, 49]
for n in nums:
    print(f"{n} -> {prime(n)}")


# 17) Program to read a number and check prime
try:
    n = int(input("Enter number : "))
    if prime(n):
        print("Prime number")
    else:
        print("Composite number")
except ValueError:
    print("Invalid input")


# 18) Employee display function
def disp(empno , ename , sal):
    print(F'Emp Number : {empno} \t Emp Name : {ename} \t Salary : {sal}')

disp(25 , 'Rama Rao' , 10000.0)
disp(35 , 'Sita' , 20000.0)
