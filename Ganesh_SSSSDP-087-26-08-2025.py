'''
Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set

1) Let  input  be  RamA  Rao
    What  is  the  output  ?  --->  AO  (case  is  ignored)

2) Both  input  and  output  are  strings

3) Hint:  Same  as  prog19  with  minor  changes
'''
 Enter  mixed  case  string :  RamA raO
 Distinct  vowels :   OA

		# output
		vowels=['A','a','E','e','I','i','O','o','U','u']
		str=input('enter a stringL: ')
		res=set(str)
		distinct={i for i in res if i in vowels}
		a=''+join(distinct)
		print('distinct_vowels: ',a)
		