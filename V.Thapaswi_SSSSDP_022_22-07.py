# find outputs
print({10,20}|{30,40})
print({10:'Hyd',20:'Sec'}|{30:'Cyd',20:'Pune'}) # {10: 'Hyd', 20: 'Sec', 30: 'Cyd'}
#print(range(4)|range(5)) # range objects are not supported for union operation
#print([10,20]|[30,20]) # list objects are not supported for union operation

#assignment operators
a=25#ref a points to obj 25
print(a)# 25
b=a#ref b and a points to obj 25
print(b)#25
print(a is b)#true. both a and b ref points to same object
x=4#ref x points to integer obj 4
y=5# ref y points to integer obj 5
z=x+y*6#z=4+5*6=34
print(z)#34
#25=a#error. operand1 cann't be object
#a+b=x+y#error. operand1 cann't be expression

# Find outputs 
a=b=c=25
print(id(a))#prints the address of int object 25
print(id(b))#prints the address of int object 25
print(id(c))#prints the address of int object 25
print(a,b,c)#25 25 25

# Find outputs
x,y,z=25,10.8,'Hyd'
print(id(x))#address of obj 25
print(id(y))#address of obj 10.8
print(id(z))#address of obj 'Hyd'

# Find outputs
a,b,c=3,4,5
a*=b+c#27
print(a)#27

# Find outputs
a=20
a%=3+2*4#20%11=9
print(a)#9

# Find outputs
a=3
a**=4#3**4
print(a)#81

# identity operators
a=25
b=25
print(a is b)#true
print(a is not b)#False
print(a==b)#True

#find outputs
a=25
b=25.0
print(a is b)#False
print(a is not b)#True
print(a==b)#True

# Find outputs
a='Hyd'
b='Hyd' 
print(a is b)#true
print(a is not b)#false
print(a==b)#true
print()
x=[1,2,3,4]
y=[1,2,3,4]
print(x is y)#false
print(x is not y)#true
print(x==y)#true
print()
m=(1,2,3,4)
n=(1,2,3,4)
print(m is n)#true
print(m is not n)#false
print(m==n)#true
print(x==m)#false
print()

#membership operators
list=[10,20,15,12,18]
print(15 in list)#true
print(19 in list)#false
print(14 not in list)#true
print(15 not in list)#false
s='Hyd is green city'
print('is' in s)#true
print('was' in s)#false
print('g' in s)#true
print('z' in s)#false
print(' ' in s)#true
print('gre' in s)#true
print('yd i' in s)#true
print('' in s)#true
print('' not in s)#false
print()

# Find outputs
x=[1,2,3,4]
y=[1,2,3,4]
print(x==y)#true
a=(4,1,3,2)
b=(4,2,3,2)
print(a==b)#false

p={1,2,3,4}
q={4,1,3,2}
print(p==q)#true
m=range(5)
n=range(5)
print(m==n)#true

a=[10,20,30]
b=(10,20,30)
print(a is b)#false
print(a==b)#false