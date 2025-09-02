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
#Program

n=input("Enter input without spaces: ")
res=int(n[0])
i=1
while(n[i]!= '='):
    if n[i]=='+':
        res+=int(n[i+1])
    elif n[i]=='*':
        res*=int(n[i+1])
    elif n[i]=='/':
        res/=int(n[i+1])
    elif n[i]=='-':
      res-=int(n[i+1])
    i=i+2
print(res)



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

n=input("Enter a number: ") # 9247

s=["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
result = ""
for i in n:
    result += s[int(i)] + " "
print(result) # Nine Two Four Seven


'''
Write  a  program  to  print  all  the  rotations  of  the  string

 1) Let  input  be     S   P  A   C   E
                               0   1   2   3   4
    What  are  the  outputs ?  --->  SPACE
	                                                  PACES
									                  ACESP
												      CESPA
												      ESPAC
                  '''

n=input("Enter a string: ") # SPACE
l=len(n)
for i in range(l):
    print(n[i:] + n[:i]) # SPACE  PACES ACESP CESPA ESPAC


'''
Write  a  program  to  print  mathematical  table  of  a  number

Let  input  be  7,
What  is  the  output ?  --->  7 * 1 = 7
                       						 7 * 2 = 14
			  								 7 * 3 = 21
												 .....
											 7 * 10 = 70
'''

n=int(input("Enter a number: ")) # 7
for i in range(1, 11):
    print(n, "*", i, "=", n*i)  
    
    
    
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


n = int(input())
for i in range(1, n+1):
    print(" " * (n - i), end="")
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()  
    
    
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


#  3878 ? ---> MMMDCCCLXXVIII 

n=int(input())

res=''
temp=n
d={1000 :  'M',900: 'CM',500 :  'D',400 : 'CD',100 : 'C',90 :  'XC',50: 'L',40: 'XL',10 :  'X',9:  'IX',5: 'V',4:'IV',1: 'I' }
i=0
for x,y in d.items():
  q=temp//x
  res+=q*y
  temp=temp%x
  i=i+1
print(res)


