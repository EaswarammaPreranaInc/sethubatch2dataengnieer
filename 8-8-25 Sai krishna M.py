'''
1)Write  a  program  to  determine  largest  command  line  input

try:
    from sys import argv
    print(argv)
    a=[]
    l = argv[1:]
    print(l)
    for i in l:
        a.append(eval(i))
    print(a)
    print(max(a))
except:
    print("Input cant be string and number")
'''


'''
2)Write  a  program  to  determine  command  line  input is even number or odd number 

try:
    from sys import argv
    print(argv)
    a=[]
    l = argv[1:]
    print(l)
    for i in l:
        a.append(int(i))
    print(a)

    if a[0]%2==0:
        print("Even Number")
    else:
        print("Odd Number")
except:
    print("Pls send an integer input only")
'''

'''
3)Write  a  program  to  determine  average  of  command  line  inputs

try:
    from sys import argv
    print(argv)
    a=[]
    l = argv[1:]
    print(l)
    for i in l:
        a.append(eval(i))
    print(a)
    print(f"Average = {sum(a)/len(a):.2f} ")
except:
    print("Pls send Number inputs ")
'''

'''
4)Write  a  program  to  sort  command  line  inputs  in  ascending  order  and  descending  order

try:
    from sys import argv
    print(argv)
    a=[]
    l = argv[1:]
    print(l)
    for i in l:
        a.append(eval(i))
    l1=sorted(a)
    l2=sorted(a,reverse=True)
    print(f"Ascending Order : {l1} and Descending Order : {l2}")
except:
    print("Pls dont send number and string together")
'''

'''
5)Concate two strings 

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")
s3 = ''

if len(s1)>2 and len(s2)>2 :
    s3+=s2[:2]+s1[2:]+" "+s1[:2]+s2[2:]
    print("Result : ",s3)
else:
    print("Input  should  be  a  min  of  2-char  string")
'''   

'''
6)Write  a  program  to  print  first  two  and  the  last  two  characters  of  the  string
Print  an  empty  string  if  string  has  less  than  four  characters

s = input("Enter a string : ")
s1=''
if len(s)>4 :
    s1 = s[:2]+s[-2:]
    print("Result : ",s1)
'''
    
'''
7)Write  a  program  to  print  characters  of  the  string  in  forward  and  reverse directions  without  slice

s = input("Enter a string : ")
print("Prininting in Forward Direction")
for i in range(len(s)):
    print(f"Character at index {i} : {s[i]}")

print()
print("Prininting in Revsrse Direction")
for i in range(len(s)-1,-1,-1) :
    print(f"Character at index {i} : {s[i]}") 
'''
    
'''
7)Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice


s = input("Enter a string : ")
even = ''
odd = ''

for i in range(len(s)):
    if i%2==0:
        even+=s[i]
    else:
        odd+=s[i]
print(f"characters at even places : {even} and characters at odd places : {odd}")
'''

'''
8)Let  input  be    A   4   B   3   C   2   $   5
                    0   1    2   3   4   5   6   7

What  is  the  output ?  --->  AAAABBBCC$$$$$

try:
    s = input("Enter a String : ").strip()  # Example: A4B3C2$5
    s1 = ""

    for i in range(0, len(s), 2):
        s1 += s[i] * int(s[i + 1])

    print(s1)
except:
    print("String should have alternate characters and digits")

'''

'''
9)Write  a  program  to  merge  two  strings  to  form  a  new  string

s1 = input("Enter First String : ")
s2 = input("Enter Second String : ")
s3=''

i=0
while(i<len(s1) or i<len(s2)):
    if i<len(s1):
        s3+=s1[i]
    if i<len(s2):
        s3+=s2[i]
    i=i+1
print("Result : ",s3)
'''

'''
10)Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

s = input("Enter a String : ")
s1=""
for i in s:
    if i not in s1:
        s1+=i 
print(s1)
 '''   


'''
11)
'''

try:
    s = input("Enter a String : ").strip()  # Example: A4M3Z5D2
    s1 = ""

    for i in range(0, len(s), 2):
        s1 += s[i]+chr(ord(s[i])+int(s[i+1]))

    print(s1)
except:
    print("String should have alternate characters and digits")





