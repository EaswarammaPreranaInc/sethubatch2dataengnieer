x = 25
y = F'{x}'
print(y)# converts any object to str like int to str
print(type(y))# prints class str
x = 10.8
y = F'{x}'
print(y)#converts float to str 10.8
print(type(y))# prints class str
x = [10,20,30,40]
y = F'{x}'
print(y)#converts list to str [10,20,30,40]
print(type(y))#prints class str

print()
a,b,c=25,10.3,'sec'
print(f'{a} \t{b}\t{c}')
print(f'a={a}\nb={b}\nc={c}')
print(f'{a=}')
print(f'{a:}\t{b:}\t{c:}')
print()
a ,  b , c = 25 , 10.8 , 'Hyd'
print(F'{a}  \t   {b}   \t  {c}')#prints 25\t 10.8\t Hyd
print(F'a = {a}  \t  b  =  {b}  \t  c  =  {c}')#prints a=25\t b=10.8 \t c=hyd
print(F'{a=}  \t   {b=}   \t  {c=}')#prints a=25\t b=10.8 \t c=hyd
print(F'{a:}  \t   {b:}   \t  {c:}')# prints values colon is ignored
print('a  =  {a}  \t  b  =  {b}  \t  c  =   {c}')# its totally considered as string
print(F'a  =  a  \t  b  =  b  \t  c  =  c')#fstring cant be without braces
#print(F'{x =}  \t   {y =}   \t  {z =}')
print()

x = 25#
print(F'{x}')  #  25
print(F'{{x}}')   #  {x} even no.of braces  get object name
print(F'{{{x}}}')  #   {25}odd no.of braces get values
print(F'{{{{x}}}}')#{{x}}
print(F'{{{{{x}}}}}')#{{25}}
print(F'{{{{{{x}}}}}}')#{{{x}}}
print(F'{{{{{{{x}}}}}}}')#{{{25}}}
print(F'{{{{{{{{x}}}}}}}}')#{{[{x}}}}
#Raw string
print()
y='srcl is\ntextile\t city'
print(y)
print(r'srcl is\\n textile city')

try:
    x=int(input('enter 1st intiger number:'))
    y=int(input('enter 2nd intiger number:'))
    print(f'{x}+{y}=',x+y)
    print(f'{x}-{y}=',x-y)
    print(f'{x}*{y}=',x*y)
    print(f'{x}/{y}=',x//y)
    print(f'{x}%{y}=',x%y)
    print(f'{x}/{y}=',x/y)
    print(f'{x}{y}=',x**y)
    print(f'max(10,7)=',max(x,y))
    print(f'min(10,7)=',min(x,y))
    print(f'{x}^{y}=',x**y)
    import math
    print(f'sqrt{x}=',math.sqrt(x))
    print(f'gcd({x},{y})=',math.gcd(x,y))
    print(f'fact({x})=',math.factorial(x))
except:
    print('input should be in integer')
    x=input('Enter 1st input:')
    y=input('Enter 2nd input:')
    print(f'Before swap: x={x}\ty={y}')
print(f'after swap:x={y}\ty={x}')
