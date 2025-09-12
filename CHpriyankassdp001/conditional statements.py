# conditional statements
print("conditional statements:")
""" there are 4 types of conditional statements i.e
         if 
            if else
                if else if (elif)
                     nested if"""

# if statement
print("if statement")
""" if statement 
it is always true block
here condition=== relation operator"""
print(" ")
print("program for check a num even or odd")
print()
a=int(input("enter a num:"))
if a%2==0:
    print("%d is even num"%a)
print("end")

print("check for negative or positive")
b=int(input("enter the value:"))
if b<=0:
    print("its a negative number")
print("end")


print("check for item is in list")
d=[6,8,9,64,2]
c=input("enter the num:")
if c==d[4]:
    print("its present")
print("bye")



# if else statement

print(" if else statement::")
print()
e=int(input("enter:"))
if e<0:
    print("its negative number")
else:
    print("its positive number")




#if elif else (elif)
print("if elif else")
i=int(input("i:"))
j=int(input("j:"))
if i<j:
    print("i is smaller than j")
elif i>j:
    print("j is smaller than i")
else:
    print("both are equal")


#nested statements
print("nested statements")
p=int(input("enter p:"))
q=int(input("enter q:"))
r=int(input("enter r:"))
if p>q:
    if p>r:
        print("p is big")
    else:
        print("r is big")
else:
    if q>r:
        print("q is big")
    else:
        print("r is big")