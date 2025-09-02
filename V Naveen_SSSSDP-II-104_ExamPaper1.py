
#1. Write  a  program  to  evaluate  expression  like  calculator

#Enter  any  expression  terminated  by  =  :  3+4*5-6/2=
#Result :  14.5

ex = input("Enter  any  expression  terminated  by  =  : ")
i = 0
a = int(ex[i])
i += 1
while ex[i] != "=":
    op = ex[i]
    i += 1
    b = int(ex[i])
    i += 1
    if op == "+":
        a = a + b
    elif op == "-":
        a = a - b
    elif op == "*":
        a = a * b
    elif op == "/":
        a = a / b
print("Result :", a)

    




#2. Write  a   program  to  print  roman  equivalent  of  a  number

#Enter  any  number :  3878
#Roman  Equivalent :   MMMDCCCLXXVIII

a = int(input("Enter  any  number : "))
b = ['M' , 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
c = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
d = ''
for i in range(len(c)):
    e = a // c[i]
    d += b[i] * e
    a = a % c[i]
print("Roman  Equivalent : ', d)





#3. Write  a  program  to  print  each  digit  of  the  number  in  words


a = input("Enter  any   number : ")
b = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'six', 'Seven', 'Eight', 'Nine']
c = ''
for i in a:
    c += b[int(i)] + ' '
print(c)




#4. Write  a  program  to  print  all  the  rotations  of  the  string

a = input("Enter any string : ")
for i in range(len(a)):
    print(a[i:] + a[:i])




#5. Write  a  program  to  print  mathematical  table  of  a  number

a = int(input("Enter  table  number :  "))
for i in range(1,11):
    print(f'{a} * {i} = {a*i}')

    


'''
6. Write a  program to print following pyramid
Input: 5

             A
            A B
           A B C
          A B C D
         A B C D E


	   i         ch
---------------------
       1         'A'

	   2         'A'  to  'B'

	   3         'A'  to  'C'

	   4         'A'  to  'D'

	   5         'A'  to  'E'
'''

a = int(input("How  many  lines ?  :  "))
for i in range(1,a+1):
    print(" "*(a-i),end = "")
    for j in range(i):
        print(chr(65+j),end = " ")
    print()