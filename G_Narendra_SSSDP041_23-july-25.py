import math
a = 25
print(++a) #25
print(a++1)#26
#print(a+=1)#26
print(--a)#-26
#print(a--)#Error
print(a--1)#27
print()#next line

l = []
for i in range(51):
    l.append(i)
print(l)

for i in l:
    if i%2==0:
        print(i,'is even',end=', ')
    else:
        print(i,'is odd',end=', ')


def is_prime(n):
    count = 0
    for i in range(2,int(math.sqrt(n))):
        if n%i==0:
            print(n,' is not prime')
            count +=1
        elif count>=1:
            print(n,' is not prime')
        else:
            print(n, ' is prime ')

print(is_prime(5))