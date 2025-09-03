#assignment1
if ():
    print('One')
    print('Two')
    print('Three')
else:
 if []:             # if cannot be indented with else, space bar needed before if
    print('Four')
    print('Five')
    print('Six')
 else:               # else should be indented with if
  if {}:
    print('Seven')
    print('Eight')
    print('Nine')
  else:
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Bye')



#determine a number is even or odd with if statement
try:
    n=int(input('Enter any integer:'))
    if n%2==0:
        print('Even number')
    else:
        print('Odd number')
except:
    print('Input should be integer')



#assignment
if(10,20,30):               # True due to non-empty tuple
    print('Hyd')            # Hyd
    print('Sec')            # Sec
    print('Cyb')            # Cyb
else:
    print('One')
    print('Two')
    print('Three')
print("Bye")                # Bye




#assignment
if():                           # False due to non-empty tuple
    print('Hyd')
    print('Sec')
    print('Cyb')
else:
    print('One')            # One
    print('Two')            # Two
    print('Three')          # Three
print('Bye')                # Bye



#assignment3
if{10:20,30:40}:            # True due to non-empty dictionary
    print('Hyd')            # Hyd
    print('Sec')            # Sec
    print('Cyb')            # Cyb
print('Bye')                # Bye



#assignment4

if { }:                     # False due to empty dictionary
    print('Hyd')
    print('Sec')
    print('Cyb')
print('Bye')                # Bye



#print month name for input month number by using if and elif
month_num = int(input("Enter month number (1 to 12): "))
if month_num == 1:
    print("Month: January")
elif month_num == 2:
    print("Month: February")
elif month_num == 3:
    print("Month: March")
elif month_num == 4:
    print("Month: April")
elif month_num == 5:
    print("Month: May")
elif month_num == 6:
    print("Month: June")
elif month_num == 7:
    print("Month: July")
elif month_num == 8:
    print("Month: August")
elif month_num == 9:
    print("Month: September")
elif month_num == 10:
    print("Month: October")
elif month_num == 11:
    print("Month: November")
elif month_num == 12:
    print("Month: December")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")



#print digit in words with else and if(do not use elif)
try:
    digit = int(input("Enter a digit (0 to 9): "))
    if digit == 0:
        print("Zero")
    else:
        if digit == 1:
            print("One")
        else:
            if digit == 2:
                print("Two")
            else:
                if digit == 3:
                    print("Three")
                else:
                    if digit == 4:
                        print("Four")
                    else:
                        if digit == 5:
                            print("Five")
                        else:
                            if digit == 6:
                                print("Six")
                            else:
                                if digit == 7:
                                    print("Seven")
                                else:
                                    if digit == 8:
                                        print("Eight")
                                    else:
                                        if digit == 9:
                                            print("Nine")
                                        else:
                                            print("Not a digit")
except:
        print('Input should be an integer')



#test year is leap year or not
try:
    year=int(input('Enter 4-digit year:'))
    if year %4 ==0 and year % 100!=0 or year % 400==0:
        print('Leap year')
    else:
        print('Not a leap year')
except:
    print('Input should be an integer')



#determine largest of three numbers with if and else
try:
    a=eval(input('Enter 1st input:'))
    b=eval(input('Enter 2nd input:'))
    c=eval(input('Enter 3rd input:'))
    if a>b>c:
        print('Largest number :',a)
    elif b>c:
        print('Largest number:',b)
    else:
        print('Largest number :',c)
except NameError:
    print('Input string should be in quotes')
except TypeError:
    print('Input can not be a complex number')



#celsius temperature to farenheit and vice versa
try:
    ch=int(input('Enter 1 to convert celsius to farenheit and 2 to convert farenheit to celsius'))
    if ch==1:
        c=float(input('Enter cesius temperature:'))
        print('Farenheit Equivalent :',1.8*c+32)
    elif ch==2:
        f=float(input('Enter farenheit temperature:'))
        print(F'celsius equivalent:{(f-32)/1.8:.2f}')
    else:
        print('Invalid input')
except:
    print('Input should be a number')



#quadrant x-axis and y-axis or origin
try:
    x=float(input('Enter value of x co-ordinate:'))
    y=float(input('Enter value of y co-ordinate:'))
    if x>0 and y>0:
        print('1st quadrant')
    elif x<0 and y>0:
        print('2nd quadrant')
    elif x<0 and y<0:
        print('3rd quadrant')
    elif x>0 and y<0:
        print('4th quadrant')
    elif x!=0 and y==0:
        print('X axis')
    elif x==0 and y!=0:
        print('Y axis')
    else:
        print('Origin')
