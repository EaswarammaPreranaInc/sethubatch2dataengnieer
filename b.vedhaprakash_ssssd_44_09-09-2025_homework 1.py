# home works 09/09/2025 questions 


---------------------------------Tricky program with global a -------------------------------
def  f1():
    global  a
    if  a:
        print(a)
        a = a - 1
        f1()
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')

a = 3
f1()
print('End')

# outputs 
3
2
1
0
Bye
Hello
Hi
0
Bye
Hello
Hi
1
Bye
Hello
Hi
2
Bye
End

--------------------------------Without global (local a) ---------------------------------------
def  f1():
    a = 3
    if  a:
        print(a)
        a = a - 1
        f1()
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')

a = 3
f1()
print('End')

#outputs
3
3
3
Bye
Hello
Hi
2
Bye
Hello
Hi
2
Bye
Hello
Hi
2
Bye
End

-------------------------------------------------------------------
def  f1(x , y):
    if   x > 40:
        return
    x += y
    f1(x , y)
    print(x)

x = 10
f1(x , x := x + 1)
print(x)


#outputs
41
39
37
35
33
31
29
27
25
23
21
19
17
15
13
11
10

--------------------------- Recursive print both sides -----------------------------------------------

def  f1(x):
    print(x)
    if   x:
        f1(x - 1)
    print(x)

f1(3)

#outputs

3
2
1
0
0
1
2
3
------------------------------------ Infinite mutual recursion -------------------------------------------

def  f1():
    print('f1  function')
    f2()
    print('End  of  f1  function')
def  f2():
    print('f2  function')
    f1()
    print('End  of  f2  function')

f1()

#outputs
f1  function
f2  function
f1  function
f2  function
f1  function
f2  function
...
Error:

------------------------------- Function references ---------------------------------------------

def    f1():
    print('f1    function')
def    f2():
    print('f2  function')

f1()
f2()
print(f1 is f2)
f2 = f1
f2()
print(f1 is f2)
f2 = f1()
print(f2)
f2()

#outputs

f1    function
f2  function
False
f1    function
True
f1    function
None

  ...
TypeError:

-------------------------------------------------------------------------------

p = print   # assign ref
p("Hyderabad")

print = None
# print("Hello")  # would cause error
p("Hello")

#outputs
Hyderabad
Hello

-------------------------------------------------------------------

x = id
print(x(25))

p = len
print(p("Hyd"))


#outputs

(id of 25, machine-dependent, e.g., 9793856)
3

-------------------------------------------------------

def    f1(a):
    def   f2():
        return  10
    return  f2() + 20 +  a

print(f1(30))


#outputs

60

--------------------------------Nested inner functions-------------------------

def  outer():
    print('Outer  function')
    def  inner1():
        print('1st  inner  function')
    def  inner2():
        print('2nd  inner  function')
    print('Hi')
    inner2()
    print('Hello')
    inner1()
    print('Back  to  outer  function')

print('Begin')
outer()
print('Bye')


#outputs

Begin
Outer  function
Hi
2nd  inner  function
Hello
1st  inner  function
Back  to  outer  function
Bye

--------------------------------------------Globals inside nested functions----------------------------------------------

x = 10
def  outer():
    x = 20
    def   inner():
        x = 30
        print(x)
        print(globals()['x'])
    inner()
outer()
print('Bye')


#outputs

30
10
Bye

-------------------------------------------------Without redefining inner x-----------------------------------

x = 10  #  Gv
def  outer():
    x = 20
    def   inner():
        print(x)
        print(globals()['x'])
    inner()
outer()


#outputs

20
10


------------------------------------------------Using global x directly--------------------------------

x = 10
def  outer():
    def   inner():
        print(x)
    inner()
outer()


#outputs

10

-------------------------------------------Local vs inner shadowing-------------------------------

def  outer():
    x = 10
    def  inner():
        x = 20
        print(x)
        x +=  7   # Error
    print(x)
    x += 5
    inner()
    print(x)

outer()
print('Bye')


#outputs

10
...
Error


