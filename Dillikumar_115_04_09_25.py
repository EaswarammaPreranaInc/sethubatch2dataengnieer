#5 symmetric matrices 
a=[[10 , 20 , 30] , 
[20 , 40  , 50 ],
[30 , 50 , 60]]
is_sym= True   

for i in range(len(a)):
    r=[]
    for j in range(i):
        if a[i][j]==a[j][i] :
            
          print("symmetricc ")
        else :          
          print("non symmetric ")


if is_sym:
    print("Matrix is Symmetric")
else:
    print("Matrix is Not Symmetric")
   
# undex sum in a list 
#index sum in a list 
l=[10, 30, 12, 30 , 30 , 11, 40, 30]
res=[]
for i  in  range(len(l)) :   
     if l[i]==30:
         res.append(i)
        
      
print(res)
print(sum(res))
         


s="Sankar Dayal<tab>Sarma"
words=0
vow="aeiouAEIOU"
cnt=0
vc=cc=0
sp=0
tabs=0
for ch in s:
    if ch in vow:
        vc += 1
    elif ch.isalpha():
        cc += 1
    elif ch == " ":
        sp += 1
    elif ch == "\t":
        tabs += 1
print("Vowels are :", vc, "Consonants are :", cc )
print( "spaces are :", sp)
print(tabs) 

s="Sankar Dayal<tab>Sarma"
vow = "aeiouAEIOU"
vc = 0
cc = sp=tab=0
for ch in s:
 if ("A" <= ch <= "Z") or ("a" <= ch <= "z")  :
  is_vow = False

for i in vow:
   if ch == i:
    is_vow = True
 #break
if is_vow:
  vc += 1
else:
  cc += 1
    
print("Vowels are :", vc, "Consonants are :", cc )
print( "spaces are :", sp)

#6Q
#pascal traiangle
n=5
for i in range(n):
    num=1
    print(" "*(n-i), end=" ")
    for j in range(i+1):
        print(num , end=" ")
        num=num*(i-j)//(j+1)
print()  


#7Q
# binary to decimal
bin=input("enter number : ")
dec=0
pow=0
for  i in  bin[::-1]:    
    if i=='1':
     dec=dec+(2**pow)
     pow=pow+1
print(dec)

#////1Q
def gcd(a,b):
    l1=[]
    l2=[]
    if a==0:
        return a
    else:
        while b!=0:
          a,b=b,a%b      
a=abs(int(input("enter value for a :")))
b=abs(int(input("enter value for a :")))
c=abs(int(input("enter value for a :")))
res=(gcd(a,b), c)
print(res)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a = abs(int(input("Enter value for a: ")))
b = abs(int(input("Enter value for b: ")))
c = abs(int(input("Enter value for c: ")))

res = gcd(gcd(a, b), c)
print("GCD of three numbers:", res)

#4 Q
from sys import argv 
def max_e(l1):
    max_e=l1
    for i in l1:
        if i >max_e:
            max_e=i
        return max_e
def min_e(l1):
    min_e=l1[0]
    for i in l1:
        if i <min_e:
            min_e=i
        return min_e
l1=[eval(i) for i in argv[1:]]
print("maximum element is :", max_e)
print("minimum element is :",min_e)

from sys import argv 

l1 = [int(i) for i in argv[1:]]
print("Maximum element is:", masx(l1))
print("Minimum element is:", min(l1))
