'''
Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0

1) What  is  the  result  if  input  is  -25 ?  --->  -1  
  # output
  num=int(input('enter 1st input: ')
  if num<0:
      result=-1
  print('-ve negative number result: ',result)
  

2) What  is  the  result  if  input  is  75 ?  --->  1
  # output
   num =int(input('enter a input: '))
   if num>0:
       result=1
    print('+ve positive num result: 'result)
    

3) What  is  the  result  if  input  is  0 ?  --->  0
  # 
   num=int(input('enter a input: ))
   if num==0:
       result=0
    print('number is equal to zero result: ' result)

4) Use  nested  ternary  operator
    # 
   num=int(input('enter a num: '))
   if num<0:
       result=-1
   elif num>0:
       result=1
   else:
      result=0
   print('result: 'result)  
'''


'''
Write  a  program  to  test  input  is  even  number  or  odd  number

1) What  is  an  even  number  ?  --->  Divisible  by  2
  # 
   num=int(input('enter a num: ')
   if num%2==0:
       print('num divisible by 2 even num: ',num)

2) What  is  an  odd  number  ?  --->  Not  divisible  by  2
  #
   num=int(input(enter a num: ')
   if num%2!=0
       print('num not divisible by 2 odd num: ',num)
3) Use  ternary  operator
    # 
     if num%2==0
         print('divisible by 2 even num: ',num)
     else 
        print('not divisible by 2 odd num: ',num) 
'''


'''
(Home  work)
Write  a  program  to  determine  area  and  perimeter  of  rectangle

1) What  are  the  inputs ?  ---> length  and   breadth
   #
    length=int(input('enter a length: '))  # 10 
    breadth=int(input(enter a breadth: '))  # 15
    

2) What  are  the  outputs  ?  --->  area  and  perimeter
    #
    area=float((length*breadth))   # 10*15
    perimeter=float(2*(length+breadth))  # 2(10+15)
    
    
3) What  is  the  area  of  rectangle  ?  --->  length * breadth
    # 
     area=f(length*breadth)  # 10 *15
     print('area of rectangle: ',area)  # 150

4) What  is  the  perimeter  of  rectangle ?  --->  2 * (length + breadth)
   #
    perimeter=float(2*(length+breadth))  #2(10+15)
    print('perimeter of rectangle: ',perimeter)  # 50
   
'''

'''
(Home  work)
Write  a  program  to  determine  volume  of  a  sphere

1) What  is  the  input ?  --->  radius
   #
   dia=int(input('enter a input: ')) # 30
   radius=dia/2  # 15

2) What  is  the  output ?  --->  volume
  #
   pi=float(input(enter a num: ))
   volume=4/3*pi*r^3
   print('volume: ',volume) 

3) What  is  the  volume  of  sphere  ?  --->  4 / 3  * pi *  r ^ 3
    volume=4/3*pi*r^3
    print('volume: ',volume)  # 14130.0
'''


'''
(Home  work)
Write  a  program  to  determine  simple  interest  and  compound  interest

1) What  are  the  inputs  ?  --->  principle , time  and   rate  of  interest
  # 
  principle=float(input('enter a principle: '))  # 100000.00
  time=float(input('enter a time: '))     # 2 years
  rate of inter=float(input('enter a rate of intrst : '))  # 2%

2) What  are  the  outputs ? --->  Simple  interest   and   compound  interest
   # 
   simple intrst=p*r*t/100  
   compound intrst=p(1+r%/100)^t-p

3) What  is  simple  interest  formula ?  ---> ptr / 100
  # 
   simple intrst=p*r*t/100
                 = 100000*2%*2/100
     print('simple intrst: ',simple intrst) # 4000

4) What  is  compound  interest  formula ?  --->  p * (1  +  r  /  100) ^  t  -  p
  # 
   compound intrst=p*(1+r/100)^t-p
                  =100000*(1+2%/100)^2-100000
    print("compound intrst: ',compound intrst)  # 404.0
'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  using  3rd   object

Let  x = 10  and  y = 25
What  are  the  values  of  x  and  y  after  swap ?  --->  x = 25  and   y = 10

   # 
   x= 25
   y= 10
   temp= x  # temp=25
   x= y     # x=10
   y= temp   # y= 25
   print('x: ',x,'y: ',y) # x:10 y: 25
'''

'''
(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  addition  and  two  subtractions

x = 25
y =  10

  x= x-y  # 25 - 10= 15 --> x= 15
  y= x+y  # 15 + 10= 25 --> y= 25
  x= y-x  #  25 - 15= 10 --> x= 10    
  print('x: ',x,'y: ',y)
'''


(Home  work)
Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object

Hint: One  multiplication  and  two  divisions

 x =  -200
 y =  100
  # 
   x=x * y   # -200 * 100 = -20000
   y=x // y  # -20000 // 100 = -200
   x=x // y  #  -20000 // -200 = 100
   print('x: ',x,'y: ',y)
