'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set
1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)
2) Both  input  and  output  are  strings
'''

ip = set(input('Enter the string : ').upper())
a = [i for i in ip if i in 'AEIOU']
print('Distinct vowels : ', ''.join(a))