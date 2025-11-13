# Program 1
# sub()  function  demo  program (Home  work)
import  re
print(re  .  sub('-'  ,  '/'  ,  '15 - Aug - 1947'))
print(re  .  sub(' '  ,  ':'  ,  '18 52 36'))
print(re  .  sub('[0-9]'  ,  '$'  ,  'a7b8c6d5'))
print(re  .  sub('[a-z]'  ,  '%'  ,  'a7b8G6d5'))
print(re  .  sub('is'  ,  'was'  ,  'Hyd is his city'))
print(re  .  sub('a' , 'b' , 'Rama  Rao'))

# Output :
15 / Aug / 1947
18:52:36
a$b$c$d$
%7%8G6%5
Rbmb  Rbo


# Program2
#  subn()  finction  demo  program  (Home  work)
import  re
print(re . subn('[a-z]'  ,  '#'  ,  'a7G9c5D8e'))
print(re  .  subn(' '   ,  ':'  ,   '18 52 46'))
print(re  .  subn('-'  ,  '/'  ,  '15-Aug-1947'))
print(re  .  subn('is'  ,  'was'  ,  'Hyd is his city'))
print(re . subn('a' , 'b' , 'Rama rao'))

# Output :
('#7G9#5D8#', 3)
('18:52:46', 2)
('Hyd was hwas city', 2)
('Rbmb rbo', 3)


# Program 3
#  split()  function  demo  program  (Home  work)
import  re
print(re . split(','  ,  'Hyd,Pune,Chennai,Delhi,Vijayawada'))
print(re . split('-'  ,  '15-Aug-1947'))
print(re . split(':'  ,  '18:52:46'))
print(re . split(' '  ,  'Hyd is green city'))

# Output :
['Hyd', 'Pune', 'Chennai', 'Delhi', 'Vijayawada']
['15', 'Aug', '1947']
['18', '52', '46']


# Program 4
# Find  outputs
import re
print(re . split('[.]'  ,  'www.gmail.com'))
print(re . split('.'  ,  'www.gmail.com'))

# Output :
['www', 'gmail', 'com']
['', '', '', '', '', '', '', '', '', '', '', '', '', '']


# Program 5
'''
Write  a  program  to  extract  all  mobile  numbers  present  in  a  file  to  another  file
and  mobile  numbers  are  mixed  with  normal  text  in  the  file

1) Let  input.txt  file  contain
    hyd 9948250500 sec 09848565090 cyb
    ap +919440250404 tel
    kar 9848066695 tn
    04023304078
    xnmxcnmxvncx 989898989898
    nnvbnvn
    969696
    919948250500

2) What  does  output.txt  file  contain ?  --->  9948250500
																	     09848565090
																	     +919440250404
																	     9848066695
																	     9898989898
																	     9199482505

3) Use  finditer()  function
'''

# Program 
import re
fname=input("Enter file name with .txt at end :")
otname=input("Enter file name for output data with .txt at end :")
fin = open(fname, "r")
fout = open(otname, "w")
data = fin.read()
pattern = r'(\+91|0)?[6789][0-9]{9}'
matches = re.finditer(pattern, data)
for m in matches:
    num = m.group()
    fout.write(num + "\n")
fin.close()
fout.close()
print("Mobile numbers extracted successfully to output.txt")

