# Exam1
'''
Write  a  program  to  evaluate  expression  like  calculator

Let  input  be  3 + 4 * 5 - 6 / 2 =
What  is  the  output ? --->  14.5

Hint:  Use  while  loop

Iteration         a          op        b        result
------------------------------------------------------
       1               3          +          4           7   --->  'a'

	   2              7          *          5           35   --->  'a'

	   3             35         -          6           29   --->  'a'

	   4             29         /          2           14.5   --->  'a'

	   5            14.5       =          ---           ----
'''
def solve(a,b,op):
	if op=='+':
		return a+b
	elif op=='-':
		return a-b 
	elif op=='*':
		return a*b 
	elif op=='/':
		return a/b 
	elif op=='%':
		return a%b

s=input("Enter the Expression: ")
a=int(s[0])
n=len(s)
for i in range(1,len(s)+1,2):
    if i>=n :
        break
    op=s[i]
    if op=='=':
        break
    b=int(s[i+1])
    a=solve(a,b,op)
print(a)

#Q2)
d = d = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',
90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}

n=int(input("Enter number: "))
# print(len(d))
res=""
for x in d.keys():
    if n==0:
        break
    if n>=x:
        freq=n//x 
        n=n%x 
        res+=freq*d[x]
print(res)

# 3878  ---> MMMDCCCLXXVIII
'''
Write  a   program  to  print  roman  equivalent  of  a  number
1000 -  M
900  -  CM
500 -  D
400 - CD
100 -   C
90  -  XC
50  -  L
40  -  XL
10  -  X
9  -  IX
5  -  V
4  -  IV
1  -  I

1) What  is  the  output  if  input  is  3878 ? ---> MMMDCCCLXXVIII

2) What  is  the  result  of  3878 // 1000 ?  --->  3
    How  many  M's  are  concatenated  to  the  sting ?  --->  Three  becoz  3878 / 1000  is  3
    What  is  the  result  of  3878 % 1000 ?  --->  878

3) What  is  the  result  of  878 // 900 ?  --->  0
    How  many  CM's  are  concatenated  to  the  string ?  ---> Zero  becoz  878 / 900  is  0
    What  is  the  result  of  878 % 900 ?  --->  878

4) What  is  the  result  of  878 // 500 ?  ---> 1
     How  many  D's  are  concatenated  to  the  string ?  ---> One  becoz  878 / 500  is  1
     What  is  the  result  of  878 % 500 ?  ---> 378
      and  so  on
'''

#Q3)
'''
Write  a  program  to  print  each  digit  of  the  number  in  words

Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven

a = ['Zero' , 'One' , 'Two' ,....  'Nine']

Iteration     ch     int(ch)       a[int(ch)]         s
--------------------------------------------------------
                                                                     ''
     1              '9'       9               'Nine'          '' + 'Nine' + ' '

	 2             '2'       2               'Two'          'Nine ' + 'Two' + ' '

	 3             '4'       4               'Four'          'Nine Two ' + 'Four' + ' '

	 4             '7'       7               'Seven'        'Nine Two Four ' + 'Seven' + ' '
'''
words = ['zero','one','two','three','four','five','six','seven','eight','nine']
n=input("Enter number: ")
res=""
for i in n:
    res+=words[int(i)]+' '
print(res)

#Q4)
'''
Write  a  program  to  print  all  the  rotations  of  the  string

 1) Let  input  be     S   P  A   C   E
                               0   1   2   3   4
    What  are  the  outputs ?  --->  SPACE
	                                                  PACES
									                  ACESP
												      CESPA
												      ESPAC

2) What  are  the  indexes  of  SPACE ?  ---> 0  to  4
     What  are  the  indexes  of  PACES ?  ---> 1  to  4 , 0  to  0
     What  are  the  indexes  of  ACESP ?  ---> 2  to  4 , 0  to  1
     What  are  the  indexes  of  CESPA ?  ---> 3  to  4 , 0  to  2
     What  are  the  indexes  of  ESPAC ?  ---> 4  to  4 , 0  to  3

3) What  are  the  indexes  in  general ?  --->  i  to  length - 1   and   0  to  i - 1
'''
s=input("Enter string: ")
n=len(s)
for i in range(n):
    print(s[i:]+s[:i])
	
#Q5)
'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       						 7 * 2 = 14
			  								 7 * 3 = 21
												 .....
											 7 * 10 = 70
'''
n=int(input("Enter number: "))
for i in range(10):
    print(f'{n}*{i+1}={n*(i+1)}')
	
#Q6)
'''
Write a  program to print following pyramid
Input: 5

             A
            A B
           A B C
          A B C D
         A B C D E


	   i         ch
---------------------
       1         'A'

	   2         'A'  to  'B'

	   3         'A'  to  'C'

	   4         'A'  to  'D'

	   5         'A'  to  'E'
'''
n=int(input("Enter number: "))
for i in range(n):
    # n-1-i spaces 
    print(' '*(n-1-i),end='')
    for j in range(i+1):
        print(chr(j+65),end=' ')
    print()

#HW
#Find  outputs (Home  work)
a = 10
def   f1():
	b = 40
	print('a : ' , a) 
	print('b : ' , b)
	print('c : ' , c)
	print()
# End  of  f1()  function
b = 20
def    f2():
	a = 50
	print('a : ' , a)
	print('b : ' , b)
	print('c : ' , c)
# End  of  f2()  function
c = 30
print('a : ' , a) #a:10
print('b : ' , b)#b:20
print('c : ' , c)#c:30
print()
a +=  1 
b +=  1
c +=  1
f1() #a: 11 b:40 c: 31
a +=  1
b +=  1
c +=  1
f2() #50 21 31
print('Bye') #Bye