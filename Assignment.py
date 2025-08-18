'''
Write  a  program  to  determine  largest  command  line  input

1) py   prog2.py   10     20     30.8   7  40    35.6
    What  is  the  largest  command  line  input ?  ---> 40
    What  is  argv ?  --->  ['prog2.py' , '10' , '20' , '30.8' , '7' , '40' , '35.6']
    What  is  list  'a' ?  --->  [10 , 20 , 30.8 , 7 , 40 , 35.6]
    How  to  determine  largest  element  of  list  'a' ?   ---> max(a)  i.e.  40
    What  is  the  result  of  max(argv[1:]) ?  ---> '7'
    What  is  the  issue  with  max(argv[1:])) ?  --->
													Largest  string  is  obtained  but  not  largest  number

2) py  prog2.py
    What  is  the  output ?  ---> Pls  send  inputs

3) py   prog2.py   'Rama'   'Sita'   'Rajesh'   'Manohar'   'Vamsi'   'Amar'
    What  is  the  lar…
    
     py   prog2.py   25   'Ten'
    What  is  the  output ?  --->  Inputs  can  not  be  number  and  string

    
    
    from sys import argv

try:
	print(f'Largest string is  : {max(argv[1:])}') 
except ValueError:
	print("Pls send inputs")    
    
    '''
from sys import argv
l=[]
m=0
print(argv)
try:
   
    for i in range(1,len(argv)):
        
        l.append(eval((argv[i])))
  
    print(f'Largest number is : {max(l)}')
except ValueError:
	print("Pls send inputs")
except TypeError:
    print("Inputs can not be number and string")
except NameError:
	print(f'Largest string is : {max(argv[1:])}')

     
      	
    
