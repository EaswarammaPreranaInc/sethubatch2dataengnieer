# sub()  function  demo  program (Home  work)
import  re
print(re  .  sub('-'  ,  '/'  ,  '15 - Aug - 1947'))                            15/Aug/1947
print(re  .  sub(' '  ,  ':'  ,  '18 52 36'))                                   18:52:36
print(re  .  sub('[0-9]'  ,  '$'  ,  'a7b8c6d5'))                               a$b$c$d$
print(re  .  sub('[a-z]'  ,  '%'  ,  'a7b8G6d5'))                               %7%8G6%5
print(re  .  sub('is'  ,  'was'  ,  'Hyd is his city'))                         Hyd was hwas city
print(re  .  sub('a' , 'b' , 'Rama  Rao'))                                      Rbmb Rbo

#  subn()  finction  demo  program  (Home  work)
import  re
print(re . subn('[a-z]'  ,  '#'  ,  'a7G9c5D8e'))                                ('#7G9#5D8#',3)
print(re  .  subn(' '   ,  ':'  ,   '18 52 46'))                                 ('18:52:46',2)
print(re  .  subn('-'  ,  '/'  ,  '15-Aug-1947'))                                ('15/Aug/1947',2)
print(re  .  subn('is'  ,  'was'  ,  'Hyd is his city'))                         ('Hyd was hwas city',2)
print(re . subn('a' , 'b' , 'Rama rao'))                                         ('Rbmb rbo',3)

#  split()  function  demo  program  (Home  work)
import  re
print(re . split(','  ,  'Hyd,Pune,Chennai,Delhi,Vijayawada'))                  ['Hyd','Pune','Chennai','Delhi','Vijayawada']
print(re . split('-'  ,  '15-Aug-1947'))                                        ['15','Aug','1947']
print(re . split(':'  ,  '18:52:46'))                                           ['18','52','46']
print(re . split(' '  ,  'Hyd is green city'))                                  ['Hyd','is','green','city']

# Find  outputs
import re
print(re . split('[.]'  ,  'www.gmail.com'))                                    ['www','gmail','com']
print(re . split('.'  ,  'www.gmail.com'))                                      ['','','','','','','','','','','','','']

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
import re
with open("input.txt", "r") as infile:
    data = infile.read()
pattern = r'\+?\d{0,2}\d{10}'
with open("output.txt", "w") as outfile:
    for match in re.finditer(pattern, data):
        number = match.group()
        if len(number) >= 10 and len(number) <= 13:
            outfile.write(number + "\n")
print("Mobile numbers extracted successfully into output.txt")
