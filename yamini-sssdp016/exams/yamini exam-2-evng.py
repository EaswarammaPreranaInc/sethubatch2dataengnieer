
#Q1

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

'''enter number in 1,2,3 or 4: 3
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
'''
#Q4
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

'''
2     
3
3 
2
enter nested list: [[1,2,3],[4,5,6]] 
enter nested list: [[1,2],[3,4],[5,6]]
[[22, 28], [49, 64]]
'''
#Q5
m=input()
n=m[::-1]
if(m==n):
    print('palindrome')
else:
    print('not palindrome')
'''
python
not palindrome
level
palindrome
'''
#Q6
def arm(n,k):
    if n > 0:
        return (n % 10) ** k + arm(n // 10,k)
    else:
        return 0

n = int(input("Enter a number: "))
k = len(str(n))
result = arm(n,k)
if result == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")

'''Enter a number: 153
153 is an Armstrong number.
'''
#Q7
rows=int(input())
for i in range(1,rows+1):
    print(' '*(rows-i),end='')
    s=''
    for j in range(1,i*2):
        s+=str(j)
    print(s)

'''
    5

    1

   123

  12345

 1234567

123456789
'''

