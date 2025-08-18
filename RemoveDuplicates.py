'''
Write  a  program  to  remove  duplicate  characters  of  the  string  without  using  set

1) Let  input  be   RAMA  RAO
   What  is  the  output ? ---> RAM<space>O

2) out = '' + 'R' = 'R' + 'A' = 'RA' + 'M' = 'RAM' + ' ' = 'RAM ' + 'O' = 'RAM O'

3) What  action  to  be  made  if  the  character  is  not  in  out  object ?  --->
																	Concatenate  the  character  to  out  object

4) What  action  to  be  made  if  the  character  is  already  in  out  object ?  --->
																							Ignore  the  character

5) Hint:  Use  not  in   operator


Enter  any  string  :  MISSISIPI
String  without  duplicates  :    MISP

'''

from sys import argv    

str1=argv[1]
res=''
for i in str1:
    if i not in res:
        res += i
print(res)