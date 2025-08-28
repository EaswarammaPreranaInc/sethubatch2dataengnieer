a=3+4
b=a*5
c=b-6
print(c/2)                                                      
 14.5
#

#
To print 7 table
a=int(input("enter a number"))
for i in range(a):
     print(f"{a}*{i} is{a*i}")                                                                                                              
   enter a number7
7*0 is0
7*1 is7
7*2 is14
7*3 is21
7*4 is28
7*5 is35
7*6 is42

#Transpose of a matrix
a=eval(input("enter rows :"))
b=eval(input("enter columns :"))
c=eval(input("enter numbers:"))
for i in range(a):
   for j in range(b):
      print(c[i][j],end=" ")
   print()
for j in range(b):
   for i in range(a):
      print(c[i][j],end=" ")
enter rows :2
enter columns :2
enter numbers:[[20,30],[40,50]]
20 30
40 50
20 40 30 50


# to print space 
a=input("enter a string: ")
print(a)
print(a[ : : -1])
print(a[1:]+a[0])
print(a[2:]+a[0:2])
print(a[3:]+a[0:3])                                                                                                         
  enter a string: space
space
ecaps
paces
acesp
cespa

n = 5   # number of lines

for i in range(1, n+1):
    print(" " * (n - i), end="")
    
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()
    A 
   A B 
  A B C 
 A B C D 
A B C D E

# Program to print each digit of a number in words

num = input("Enter a number: ")

digits_words = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

for digit in num:
    if digit in digits_words:
        print(digits_words[digit], end=" ")
    else:
        print("Not a digit", end=" ")
Enter a number: 5021
Five Zero Two One

#to check palindrome 
a=input("enter a string:")
if a[ : : -1]==a:
    print(f" it is a palindrome {a}")                                                                                                            
   enter a string:wow
 it is a palindrome wow

# matrix multiplication 
rows=int(input())
col=int(input())

rows1=int(input())
col1=int(input())

a=eval(input('enter nested list: '))
b=eval(input('enter nested list: '))
c = [[0 for _ in range(col1)] for _ in range(rows)]
for i in range(rows):
    for j in range(col1):
        for k in range(col):
            c[i][j]+=a[i][k]*b[k][j]
print(c)

2
3
3
2
enter nested list: [[1,2,3],[4,5,6]]   
enter nested list: [[1,2],[3,4],[5,6]]
[[22, 28], [49, 64]]

#matchsticks program
 match=21
tot=5

while(match>1):
    user=int(input('enter number in 1,2,3 or 4: '))
    comp=5-user
    match-=user+comp
    print('computer chose',comp )
    print('remaining match',match)
if(match==1):
    print('You lost !!!! Computer won thew game')

enter number in 1,2,3 or 4: 3
computer chose 2
remaining match 16
enter number in 1,2,3 or 4: 4
computer chose 1
remaining match 11
enter number in 1,2,3 or 4: 1
computer chose 4
remaining match 6
enter number in 1,2,3 or 4: 2
computer chose 3
remaining match 1
You lost!!!! Computer won thew game

#
 rows=int(input())
for i in range(1,rows+1):
    print(' '*(rows-i),end='')
    s=''
    for j in range(1,i*2):
        s+=str(j)
    print(s)
 5

    1

   123

  12345

 1234567

123456789