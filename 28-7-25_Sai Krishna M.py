#
'''
try:
    
    import math
    a = int(input("Enter the 1st integer : "))
    b = int(input("Enter the 2nd integer : "))
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} * {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')
    print(f'{a} % {b} = {a%b}')
    print(f'{a} ^ {b} = {a**b}')
    print(f'max({a},{b}) = {max(a,b)}')
    print(f'min({a},{b}) = {min(a,b)}')
    print(f'gcd({a},{b}) = {math.gcd(a,b)}')
    print(f'sqrt({a}) = {math.sqrt(a)}')
    print(f'fact({a}) = {math.factorial(a)}')
 
except ZeroDivisionError:
    print("Enter only natural numbers")
except ValueError:
    print("Accepts only integers not other datatypes")
    


a = int(input("Enter the 1st integer : "))
b = int(input("Enter the 2st integer : "))
print(f"Before Swap : {a=} \t {b=}")
a,b = b,a 
print(f"After Swap : {a=} \t {b=}")



a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))
c = eval(input("Enter 3rd input : "))

res = a if a>b and a>c else b if b>c else c 
print(f'Largest among {a},{b} and {c} is {res}')



a = eval(input("Enter 1st input : "))
b = eval(input("Enter 2nd input : "))

res = '>' if a>b else '<' if a<b else '='
print(f'Result is : {res}')



a = int(input("Enter any number : "))
res = 1 if a>0 else -1 if a<0 else 0
print(f'Result is : {res}')


a = int(input("Enter any +ve number : "))
res = "Even Number" if a%2==0 else "Odd Number" 
print(f'Result is : {res}')


l = float(input("Enter the Length of Rectangle : "))
b = float(input("Enter the Breadth of Rectangle : "))
if l==b:
    print(f'Perimeter of Square is {4*l}')
    print(f'Area of Square is {l*l}')
else:
    print(f'Perimeter of Rectangle is {2*(l+b)}')
    print(f'Area of Rectangle is {l*b}')


a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
print(f'Before Swap : {a=}\t{b=}')
temp = a 
a = b 
b = temp 
print(f'After  Swap : {a=}\t{b=}')

a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
print(f'Before Swap : {a=}\t{b=}')
a = a+b 
b = a-b 
a = a-b 
print(f'After  Swap : {a=}\t{b=}')
'''
a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
print(f'Before Swap : {a=}\t{b=}')
a = a*b 
b = a//b 
a = a//b 
print(f'After  Swap : {a=}\t{b=}')