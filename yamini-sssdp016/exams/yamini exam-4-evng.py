#Q2

s=input()
b=dict()
for i in s:
        b[i]=s.count(i)
k=max(b.values())
for x in b.keys():
    if(b[x]==k):
        print(x)
        break

#Q3

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
    sort=[]
    for i in a:
        i.sort()
        sort.append(i)
    print(sort)

#Q4

def sol(n):
    sum=0
    for i in range(len(n)):
        sum+=n[i]
        sol(n[i+1:])
    return sum
n=eval(input())
print(sol(n))


#Q5

s=eval(input())
ctr=0
for word in s:
    if len(word)>2:
        if word[0]==word[-1]:
            ctr+=1
print(ctr)

#Q6

n=int(input())
k=1
for i in range(1,n+1):
    for j in range(i):           
        print(k,end=' ')
        k+=2
    print()

#Q7

n=input().upper()
n=sorted(n)
k='AEIOU'
b=dict()
for i in n:
    if i!=' ' and i in k:
        b[i]=n.count(i)
for x,y in b.items():
    print(x,y,sep='...',end=' ')
