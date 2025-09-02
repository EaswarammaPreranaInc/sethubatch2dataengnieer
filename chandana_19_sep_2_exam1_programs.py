'''
Write  a  program  to  evaluate  expression  like  calculator

Let  input  be  3 + 4 * 5 - 6 / 2 =
What  is  the  output ? --->  14.5

Hint:  Use  while  loop

Iteration         a          op        b          result
----------------------------------------------------------
       1          3          +          4           7   --->  'a'

	   2          7          *          5           35   --->  'a'

	   3          35         -          6           29   --->  'a'

	   4          29         /          2           14.5   --->  'a'

	   5          14.5       =          ---          ----
'''

x=input('Enter any expression terminated by =  :  ')
x=x.replace('+',' + ').replace('-',' - ').replace('*',' * ').replace('/',' / ').replace('=',' = ')
y=x.split()
i=0
a=float(y[i]) 
i+=1
while y[i]!='=':
	op=y[i]
	b=float(y[i+1])
	if   op=='+':
		a=a+b
	elif op=='-':
		a=a-b
	elif op=='*':
		a=a*b
	elif op=='/':
		a=a/b
	i+=2
print('Result  :  ', a)

'''
o/p:
Enter any expression terminated by =  :  3+4*5-6/2=
Result  :   14.5'''


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
num = int(input('Enter a number :  '))
roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
			(100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        	(10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
result = ''
for x,y in roman:
    count = num // x
    result += y * count
    num %= x
print('roman Equivalent:',result)
'''
o/p:
Enter a number :  3878
roman Equivalent: MMMDCCCLXXVIII'''


'''
Write  a  program  to  print  each  digit  of  the  number  in  words

Let  input  be  9247
What  is  the  output  ?  ---> Nine  Two  Four  Seven

a = ['Zero' , 'One' , 'Two' ,....  'Nine']

Iteration     ch     int(ch)       a[int(ch)]         s
--------------------------------------------------------
                                                                     ''
     1        '9'       9            'Nine'         '' + 'Nine' + ' '

	 2        '2'       2            'Two'          'Nine ' + 'Two' + ' '

	 3        '4'       4            'Four'         'Nine Two ' + 'Four' + ' '

	 4        '7'       7            'Seven'        'Nine Two Four ' + 'Seven' + ' '
'''

a = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
n = input("Enter a number: ")
result = ''
for i in n:                          
    x = int(i)                    
    result = result + a[x] + ' '             
print(result) 
'''
o/p:
Enter a number: 6589
Six Five Eight Nine 
'''



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


a = input("Enter a string: ")
n = len(a)
print("rotations")
for i in range(n):
    result = a[i:] + a[:i]   
    print(result)

'''
Enter a string: space
rotations
space
paces
acesp
cespa
espac
'''


'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       						 7 * 2 = 14
			  								 7 * 3 = 21
												 .....
											 7 * 10 = 70
'''

x=int(input("Enter a number: "))
for i in range(1,11):
	print(F'{x} * {i} = {x*i}')	

'''
Enter a number: 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
'''



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

n = int(input('How many lines?: '))
for i in range(1, n+1):  
    print(" "*(n-i), end="")      
    for j in range(i):
        print(chr(ord('A')+j), end=" ")  
    print()   
'''
How many lines?: 6
     A 
    A B
   A B C
  A B C D
 A B C D E
A B C D E F
'''