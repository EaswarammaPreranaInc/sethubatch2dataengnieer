#1
n = input()
result = int(n[0])  
for i in range(1, len(n), 2):  
    op = n[i]                 
    num = int(n[i+1])          
    if op == '+':
        result = result + num
    elif op == '-':
        result = result - num
    elif op == '*':
        result = result * num
    elif op == '/':
        result = result / num
print(result)
'''
3+4*5-6/2
14.5
'''
#2
n=int(input())
s=''
rom={1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
for x,y in rom.items:
    m=n//x
    s+=m*y
    n=n%x
print(s)
'''
3878
MMMDCCCLXXVIII
'''
#3
n = input()
s = ''
num={0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
for i in n:
        for x,y in num.items():
            if int(i)==x:
                s+=y+' '
print(s)
'''
9247
Nine Two Four Seven
'''
#4
try:

    print('Enter matrix until ctrl+z')
    a = []
    while True:
        line=input().split() 
        row = [] # Empty list
        for x in line: 
            row.append (int(x))
        a. append (row) 
except:
        b=[]
        m=len(a)
        n=len(a[0])
        for j in range(n):
            row=[]
            for i in range(m):
                row.append(a[i][j])
            b.append(row)
print(b)
'''
Enter matrix until ctrl+z
3 4 5
1 2 3
1 4 5
^Z
[[3, 1, 1], [4, 2, 4], [5, 3, 5]]
'''
#5
n=input()
for i in range(len(n)):
    s=''
    s+=n[i:]+n[:i]
    print(s)
'''
SPACE
SPACE
PACES
ACESP
CESPA
ESPAC
'''
#6
n= int(input())
for i in range(11):
    print(f'{n}*{i}={n*i}')
'''  
7
7*0=0
7*1=7
7*2=14
7*3=21
7*4=28
7*5=35
7*6=42
7*7=49
7*8=56
7*9=63
7*10=70
''' 
#7
x=int(input())
p=ord('A')
for i in range(x):
    print(' '*(x-i-1),end='')
    s=''
    for j in range(p,p+i+1):
        s+=chr(j)+' '
    print(s)
'''
    A
   A B
  A B C
 A B C D
A B C D E
'''
