'''
Write  a   program  to  print  roman  equivalent  of  a  number
1000 -  M
900  -  CM
500 -  D
400 - CD
100 -   C
90  -  XC
50  -  L
40  -  XL
10  -  X
9  -  IX
5  -  V
4  -  IV
1  -  I

1) What  is  the  output  if  input  is  3878 ? ---> MMMDCCCLXXVIII

2) What  is  the  result  of  3878 // 1000 ?  --->  3
    How  many  M's  are  concatenated  to  the  sting ?  --->  Three  becoz  3878 / 1000  is  3
    What  is  the  result  of  3878 % 1000 ?  --->  878

3) What  is  the  result  of  878 // 900 ?  --->  0
    How  many  CM's  are  concatenated  to  the  string ?  ---> Zero  becoz  878 / 900  is  0
    What  is  the  result  of  878 % 900 ?  --->  878

4) What  is  the  result  of  878 // 500 ?  ---> 1
     How  many  D's  are  concatenated  to  the  string ?  ---> One  becoz  878 / 500  is  1
     What  is  the  result  of  878 % 500 ?  ---> 378
     and so on
'''

n=int(input("Enter a number = "))
roman= {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}
res = ""
for val in sorted(roman.keys(), reverse=True):
    count = n // val
    res += roman[val] * count
    n = n % val
print("Roman Equivalent :", res)


'''
Output:

Enter a number = 4878
Roman Equivalent : MMMMDCCCLXXVIII

'''