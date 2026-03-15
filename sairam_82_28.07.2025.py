1) Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers 
Program: 
a = complex(input("First complex number: ")) 
b = complex(input("Second complex number: ")) 
sum = a + b 
diff = a - b 
prod = a * b 
div = a / b 
print(f"First complex number ---> {a}") 
print(f"Second complex number ---> {b}") 
print(f"What is the sum? ---> {a} + {b} = {sum}") 
print(f"What is the difference? ---> {a} - {b} = {diff}") 
print(f"What is the product? ---> {a} * {b} = {prod}") 
print(f"What is the division? ---> {a} / {b} = {div}") 
Output: 
First complex number: 5+4j 
Second complex number: 6+8j 
First complex number ---> (5+4j) 
Second complex number ---> (6+8j) 
What is the sum? ---> (5+4j) + (6+8j) = (11+12j) 
What is the difference? ---> (5+4j) - (6+8j) = (-1-4j) 
What is the product? ---> (5+4j) * (6+8j) = (-2+64j) 
What is the division? ---> (5+4j) / (6+8j) = (0.62-0.16j) 

2) 
# Identify  error 
else: 
print('else  suite') 
print('Outside')  # print('else  suite') needs to be moved to the right (indented) 

3) # Identify  error 
if  
9 > 5 
print('Hello') 
print('Bye') #No Semicolon – Syntax Error 

4) Identify  error 
if  9 > 12: 
print('Hyd') 
else 
print('Sec') #Syntax and intendation Error 

5) # Identify  error 
if  (10,20,15): 
print('Hyd') 
else: 
print('Sec') #Intendation Error 

6) # Identify  error 
if  (): 
else: 
print('Hyd') 
print('Bye')  #Intendation Error 

7) # Identify  error 
if  { }: 
{ 
print('One') 
print('Two') 
print('Three') 
print('Sec') 
} 
else: 
{ 
} 
print('Four') 
print('Five') 
print('Six') 
print('Bye')  #Syntax Error-Braces not allowed  

8) # Identify  error 
if  (): 
else: 
if  []: 
else: 
if  {}: 
else: 
print('One') 
print('Two') 
print('Three') 
print('Four') 
print('Five') 
print('Six') 
print('Seven') 
print('Eight') 
print('Nine') 
print('Hyd') 
print('Sec') 
print('Cyb') 
print('Bye')  #Indentation Error 

#9) Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement 
a = int(input("Enter a number: ")) 
if a % 2 == 0: 
print(f"{a} is even") 
else: 
print(f"{a} is odd") 
Output: 
Enter a number: 31 
31 is odd 

#10) Find outputs  (Home  work) 
if(): 
else: 
print('Hyd') 
print('Sec') 
print('Cyb') 
print('One') #One  
print('Two') #Two 
print('Three')#Three 
print('Bye') #Bye 

#11) # Find  outputs  (Home  work) 
if{10 : 20 , 30 : 40}: 
print('Hyd') #Hyd 
print('Sec') #Sec 
print('Cyb') #Cyb 
print('Bye') #Bye 

#12) # Find outputs  (Home  work) 
if { }: 
print('Hyd') 
print('Sec') 
print('Cyb') 
print('Bye') #Bye 

#13) # Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif 
a = int(input("Enter month number (1-12): ")) 
if a == 1: 
print("January") 
elif a == 2: 
print("February") 
elif a == 3: 
print("March") 
elif a == 4: 
print("April") 
elif a == 5: 
print("May") 
elif a == 6: 
print("June") 
elif a == 7: 
print("July") 
elif a == 8: 
print("August") 
elif a == 9: 
print("September") 
elif a == 10: 
print("October") 
elif a == 11: 
print("November") 
elif a == 12: 
print("December") 
else: 
print("Invalid month number") 
Output: 
Enter month number (1-12): 11 
November 

#14) 
a = int(input("Enter a digit (0-9): ")) 
if a == 0: 
print("Zero") 
elif a == 1: 
print("One") 
elif a == 2: 
print("Two") 
elif a == 3: 
print("Three") 
elif a == 4: 
print("Four") 
elif a == 5: 
print("Five") 
elif a == 6: 
print("Six") 
elif a == 7: 
print("Seven") 
elif a == 8: 
print("Eight") 
elif a == 9: 
print("Nine") 
else: 
print("Invalid") 
Output: 
Enter a digit (0-9): 7 
Seven 