except:
    print('Input should be a number')



#determine largest,smallest and middle of three numbers
try:
    a=float(input('Enter first input:'))
    b=float(input('Enter second input:'))
    c=float(input('Enter third input:'))
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    min=a
    if b<min:
        min=b
    if c<min:
        min=c
    mid = (a+b+c)-(max+min)
    print('Largest input:',max)
    print('Smallest input:',min)
    print('Middle input:',mid)
except NameError:
    print('Input string should be in quotes')
except TypeError:
    print('Input can not be a complex number')



#determine three sides form a triangle or not
import math
try:
    a=float(input('Enter 1st side:'))
    b=float(input('Enter 2nd side:'))
    c=float(input('Enter 3rd side:'))
    if a+b>=c and b+c>=a and c+a>=b:
        if a==b==c:
            print('Equilateral triangle')
            area=math.sqrt(3)/4*a*a
            print(F'Area:{area:.2f}')
        elif a==b or b==c or a==c:
            print('Isoscles triangle')
            p=a+b+c
            print(F'Perimeter:{p}')
        else:
            print('Scalene triangle')
            s=(a+b+c)/2
            area=math.sqrt(s*(s-a)*(s-b)*(s-c))
            print(F'Area:{area:.2f}')
            print(F'Perimeter:{2*s}')
    else:print('Not a triangle')
except:
    print('Input should be a number')



#determine roots quadratic equation
import math
a=float(input('Enter value of a:'))
if a==0:
    print('Value of a can not be 0')
    exit()
b=float(input('Enter value of b:'))
c=float(input('Enter value of c:'))
disc=b**2-4*a*c
if disc>0:
    print('Roots are real and distinct')
    roots1=(-b+math.sqrt(disc)/(2*a))
    roots2=(-b-math.sqrt(disc)/(2*a))
    print(F'Root 1:{root1:.2f}')
    print(F'Root 2:{root2:.2f}')
elif disc<0:
    print('Roots are imaginary or complex')
    real=-b/(2*a)
    imag=math.sqrt(-disc)/(2*a)
    print(F'Root1:{real}+{imag}j')
    print(F'Root2:{real}-{imag}j')
else:
    print('Roots are real and equal')
    root=-b/(2*a)
    print(F'Root1:{root}')
    print(F'Root2:{root}')



#centre of origin and radius is 'r'
import math
x=float(input('Enter value of x:'))         # 3
y=float(input('Enter value of y:'))         # 4
r=float(input('Enter radius of circle:'))   # 5
d=math.sqrt(x**2+y**2)                      # 5
if d>r:
    print('point is outside the circle')
elif d>r:
    print('Point is inside the circle')
else:
    print('Point is on the circle')



#Match statements

#day of the week with match..case
try:
    m=int(input('Enter anty day number(1-7):'))
    match m:
        case 1:
            print('Monday')
        case 2:
            print('Tueday')
        case 3:
            print('Wednesday')
        case 4:
            print('Thursday')
        case 5:
            print('Friday')
        case 6:
            print('Saturday')
        case 7:
            print('Sunday')
        case _:
            print('Invalid day number')
    print('Bye')
except:
    print('Input should be an integer')



#assignmet
m=4
match m:
    case 1:
        print('One')        
    case 2:
        print('Two')
    case 3:
        print('Three')
print('Bye')                # Bye


#assignment2
m=2
match m:
    case 1:
        print('One')
#    case _:                  # error case _ cannot be in middle of the match
        print('Hello')
    case _:                  # valid
        print('Bye')
print('End')


#assignment3
m=1
match m:
    case 1:
        print('Hyd')        # Hyd
    case 1:                 # Not executed as 1st case is already executed
        print('Sec')
    case 1:                 # Not executed as 1st case is already executed
        print('Cyb')
print('Bye')                # Bye



#assignment4
ch='B'
match ch:
    case 'A':
        print('Apple')
    case 'B':
        print('Book')                   # Book
    case 'C':
        print('Cafe')
    case _:
        print('None of the above')
print('Bye')                            # Bye



#assignment5
x=eval(input('Enter any number:'))
match x:
    case 7 | -6 | 0:            # Executed when 'x' is 7,-6 (or) 0
        print('Hyd')
        print('Sec')
        print('Cyb')
    case -10 | 15:              # Executed when 'x' is -10 or 15
        print('One')
        print('Two')
        print('Three')
    case _:                     # Executed when 'x' is none of the above 5 values
        print('India')
        print('China')
        print('Usa')
