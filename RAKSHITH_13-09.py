
#  How  to  iterate  generator  with  for  loop
import  time
def   f1():
	print('One')
	yield  25
	print('Two')
	yield  10.8
	print('Three')
	yield  'Hyd'
	print('Four')
# End  of  generator
g = f1()
for   x   in   g:
	print(x)
	time . sleep(1)
	print('Hello')
# End  of  for  loop
print('End')
print(g)
print(next(g))
g = f1()
print(next(g))


output:-
one
25
Hello
Two
10.8
Hello
Three
Hyd
Hello
Four
End
<generator object f1 at 1000001>
Error stop iteration 
one 
25



# Most  tricky  program
# Find  outputs(Home  work)
import  time
def   f1():
	yield  25
	yield  10.8
	yield  'Hyd'
# End  of  generator
g = f1()
print(next(g))
for  x  in   g:
	print(x)
print()
for  x  in   f1():
	print(x)
print()
gen = f1()
print(next(gen))
for  x  in   f1():
	print(x)
print(next(gen))


output:-
25
10.8
Hyd

25
10.8
Hyd

25
25
10.8
Hyd
10.8


#Find  outputs (Home  work)
import  time
g = (x * x   for    x    in    range(5))
for  y  in   g:
	print(y)
	time . sleep(2)
	print('Hello')
for  y  in   g:
	print(y)
    
    
output:-
0
Hello
1
Hello
4
Hello
9
Hello
16
Hello



# Find  outputs (Home  work)
import  time
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)
for  y  in   (x * x   for    x    in    range(5)):
	print(y)
	time . sleep(2)



output:-
0
1
4
9
16
0
1
4
9
16


#Find  outputs(Home  work)
import  time
g1 = (x * x   for  x  in  range(5))
g2 = g1
for  y  in  g1:
	print(y)
	time . sleep(2)
for  y  in  g2:
	print(y)
print(g1  is  g2)



output:-
0
1
4
9
16
True


#  Find  outputs (Home  work)
l = [x * x   for   x   in   range(5)]
print(l)
print(type(l))

s = {x * x   for   x   in   range(5)}
print(s)
print(type(s))

d = {x : x * x    for   x   in   range(5)}
print(d)
print(type(d))

g = (x * x   for   x   in   range(5))
print(g)
print(type(g))


output:-
[0,1,4,9,16]
<class 'list'>
{0,1,4,9,16}
<class 'set'>
{0:0,1:1,2:4,3:9,4:16}
<class 'dict'>
<generator object <genexpr> at 1000001>
<class 'generator'>


#  Find  outputs (Home  work)
def  f1():
	return  10
	return  20
	return  30
def  f2():
	yield  10
	yield  20
	yield  30
# End  of  the  function
print(f1())
print(f1())
print(f1())
print()
g = f2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))


output:-
10
10
10

10
20
30
Error stop iteration


#  Prove  that  there  is  no  waiting  time  for  generator
from  timeit  import   timeit
print(timeit('[x * x   for  x  in  range(500) ]'))
print(timeit('( x * x   for  x  in  range(500) )'))


output:-
18.698580199998105
0.25666819998878054



# Prove  that  there  is  no  memory  error  for  generator
import  sys
list = [x * x   for   x   in    range(10000)]
gen = (x * x   for   x   in    range(100000000000000000000000000000000000000000000000))
print(sys . getsizeof(list))
print(sys . getsizeof(gen))


output:-
85176
200


Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements

Enter   first  number  :   10
Enter   second  number  :   7
Sum : 17
Differnece :  3
Product :  70
Division : 1.4285714285714286

Enter   first  number  :   10
Enter   second  number  :   0
Sum : 10
Differnece :  10
Product :  0
Division  by zero  is  not  permitted


def f1(a,b):
    try:
        yield f'Sum : {a+b}'
        if a<b:
            yield f'Difference : {b-a}'
        else:
            yield f'Differnece : {a-b}'
        yield f'Product : {a*b}'
        yield f'Division : {a/b}'
    except:
        print('Division by zero is not possible')

a=int(input('Enter first number :'))
b=int(input('Enter second number : ')) 
for i in f1(a,b):
    print(i)
    
output:-
Enter first number :0
Enter second number : 10
Sum : 10
Difference : 10
Product : 0
Division : 0.0


Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object




def f1(a,b):
    yield a
    while a<b:
        yield a+1
        a+=1

a=int(input('Enter start value : '))
b=int(input('Enter end value : '))
for i in f1(a,b):
    print(i)

output:-
Enter start value : 1
Enter end value : 10
1
2
3
4
5
6
7
8
9
10



Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop




def fib(a):
    c,d=0,1
    while c<a:
        yield c
        c,d=d,c+d
a=int(input('Enter the last value of fibonacci series : '))
for i in fib(a):
    print(i)
print('End')
   
output:-
Enter the last value of fibonacci series:10
0
1
1
2
3
5
8
End