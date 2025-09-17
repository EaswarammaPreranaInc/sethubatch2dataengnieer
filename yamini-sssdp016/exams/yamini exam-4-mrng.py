#Q1
def perm(n):
   if len(n)==0:
       return [[]]
   res=[]
   for i in range(len(n)):
       curr=n[i]
       rem=n[:i]+n[i+1:]
       for j in perm(rem):
           res.append([curr]+j)
   return res
n=eval(input('enter a list: '))
print(perm(n))

#Q2

s=input().split('.')
n=[]

for i in s:
    n.extend(i.split())

b=dict()
for i in n:
        b[i]=n.count(i)

k=max(b.values())
for x in b.keys():
    if(b[x]==k):
        print(x)
        break


#Q4

def occ(n,k):
    ctr=0
    for i in n:
        if i==k:
            ctr+=1
        occ(n[i:],k)
    return ctr
n=eval(input())
k=int(input())
print(occ(n,k))

#Q5

def sub(n):
    if len(n)>0:
        s=[]
        for i in range(len(n)):
            r=n[:i]+n[i+1:]
            sub(r)
            if n[i] not in s:
                s.append(n[i])
            
        print(s)
n=input()
sub(n)

#Q6

n=int(input())
for i in range(1,n+1):
    
    print((n-i)*' ',end='')
    s=''
    if(i==1):
        s+=str(i)
    else:
        for i in range(i,0,-1):
            s+=str(i)
        s+=s[len(s)-2::-1]
    print(s)

#Q7

n=input().upper()
n=sorted(n)
print(n)
b=dict()
for i in n:
    if i!=' ':
        b[i]=n.count(i)


print(b)
