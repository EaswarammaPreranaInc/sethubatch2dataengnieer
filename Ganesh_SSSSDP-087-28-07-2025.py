'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
   #
    a= complex(3,4)
    print('First Complex num: ',a)
    
2nd   complex  number   --->  5 + 6j
   #
    b= complex(5,6)
      print('second complex: ',b)

What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
   # 
    sum= a + b
     print('sum of number: ' ,sum)

What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
    #
     diff= a - b
      print('diff number: ',diff)

What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j
    #
    product= a * b
     print('product of num: ',product)

What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                            =   (15 - 18j + 20j + 24) / (25 + 36)
    #
     divisible= a / b
     print('divisible by num: ',divisible)
																		 = 39 / 61 + 2j / 61											   
'''

# Identify  error

    else:
     print('else  suite')
    print('Outside')

 #answer
  if false:
     print('if suite')
  else:
     print('else  suite')
  print('Outside')


# Identify  error
     if  9 > 5
	print('Hello')
      print('Bye')

     # answer 
     if  9 > 5:
	print('Hello')
      print('Bye')

# Identify  error
     if  9 > 12:
	print('Hyd')
     else
	print('Sec')

    #answer
        if  9 > 12:
	    print('Hyd')
        else:
	    print('Sec')

# Identify  error
     if  (10,20,15):
         print('Hyd')
     else:
         print('Sec')

     # answer
       if(10,20,15):
            print('Hyd')
       else:
            print('Sec')


# Identify  error
    if  ():
			  print('Hyd')
	else:
					print('Sec')
     print('Bye')

       # answer
          if ():
               print('Hyd')
	  else:
	       print('Sec')
          print('Bye')


# Identify  error
   if  { }:
  {
	print('One')
	print('Two')
	print('Three')
  }
  else:
  {
	print('Four')
	print('Five')
	print('Six')
  }
  print('Bye')
     
      # answer
           if { }:
	        print('One')
	        print('Two')
	        print('Three')
           else:
	       print('Four')
	       print('Five')
	       print('Six')
         print('Bye')

# Identify  error
     if  ():
	print('One')
	print('Two')
	print('Three')
     else:
     if  []:
	print('Four')
	print('Five')
	print('Six')
     else:
     if  {}:
	print('Seven')
	print('Eight')
	print('Nine')
     else:
	print('Hyd')
	print('Sec')
	print('Cyb')
     print('Bye')
    
      # answer
     if True:
	print('One')
        print('Two')
        print('Three')
    else:
        if []:
	   print('Four')
	   print('Five')
	   print('Six')
        else:
            if  {}:
	        print('Seven')
	        print('Eight')
	        print('Nine')
            else:
	       print('Hyd')
	       print('Sec')
	 print('Cyb')
      print('Bye')

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
     #
    num=int(input('enter a num: '))
    if num % 2== 0:
        print('number is even: ',num)
    else: 
        print('num is odd: ' num)


# Find outputs  (Home  work)
    if():
        print('Hyd')
        print('Sec')
        print('Cyb')       # error because donot put empty brasses in if else condition 
    else:
        print('One')
        print('Two')
        print('Three')
    print('Bye')


# Find  outputs  (Home  work)
    if{10 : 20 , 30 : 40}:
        print('Hyd')     # Hyd
        print('Sec')     # Sec
        print('Cyb')     # Cyb
    print('Bye')         # Bye

  # Find outputs  (Home  work)
    if { }:
	print('Hyd')
	print('Sec')      # Bye
	print('Cyb')
    print('Bye')
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
    #
    Month=int(input('enter a month num within 1  to 12: ')
       if(Month==1):
            print('january')
       else:
           print('Input  should  be  between  1  and   12')

    '''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
   #
   0 - Zero
   1 - One
   2 - Two
   ...
   9 - Nine
   10 - Invalid
   
   # if (str=='Zero'):
           print(0)
     else:
          if(str=='one')
               print(1)
          else:
              if(str=='two')
                   print(2)
              else:
                  print(9)
      print('invalid')
''' 

    
 