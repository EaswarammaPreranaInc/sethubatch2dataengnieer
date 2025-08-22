#Leap Year Program
year=int(input("Enter Year:"))
if year%4==0 and year%100!=0 or year%400==0:
    print("Leap Year")
else:
    print("Non Leap Year")
ouput:
Enter Year:2004
Leap Year
Enter Year:1900
Non Leap Year
Enter Year 2000
Leap Year
#largest number unsing if else
a=int(input("Enter 1st number:"))
b=int(input("Enter 2nd number:"))
c=int(input("Enter 3rd number:"))
if a>b and a>c:
    print("Largest number is",a)
elif b>c:
    print("Largest number is",b)
else:
        print("Largest number is",c)
output:
Enter 1st number25
Enter 2nd number35
Enter 3rd number12
Largest number is 35
#conversion of fahrenheit to celsius and vice versa using match
a=int(input("Enter 1 or 2 to for conversion"))
temp=float(input("Enetr temperature:"))
match a:
    case 1:
        f=(1.8 * temp)+ 32
        print(f,"farenheit")
    case 2:
        cel=(temp-32)/1.8

        print(cel,"celsius")
output:        
Enter 1 or 2 to for conversion1
Enetr temperature:35.5
95.9 farenheit
Enter 1 or 2 to for conversion2
Enetr temperature:95.6
35.33333333333333 celsius
#Quandrants of x and y axis 
x=int(input("Enetr x value"))
y=int(input("Enter y value"))
if x>0 and y>0:
    print("1st Quadrant")
elif x<0 and y>0:
    print("2nd Quadrant")
elif x<0 and y<0:
    print("3rd Quadrant")
elif x>0 and y<0:
    print("4th quadrant")
elif x!=0 and y==0:
    print("value of x when y is zero",x)
elif x==0 and y!=0:
    print("value of y when x is zero",y)
else:
    print("origin")
output:
Enetr x value5
Enter y value7
1st Quadrant
Enetr x value-2
Enter y value3
2nd Quadrant
Enetr x value-5
Enter y value-9
3rd Quadrant
Enetr x value2
Enter y value-4
4th quadrant
Enetr x value0
Enter y value8
value of y when x is zero 8
Enetr x value-3
Enter y value0
value of x when y is zero -3
Enetr x value0
Enter y value0
origin

#Finding the min,max and middle of given three numbers
n1 = int(input("enter 1st num"))
n2=int(input("enter 2nd num"))
n3=int(input("enter 3rd num"))
max = n1
if(n2>max):
    max=n2
    if(n3>max):
        max=n3
print("maximum",max)
min=n1
if(n2<min):
    min=n2
    if(n3<min):
        min=n3
print("minimum",min)
mid=(n1+n2+n3)-(max+min)
print("middle", mid)
Output:
Enter  1st number :10
Enter 2nd number :20
Enter 3rd number:5
maximum 20
minimum 5
middle 10








