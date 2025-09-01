'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  ---> AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
a = input('Enter  mixed  case  string :  ')  #  Reads  a  string
a = a . upper()  #  Converts  string  to   uppercase
b = set(a)  #  Converts  uppercase string  to  set
d = b . intersection('AEIOU')  #  Common elements  between  set 'b'  and  string  'AEIOU'
e = '' . join(d)   #  Converts  set  'd'  to  string
print('Distinct  vowels :  ' , e)