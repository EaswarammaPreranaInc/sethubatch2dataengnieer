# write a program to evaluate expression like a calculator
n=input("enter expression : ")
s=n.split()
a=float(s[0])
i=1
while i < len(s):
   op=s[i]
   if op=="=":
     break 
   b=float(s[i+1])    
   if op == "+":
       a=a+b
   elif op == "-":
      a=a-b
   elif op == "*":
      a=a*b
   elif op == "/":
      a=a/b
   i=i+2
print("result is: ",a)
                                                  
 enter expression : 3 + 4 * 5 - 6 / 2 =
result is:  14.5



a= int(input("enter how many rows: "))
for i in range(a):
    print(" "*(a-i-1),end="")
    for j in range(i+1):
         print(chr(65 + j),end=' ')
    print()
 enter how many rows: 9
        A
       A B
      A B C
     A B C D
    A B C D E
   A B C D E F
  A B C D E F G
 A B C D E F G H
A B C D E F G H I





a=input("enter a number: ")
digit_words={
'0':'zero',
'1':'one',
'2':'two',
'3':'three',
'4':'four',
'5':'five',
'6':'six',
'7':'seven',
'8':'eight',
'9':'nine',
'10':'ten'
}
 
# write a program to convert digits to words
for digit in a:
   if digit in digit_words:
       print(digit_words[digit],end=" ")   
   else:
     print(" not a number")
enter a number: 5021
five zero two one