print('Bye')



#assignment6
a=[10,20,15,18]
for i in range(len(a)):
    a[i] += 1
print('a:',a)               # [11,21,16,19]
b=[10,20,15,18]
for x in b:
    x += 1
print('b:',b)               # [10,20,15,18]



#electricity bill
try:
    units=int(input('Enter units:'))
    match units // 100:
        case 0: 
            cost = units*3.00
        case 1:
            cost = 100*3.00+(units-100)*3.50
        case 2 | 3:
            cost = 100*3.00+100*3.50+75*4.00
        case 4 | 5 |6:
            cost = 100*3.00+100*3.50+200*4.00+(units-400)*4.50
        case _:
            print('Hello')
            cost = 100*3.00*100*3.50+200*4.00+300*4.50+(units-700)*5.00
    print('Bill amount :',cost)
except ValueError:
    print('Invalid input,please enter a vaild integer')



# loops statements

#fibonacci
x=int(input('Enter value of x :'))
if x==0:
    print(0)                        # print 0 if input is 0     
else:
    a=0                             # First term of the series
    b=1                             # 2nd term of the series
    print('Fibonacci Series')
    print(a)                        
    print(b)                        
    c=a+b
    while c<=x:                     # Repeat until c > x
        print(c)                    # Each term from 3rd term
        a=b
        b=c
        c=a+b



#infinite loop

while True:          # if True loop is infinite if False it is not executed
    print('Hello')
print()



#assignment
for x in [10,20,15,18]:         # X in each element of list
    print(x)                    # 10 <next line> 20 <next line> 15 <next line> 18
print()
for ch in 'Hyd':                # ch is each character of sring 'Hyd'
    print(ch)                   # H <next line> y <next line> d <next line>
print()
for x in range(5):              # 'x' is each element of range object
    print(x)                    # 0 <next line> 1 <next line> 2 <next line> 3 <next line> 4 <next line>



#assignment2
for x in {10:20,30:40,50:60}.keys():         # 'x' is each element of the list in dict_keys object
    print(x)                                 # 10 <next line> 30 <next line> 50 <next line>
print()
for x in {10:20,30:40,50:60}.values():       # 'x' is each element of the list in dict_values object
    print(x)                                 # 20 <next line> 40 <next line> 60 <next line>
print()
for x in {10:20,30:40,50:60}.items():        # 'x' is each element of the list in dict_items object
    print(x)                                 # (10,20) <next line> (30,40) <next line> (50,60) <next line>
for x in {10:20,30:40,50:60}:                # 'x' is each element of the list in dict_keys object
    print(x)                                 # 10 <next line> 30 <next line> 50 <next line>



#assignment3
a={10:20,30:40,50:60}
for x,y,in a.items():               # x and y elements of each tuple in the list of dict_items object
    print(x,y,sep='...')
for x,y in a:                       # error two variables are not permitted as keys() method is executed by default
    print(x,y)
for x,y in {10:20,30:40,50:60}:     # error two variables are not permitted as keys() method is executed by default
    print(x,y,sep='...')

#assignment4
for x in 123:   # error loop cannot be iterate throw non-sequence
    print(x)


#assignment 5
for x in ():                # Not executed due to empty tuple
    print(x)
for x in []:                # Not executed due to empty list
    print(x)
for x in {}:                # Not executed due to empty dictionary
    print(x)
for x in set():             # Not executed due to empty set
    print(x)
for x in '':                # Not executed due to empty string
    print(x)
for x in range(10,10):      # Not executed due to empty range object
    print(x)
for x in range():           # error range can be 0,2.. not 0
    print(x)
for x in (25):              # error loop cannot throw iterate
        print(x)



#nested loop demo
for i in range(1,4):
    for j in range(1,5):
        print(i,j)
    print('Hello')
print('Bye')

#output
'''
1 1
1 2
1 3
1 4
Hello
2 1
2 2
2 3
2 4
Hello
3 1
3 2
3 3
3 4
Hello
Bye
'''

#assignment
a=[25,10.8,'Hyd',True]
print('Indexed based for loop')
for i in range(len(a)):             # to print each element and the corresponding index
    print(i,a[i],sep='...')         # print i and a[i] where i varies from 0 to len-1



#reverse order 
a=[25,10.8,'Hyd',True]
print('Indexed for loop')
for i in range(1,len(a)+1):         # to print each element of list in reverse order
    print(a[-i])                    # print a[-i] where i varies from 1 to len



