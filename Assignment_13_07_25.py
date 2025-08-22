'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO
s = input("enter a string")
s1=s.upper()
res=""
vowels='AEIOU'
for character in s1:
    if character in vowels and character not in res:
        res += character
print(res)
output
enter a string RaMA  rAo
AO
#Write a program to print natural numbers with in a limit
n=int(input("Enter the limit of natural number"))
sum=0
for i in range(1,n+1):
    sum+=i
    a=sum/n
print(a)
#write a program to print lcm of two numbers
import math
a=int(input("enter  number"))
b=int(input("enter  number"))
lcm=int(abs(a*b)/math.gcd(a,b))
print(lcm)'''
def lcm1(x,y):
    if x>y:
        greater =x
    else:
        greater=y
    while(True):
        if ((greater %x==0) and(greater%y==0)):
            lcm=greater
            break
        greater+=1
    return lcm
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
print(lcm1(num1,num2))
