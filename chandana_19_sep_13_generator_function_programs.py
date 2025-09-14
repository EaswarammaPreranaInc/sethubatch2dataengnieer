'''
Write  a  generator  to  yield  sum , difference , product  and  division  of  2  numbers

Hint:  Use  generator  function  and  for  loop  to  iterate  elements
'''
def f1(a,b):
    print('Sum: ',end='')
    yield a+b
    print('Difference: ',end='')
    yield a-b
    print('Product: ',end='')
    yield a*b
    if b!=0:
        print('Division: ',end='')
        yield a/b
    else:
        print('Division by zero is not permitted')
a=int(input('enter first number: '))
b=int(input('enter second number: '))
for i in f1(a,b):
    print(i)
'''
o/p1:
enter first number: 2
enter second number: 5
Sum: 7
Difference: -3
Product: 10
Division: 0.4
'''
'''
o/p2:
enter first number: 2
enter second number: 0
Sum: 2
Difference: 2
Product: 0
Division by zero is not permitted'''


'''
Design  a  generator  to  yield  from  x (may  be  10)  to   y (may  be  20)

Hint:  Use  generator  function  and  for  loop

Hint:  Do  not  use  range  object
'''
def f1(x,y):
    while x<=y:
        yield x
        x+=1
x=int(input('Enter start value: '))
y=int(input('Enter end value: '))

for i in f1(x,y):
    print(i)

'''
Enter start value: 2
Enter end value: 9
2
3
4
5
6
7
8
9
'''


'''
Write  a   generator  to  generate  fibonacci  series

1) What  is  fibonacci  series ?  --->  0 , 1 , 1 , 2 , 3 , 5 , 8 , .....

2) What  is  the  formula  for  10th  term ?  --->  9th  term + 8th  term
    What  is  the  formula  for  3rd  term ?  ---> 2nd  term + 1st  term

3) What  are  the  first  two  terms ?  --->  0  and  1

4) Use  generator  function  and  for  loop
'''

def f1(n):
    x=0
    y=1
    for i in range(n):
        yield x
        x,y=y,x+y

n=int(input('Enter the last value of fibonacci series: '))
g=f1(n)
for i in g:
    print(i)
print('End')
'''
o/p:
Enter the last value of fibonacci series: 10
0
1
1
2
3
5
8
13
21
34
End
'''