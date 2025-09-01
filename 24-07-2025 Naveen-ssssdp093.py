#plus operator
print(10+20)                                # 30
print(10.8+20.6)                            # 31.4
print(3+4j+5+6j)                            # 8+10j
print(True+False)                           # 1
print('Hyder'+'abad')                       # Hyderabad
print('Sankar'+'Dayal'+'Sarma')             # SankarDayalSarma
print('10'+'20')                            # 1020
print([10,20,30]+[1,2,3])                   # [10,20,30,1,2,3]
print((25,10.8,'Hyd')+(3+4j,True,None))     # (25,10.8,'Hyd',(3+4j),True,None)
#print({10,20}+{30+40})                     # error sets cannot be concatenated
#print({10:'Hyd'}+{20:'Sec'})               # error dictionaries cannot be concatenated
#print(range(4)+range(5))                   # error range objects cannot be concatenated
#print(10+'20')                             # error operand 2 should be a non-sequence as operand 1 is no sequence
#print([10,20,30]+5)                        # error list and int cannot be concatenated
#print([10,20,30]+(40,50,60))               # error list and tuple cannot be concatenated


#pipe demo
print({10,20} | {30,20})                            # {10,20,30} set can be any order
print({10:'Hyd',20:'Sec'} | {30:'Cyb',20:'Vja'})    # {10:'Hyd',20:'Vja',30:'Cyb'}
print(range(4) | range(5))                          # error range objects cannot be concatenated
print([10,20,30] | [20,40,10,50])                   # error lists cannot be concatenated with | operator


#star-demo
print(25*3)                         # 75
print(10.8*25.6)                    # 276.48
print(True*False)                   # 0
print((3+4j)*(5+6j))                # -9+38j
print(3+4j*5+6j)                    # 3+26j
print('25'*3)                       # 252525
print(3*'25')                       # 252525
print('Hyd'*4)                      # HydHydHydHyd
print([10,20,15]*2)                 # [10,20,15,10,20,15]
print((25,10.8,'Hyd',True)*3)       # (25,10.8,'Hyd',True,25,10.8,'Hyd',True,25,10.8,'Hyd',True)
#print(([10,20,15]*3.0))            # error due to float operand
#print({10,20,15}*2)                # error set cannot be repeated
#print({10:20,30:40}*2)             # error dict cannot be repeated
#print([10]*[20])                   # error due to 2nd operand is non-int


#slash operator
print(9.0/2)                    # 4.5
print(9/2.0)                    # 4.5
print(9.0/2.0)                  # 4.5
print(9/2)                      # 4.5
print(10.5/2)                   # 5.25
print(10/3)                     # 3.3333
print(10/2)                     # 5.0