#add-list
a=eval(input('Enter 1st list:'))
b=eval(input('Enter 2nd list:'))
c=[]
small=min(len(a),len(b))            # smallest list length
for i in range(small):              # add list 'a' and 'b' and store results in list 'c'
    c.append(a[i]+b[i])
print('3rd list:',c)



#part of list
a=[25,10.8,'Hyd',True,3+4j,None,'Sec']
for i in range(2,5):                        # prints elements from indexes 2 to 4 of list 'a'
    print(a[i])                             # Hyd <next line> True <next line> 3+4j <next line>



#assignment
a=[10,20,15,18]
for i in range(len(a)):
    a[i]+=1
print('a:',a)               # [11,21,16,19]
b=[10,20,15,18]
for x in b:
    x+=1
print('b:',b)               # [10,20,15,18]



#pyramid
n=int(input('How many lines?:'))
s=n-1
for i in range(1,n+1):
    print(' '*s,end='')                 # print 's' number of spaces 
    s-=1                                # decrements number of spaces
    print('*'*(2*i-1))                  # prints 2*i-1 number of *'s'



# break,continue,pass,exit()

#assignment1
for i in range(1,8):
    print(i)
    if i%3==0:
        continue
    else:
        print('Sec')
    print('Hello')
print('Outside loop')

# output
'''
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside loop
'''


#assignment2
if():
    print('Hyd')
    continue      # continue cannot be used without loop
    print('Sec')



#Break program
for i in range(1,8):
    print(i)
    if i%3==0:
        break
    else:
        print('Sec')
    print('Hello')
print('Outside loop')


#output
'''
1
Sec 
Hello
2
Sec 
Hello
3
Outside loop
'''



#assignment
if(10,20,30):
    print('Hyd')
    break           # break cannot be used without loop
    print('Sec')



#pass function
for i in range(1,8):
    print(i)
    if i %3==0:
        pass
        print('Hyd')
    else:
        print('Sec')
    print('Hello')
print('Outside loop')


#output
'''
1
Sec
Hello
2
Sec
Hello
3
Hyd
Hello
4
Sec
Hello
5
Sec
Hello
6
Hyd
Hello
7
Sec
Hello
Outside loop
'''



#exit function
for i in range(1,8):
    print(i)
    if i%3==0:
        exit()      # stops execution
    else:
        print('Sec')
    print('Hello')
print('Outside loop')

#output
'''
1
Sec 
Hello
2 
Sec
Hello
3
'''

#for-else 1
for i in range(1,8):
    print(i)
    if i%3==0:
        continue
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')

#output
'''
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
else suite
Outside loop
'''


#for-else 2
for i in range(1,8):
    print(i)
    if i%3==0:
        break
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')


#output
'''
1
Sec 
Hello
2
Sec
Hello
3
'''


#for else 3
for i in range(1,8):
    print(i)
    if i==8:
        break
    else:
        print('Sec')
    print('Hello')
else:
    print('else suite')
print('Outside loop')

#output
'''
1
Sec
Hello
2
Sec
Hello
3
Sec 
Hello
4
Sec
Hello
5
Sec
Hello
6
Sec
Hello
7
Sec
Hello
else suite
Outside loop
'''


#assignment
a=eval(input('Enter any list :'))
x=eval(input('Enter the element to be searched:'))
for i in range(len(a)):
    if a[i]==x:
        print('Found at index:',i)
        break
        print('Not found')



#assignment duplicate numbers
a=eval(input('Enter any list:'))
x=eval(input('Enter the element to be searched:'))
ctr=0
for i in range(len(a)):
    if a[i]==x:
        print('Found at index:',i)
        ctr+=1
print(F'{x} is found {ctr} times')



# walrus operator

#assignment1
print(a:=25)				# 25
print(a=35)					# error
print(a)					# 25
print(a:=6+7)				# 13
print(13)					# 13
print(a)					# 13
print((a:=6)+7)				# 13
print(a)					# 6
#print((a=6)+7)				# error



#assignment2
a=0
if a==0:					# True
    print('Hyd')			# Hyd
else:
    print('Sec')
if b:=0:					# False
    print('Hyd')
else:
    print('Sec')			# Sec : 0
if c==0:					# error 
    print('Hyd')
else:
    print('Sec')



#assignment3
#determine average of inputs which are terminated with ctrl+z

try:
	sum =  ctr = 0
	while  True:
		x = eval(input('Enter input  (ctrl + z  to  stop)  :  '))  
		sum += x 
		ctr +=1 
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError: 
		print('Enter  at  least  one  input')
except  (NameError , TypeError):  
	print('Input  can  not  be  string')
