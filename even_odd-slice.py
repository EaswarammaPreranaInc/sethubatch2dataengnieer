'''
Write  a  program  to  print  characters  at  even  and  odd  indexes  without  slice

							 0      1      2      3     4     5     6      7
Let  input  be        R      a     m      a             R     a      o

odd =  '' + 'a' + 'a' + 'R' + 'o' = 'aaRo'
even =   '' + 'R' + 'm' + ' '  + 'a' = 'Rm a'

1) What  action  to  be  made  when  index  is  even ?  --->
																	Concatenate  the  character  to  even  object

2) What  action  to  be  made  when  index  is  odd ?  --->
																	Concatenate  the  characeter  to  odd  object

3) Hint: Use  single  for  loop


Enter  any  string  :  RAMA RAO
String  at  even  indexes  : RM A
String  at  odd  indexes  : AARO
'''

from sys import argv

try:
    str1=argv[1]

    even=''
    odd=''
    for i in range(len(str1)):
        if i%2==0:
            even+=str1[i]
        else:
            odd+=str1[i]
    print("String  at  even  indexes  : ",even)
    print("String  at  odd  indexes  : ",odd) 
except :
    print("Please provide the input in quotes")