#double slash
print(9//2)                 # 4
print(9.0//2)               # 4.0
print(9//2.0)               # 4.0
print(9.0//2.0)             # 4.0
print(10.5//2)              # 5.0
print(10.0//3)              # 3.0
print(10//3)                # 3
print(8.5//3)               # 2.0
print(18//4)                # 4
print(-18//4)               # -5
print(-(18//4))             # -4


#percentile
print(9%5)                  # 4
print(9.0%5)                # 4.0
print(9%5.0)                # 4.0
print(9.0%5.0)              # 4.0
print(10.5%2)               # 0.5
print(8.9%3)                # 2.9


#divbyzero

#print(7/0)  division by zero is not peritted
#print(7//0)  division by zero is not peritted 
#print(7%0)     division by zero is not peritted


#**operator

print(3**4)                # 81
print(10**-2)              # 0.01
print(4**3**2)             # 262144
print(3+4*5-32/2**3)       # 19.0


#relational operator

print(9>=5)             # True
print(9>=9)             # True
print(9>=12)            # False
print(6<=8)             # True
print(6<=6)             # True
print(6<=4)             # False
print(9!=7)             # True
print(6==8)             # False
print(True>False)       # True
print(3+4j==3+4j)       # True
print(3+4j==5+6j)       # False
print(3+4j!=5+6j)       # True
print(10==10.0)         # True
#print(3+4j>3+4j)       # complex numbers cannot be compared with >

#string-comp
print('Rama'>'Rajesh')         # True 'm'>'j'
print('Rama'<'Sita')           # True  'R'<'S'
print('Hyd'=='Hyd')            # True same strings
print('Rama'<='Ramana')        # True ''>='n'
print('Rama Rao'>='Rama')      # True ' '>=''
print('Hyd'!='Sec')            # True
print('Hyd'<'hyd')             # True 'H'<'h'

#chaining
print(10<20<30)             # True
print(10>=20<30)            # False
print(10<20>30)             # False
print(1<2>3>1)              # False
print(1<2<3<4)              # True
print(4>3>=3>2)             # True

#and operator
print(True and False)       # False
print(False and True)       # False
print(False and False)      # False
print(True and True)        # True
print(10 and 20)            # 20
print(0 and 20)             # 0
print(-25 and 0)            # 0
print('' and 25)            # Empty string
print(6j and 'Hyd')         # Hyd
print(0j and 'Hyd')         # 0j
print('Hyd' and 10.8)       # 10.8
print(10 and 20 and 30)     # 20 and 30

#or operator
print(True or False)        # True
print(False or True)        # True
print(True or True)         # True
print(False or False)       # False
print(10 or 20)             # 10
print(0 or 20)              # 20
print(-25 or 0)             # -25
print('' or 35)             # 35
print(6j or 'Hyd')          # 6j
print(0.0 or 3+4j)          # 3+4j
print('Hyd' or 10.8)        # Hyd

#not operator
print(not True)             # False
print(not False)            # True
print(not 25)               # False
print(not 0)                # True
print(not 'Hyd')            # False
print(not '')               # True
print(not -10)              # False
print(not not 'Hyd')        # True

#program
i=10
i=not i>14
print(i)                            # True
print(not(6<4 or 9>=5 and 6!=6))    # True

#assignment operator
a=25
print(a)                # 25
b=a
print(b)                # 25
print(a is b)           # True
x=4
y=5
z=x+y*6
print(z)            # 34
#25=a               # error 
#a+b=x+y            # error

#equal demo
a=b=c=25
print(id(a))        # address of object 25
print(id(b))        # address of object 25
print(id(c))        # address of object 25
print(a,b,c)        # 25 25 25

#Multiple assignment
x,y,z=25,10.8,'Hyd'
print(x)            # 25
print(y)            # 10.8
print(z)            # Hyd

#plus equal
a=7
print(a,id(a))      # 7  address of object 7
a+=5
print(a,id(a))      # 12  address of object 12

#star equal
a,b,c=3,4,5
a*=b+c          # a=a*(b+c)
print(a)        # 27

#percentile equal
a=20
a%=3+2*4        # a=a%(3+2*4)
print(a)        # 9

#double star equal
a=3
a**=4           # a=a**4
print(a)        # 81

#identify operator
a=25
b=25
print(a is b)           # True
print(a is not b)       # False
print(a==b)             # True


#assignment2
a=25
b=25.0
print(a is b)           # True
print(a is not b)       # False
print(a==b)             # True


#assignment3
a='Hyd'
b='Hyd'
print(a is b)           # True
print(a is not b)       # False
print(a==b)             # True
x=[1,2,3,4]
y=[1,2,3,4]
print(x is y)           # False
print(x is not y)       # True
print(x==y)             # True
m=(1,2,3,4)
n=(1,2,3,4)
print(m is n)           # True
print(m is not n)       # False
print(m==n)             # True
print(x==m)             # False


#assignment4
x=[1,2,3,4]
y=[1,2,3,4]
print(x==y)             # False
a=(4,1,3,2)
b=(4,2,3,1)
print(a==b)             # False
p={1,2,3,4}
q={4,1,3,2}
print(p==q)             # True
m=range(5)
n=range(5)
print(m==n)             # True


#membership operator
list=[10,20,15,12,18]
print(15 in list)           # True
print(19 in list)           # False
print(14 not in list)       # True
print(15 not in list)       # False
s='Hyd is green city'
print('is' in s)            # True
print('was' in s)           # False
print('g' in s)             # True
print('z' in s)             # False
print(' ' in s)             # True
print('gre' in s)           # True
print('yd i' in s)          # True
print('' in s)              # True
print('' not in s)          # False


# ++ and -- operator
a=25
print(++a)          # 25
#print(a++)         # error
print(a++1)         # 26
print(--a)          # 25
#print(a--)         # erro
print(a--1)         # 26
print(-a)           # -25
print(+-a)          # -25
print(-+a)          # -25


#semicolon 
print('One');        # One <Next line>
print('Two');        # Two <Next line>
print('Three');      # Three <Next line>
print('Hyd');print('Sec');print('Cyb')  # Hyd <next line> Sec <next line> Cyb <Next line>
