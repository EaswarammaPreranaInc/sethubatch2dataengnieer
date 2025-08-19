'''
Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers

First  complex  number   --->  3 + 4j
2nd   complex  number   --->  5 + 6j
What  is  the  sum ? ---> (3 + 4j) + (5 + 6j) = 8 + 10j
What  is  the  difference ?  ---> (3 + 4j) - (5 + 6j) =  -2 - 2j
What  is  the  product ?  ---> (3 + 4j) * (5 + 6j) =  15 + 18j + 20j - 24 =  -9 + 38j


What  is  the  division ?  ---> (3 + 4j) / (5 + 6j) = (3 + 4j) * (5 - 6j) / (5 + 6j) * (5 -6j)
                                                                         =   (15 - 18j + 20j + 24) / (25 + 36)
																		 = 39 / 61 + 2j / 61											     
Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)                                             
                                             
'''

a=complex(input("enter 1st number: "))
b=complex(input("enter 2st number: "))
print(f"a + b = {a+b}")
print(f"a - b = {a-b}")
print(f"a * b = {a*b}")
print(f"a / b = {a/b:.2f}")


# Identify  error
else:
	print('else  suite') #syntax Error because of only else block of code 
print('Outside')



# Identify  error
if  9 > 5
	print('Hello')#Error beacuse of colon is missing in if condition
print('Bye')



# Identify  error
if  9 > 12:
	print('Hyd')
else              #Error because colon is missing in else Block 
	print('Sec')
	


# Identify  error
if  ():  
			print('Hyd')
   else:  #Error because Else is not in same suite as if condition
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
}                   #Error because of braces. python doesn't support braces
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
print('Bye')#Indentation Error in  2nd, 3rd  conditions 


# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
num=eval(input("enter any num: "))
if num%2==0:
	print("even  number")
else:
	print("odd number")
	

# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')     
        print('Two')
        print('Three')
print('Bye')  ''' One
                  Two
						Three
						Bye'''


# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')   
        print('Sec')
        print('Cyb')
print('Bye') '''
                Hyd
					 Sec
					 Cyb
					 Bye'''

# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')  #Bye

'''
# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)

Enter month number (1 - 12): 6
June

Enter month number (1 - 12): 13
Input  should  be  between  1  and   12

Enter month number (1 - 12): 10.8
Input  should  be  an  integer
'''

try:
   month=int(input("Enter month number(1 - 12): "))
   if month==1:
      print("Jan")
   elif month==2:
      print("Feb")
   elif month==3:
      print("Mar")
   elif month==4:
      print("Apr")
   elif month==5:
      print("May")
   elif month==6:
      print("Jun")
   elif month==7:
      print("Jul")
   elif month==8:
      print("Aug")
   elif month==9:
      print("sept")
   elif month==10:
      print("Oct")
   elif month==11:
      print("Nov")
   elif month==12:
      print("Dec")
   else:
      print("Input should be between 1 and 12 ")
except ValueError:
       print("Input should be an Integer")


'''
Write  a  program  to  print  digit  in  words  with  else  and  if  
(do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

num=int(input("Enter a digit (0-9): "))
if num == 0:
   print("Zero")
else:
   if num == 1:
      print("One")
   else:
      if num == 2:
            print("Two")
      else:
            if num == 3:
               print("Three")
            else:
               if num == 4:
                  print("Four")
               else:
                  if num == 5:
                        print("Five")
                  else:
                        if num == 6:
                           print("Six")
                        else:
                           if num == 7:
                              print("Seven")
                           else:
                              if num == 8:
                                    print("Eight")
                              else:
                                    if num == 9:
                                       print("Nine")
                                    else:
                                       # This else catches anything unexpected
                                       print("Invalid")
