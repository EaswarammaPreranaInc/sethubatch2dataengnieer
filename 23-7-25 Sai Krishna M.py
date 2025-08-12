#=======================================================Practice Programs=====================================

'''
1)Given two integer numbers, 
write a Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

a = int(input("Enter the First Integer : "))
b = int(input("Enter the Second Integer : "))

print(a*b if a*b<1000 else a+b)

if a*b<1000:
    print("Product of two numbers : ",a*b)
else:
    print("Sum of two numbers : ",a+b)
'''

'''
2)Write Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.


for i in range(10):
    if i==0:
        print(f"Current number is {i} and Previous number is {i} and their Sum is {i+1}")
    else:
        print(f"Current number is {i} and Previous number is {i-1} and their Sum is {i+(i-1)}")

'''

'''
3)Print characters present at an even index number

s=input("Enter a String : ")
for i in range(len(s)):
    if i%2==0:
        print(s[i])
'''

'''
4)Remove first n characters from a string

s="Vishnu"
def remove_chars(word, n):
    # write your code

print("Removing characters from a string")
print(remove_chars("pynative", 4)) 
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2)) 
# output 'native'

'''
'''
5)Check if the first and last numbers of a list are the same

a = []
n = int(input("Enter how many numbers to enter : "))
for i in range(n):
    b = int(input("Enter a number : "))
    a.append(b)

if a[0]==a[-1]:
    print("True")
else:
    print("False")
'''

'''
6)Display numbers divisible by 5

a = []
n = int(input("Enter how many numbers to enter : "))
for i in range(n):
    b = int(input("Enter a number : "))
    a.append(b)

print(a)
print("Divisible by 5")

for i in a:
    if i%5==0:
        print(i)
        
'''


'''
7)Find the number of occurrences of a substring in a string
str_x = "Emma is good developer. Emma is a writer"
'''

'''
8)Print the following pattern
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5
'''

'''
9)Check Palindrome Number
original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
'''

'''
10)Given two lists of numbers, 
write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

list3 = []
for i in list1:
    if i%2==1:
        list3.append(i)

for i in list2:
    if i%2==0:
        list3.append(i)
print(list1)
print(list2)
print(list3)
'''

'''
11) Get each digit from a number in the reverse order with space .

a = int(input("Emter a number : "))
print("Given number", a )
while a > 0:
    digit = a % 10
    a = a // 10
    print(digit, end=" ")
'''

'''
12) Print multiplication table from 1 to 10

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")

'''
'''
13)Check Palindrome Number
'''
'''
for i in range(5,-1,-1):
    if i==0:
        print("Time Up")
    else:
       print("Time Remaining : ",i,"Seconds") 


str1 = 'My'
str2 = 'Name'
str3 = 'Is'
str4 = 'James'

print(str1,str2,str3,str4,sep='**')

num = 458.541315
print('%.2f'%num)


totalMoney = 1000
quantity = 3
price = 450

print(f"I have {totalMoney} dollars so I can buy {quantity} football for {'%.2f' %price} dollars.")



n = int(input("Enter a number : "))
r = n*(n+1)//2
print(r)


num = [12, 75, 150, 180, 145, 525, 50]
for i in num:
    if i > 500:
        break
    elif i> 150:
        continue
    elif i % 5 == 0:
        print(i)
         


num = int(input("Enter a number : "))
temp=num 
s=0
while num>0:
    digit = num%10 
    s = s+digit
    num=num//10
    
print(f"the number is {temp} and its Sum is : {s}")



a = eval(input("Enter a number or sting : "))
if type(a)!='' :
    temp=a 
    rev=0
    while a>0:
        rem = a%10 
        rev = (rev*10)+rem
        a=a//10
    print(f"The number is {temp} and its reversed number is : {rev}")
elif type(a)==' ':
    print(f"The string is {a} and its reversed string is : {a[::-1]}")
'''

'''
14) Write a program to create a new string made of an input string’s first, middle, and last character.

str1 = "James Stark"
str2 = str1[0]+str1[len(str1)//2]+str1[-1]
print(str2)

mi = int(len(str1) / 2)
res = str1[mi - 1:mi + 2]
print("Middle three chars are:", res)
'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3=[]
for i in range(len(l1)):
    if i%2!=0:
        l3.append(l1[i])
        print(l1[i],end=",")
print()
for i in range(len(l2)):
    if i%2==0:
        l3.append(l2[i])
        print(l2[i],end=",")
print()
print(l3)
















