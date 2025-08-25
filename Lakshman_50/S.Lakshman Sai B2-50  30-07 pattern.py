'''
Write  a  program  to  print  full  pyramid
	 *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''

# equilateral triangle with odd number of stars
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print(" "*(n-i), end='')
      print('*'*(2*i-1))
      break
   '''
    *
   ***
  *****
 *******
*********
'''

# equilateral triangle with odd number of stars with reverse 
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print(" "*(i), end='')
      print('*'*(2*n-2*i-1))
      break
   '''Enter number of lines: 5
*********
 *******
  *****
   ***
    *
      '''


# equilateral triangle with odd number of stars with natural numbers of stars
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print(" "*(n-i), end='')
      print('* '*i)
      break
   '''
   Enter number of lines: 5
     
    *
   * *
  * * *
 * * * *
* * * * *
'''


# equilateral triangle with odd number of stars with natural numbers of stars with reverse
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print(" "*i, end='')
      print('* '*(n-i))
      break
'''
Enter number of lines: 5
* * * * * 
 * * * *
  * * *
   * *
    *
    '''





# right angle triangle from left to right with natural numbers of '*'
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print(" "*(n-i), end='')
      print('*'*(i))
      break
   '''
   Enter number of lines: 5
     
    *
   **
  ***
 ****
*****
'''

# right angle triangle from left to right with natural numbers of '*' in reverse 
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print(" "*(i), end='')
      print('*'*(n-i))
      break
'''
Enter number of lines: 5
*****
 ****
  ***
   **
    *
    '''

# right angle triangle from left to right  with odd no.of '*'
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print(" "*(2*n-2*i),end='')
      print('*'*(2*i-1))
      break
   '''
   Enter number of lines: 5

        *
      ***
    *****
  *******
*********
'''

# right angle triangle from left to right  with odd no.of '*' with reverse
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print(" "*(2*i),end='')
      print('*'*(2*n-2*i-1))
      break
'''
Enter number of lines: 5
*********
  *******
    *****
      ***
        *
        '''







# right angle triangle from  right to left  with natural number of '*'
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print('*'*(i))
      break
   '''
   Enter number of lines: 5

*
**
***
****
*****
'''



# right angle triangle from  right to left  with natural number of '*' in reverse 
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print('*'*(n-i))
      break
   '''
   Enter number of lines: 5
*****
****
***
**
*
'''



# right angle triangle from  right to left  with odd number of '*'
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print('*'*(2*i-1))
      break
   '''
   Enter number of lines: 5

*
***
*****
*******
*********
'''


# right angle triangle from  right to left  with odd number of '*'
n=int(input("Enter number of lines: "))
for i in range(n+1):
   for _ in range(i+1):
      print('*'*(2*n-2*i-1))
      break
   '''
   Enter number of lines: 5
*********
*******
*****
***
*
'''

import math
a=[]
i=1
num=list(input("enter: "))
for i in range(1,num[i]):
   if num[i]%i==0:
      a.append(i)
      print(a)
#print(math.gcd())


num=int(input("enter: "))
a={1:"hundred", 0:None}
b={1:'ten', 2:'twenty',3:'Thirty',4:'forty',5:'fifty',6:'sixty',7:'seventy',8:'eighty',9:'ninty', 0:None}
c={1:'one', 2:'tw0',3:'Three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine', 0:None}
n=num//100
m=(num-(n*100))//10
p=num-((n*100)+(m*10))
print(n)
print(m)
print(p)
print(b[1].values)



num=int(input("enter your number: "))
prime_list=[]
for i in range(2,num+1):
   is_prime=True
   for j in range(2,i):
      if i%j==0:
         is_prime=False
         break
   if is_prime:
      prime_list.append(i)
print(prime_list)

