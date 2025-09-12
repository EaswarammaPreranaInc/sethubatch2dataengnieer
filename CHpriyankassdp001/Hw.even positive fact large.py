#check a number positive or negative

a=int(input("enter a number: "))
if a>0:
    print(a,"is the positive number ")
else:
    if a<0:
        print(a,"is the negative number ")
    else:
       print(a,"is zero")


#check the number is even or odd


a=int(input("enter a number: "))
if a%2==0:
    print(a,"is the even number")
else:
    print(a,"is the odd number ")

#check the number is divisble by 5 and 11

a= int(input("enter a number: "))
if a%5==0 and a%11==0:
    print(a,"it is divisible by 5 and 11 ")
else:
    print(a, "it is not divisible by 5 and 11 ")


#find the largest number in three numbers


a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))
if a>b and a>c:
    print(a,"is the largest number ")
elif b>c:
    print(b,"is the largest number ")
else:
    print(c,"is the largest number ")


# find the largest number in another way


a,b,c=[eval(x) for x in input("enter three values").split()]
if a>b and a>c:
    print(a,"is the largest number ")
elif b>c:
    print(b,"is the largest number ")
else:
   print(c,"is the largest number ")


#check whether year is leap year or not

a=int(input("enter a any year"))
if a%4==0 and a%100!=0 or a%400==0:
    print(a,"is the leap year")
else:
    print("its Not leap year")


# print 1-10 number by loop

for i in range(1,11):
    print(i)

#write a prog for table 

a=int(input("enter any number for table "))
for i in range(1,21):
    print(f'{a}*{i}={a*i}')



# factorial of number


a=int(input("enter a number"))
b=1
for i in range(1,a+1):
    b=b*i
print(b)

from math import factorial
a=int(input("enter any number"))
fact=1
fact=fact*factorial(a-1)
print(factorial)