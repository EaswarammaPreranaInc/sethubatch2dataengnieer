############# 28-07-2025 ###############################################################################
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
'''


#####answere 

Enter first complex number : 3+4j
Enter second complex number: 5+6j
Sum :  (8+10j)
Difference :  (-2-2j)
Product:  (-9+38j)
Division :  (0.6393442622950819+0.03278688524590165j)

###########################################################################################################

# Identify  error
else:
		print('else  suite') # there is no if  
print('Outside')

##############################################################################################################
# Identify  error
if  9 > 5  ## here colon is not there 
	print('Hello') 
print('Bye')

#############################################################################################################

# Identify  error
if  9 > 12:
	print('Hyd') 
else                    # after else there should be a colon 
	print('Sec')

###############################
# Identify  error
if  (10,20,15):
print('Hyd') ## indentation error 
else:
print('Sec') ## indentation error 
################################
# Identify  error
if  ():
			print('Hyd')
	else:
					print('Sec')
print('Bye')
#######################################
# Identify  error  
if  { }:     
{                    # error due to flower brackets are there 
	print('One')
	print('Two')
	print('Three')
}
else:
{                     ## error due to flower brackets are there 
	print('Four')
	print('Five')
	print('Six')
}
print('Bye')
#######################################
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
if  []:   # if should not be there machine  takes much time to execute
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
###########################################

# Write  a  program  to  determine  a  number  is  even  or  odd  with   if  statement
a=int(input('Enter a number :'))
if a%2 == 0:
	print(f'{a} is an Even number')
else:
	print(f'{a} is an odd number')
#########################################
# Find outputs  (Home  work)
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:                        ## there is an empty string and it only prints bye 
        print('One')
        print('Two')
        print('Three')
print('Bye')
#############################################
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}: # i guess 10:20 takes value hyd 
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')                ## prints bye 
###########################################
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')  # prints only bye 

######################################

# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)


















#################   question            ######################################

Enter month number (1 - 12): 6
June

####### answere #####################

n = int(input('Enter the number:'))
if n == 1:
    print('january')
elif n==2:
    print('febuary')
elif n==3:
    print('march')
elif n==4:
    print('april')
elif n==5:
    print('may')
elif n==6:
    print('june')
elif n==7:
    print('july')
elif n==8:
    print('auguest')
elif n==9:
    print('september')
elif n==10:
    print('october')
elif n==11:
    print('november')
else:
    print('december')
        
        
    
        




####### answere #############

month_num = int(input('enter the month number:'))
if 1 >= month_num < 12:
	print(calendar.month_name(month_num))
else:
	print('Input should be month_name;')







#########################################################################################

Enter month number (1 - 12): 13
Input  should  be  between  1  and   12

##########answere #######

month_num = int(input('Enter the month number (1-12): '))

if 1 <= month_num <= 12:
    print(f'Success! {month_num} is a valid month number.')
else:
    print('Input should be between 1 and 12.')




##########################################################################################
Enter month number (1 - 12): 10.8
Input  should  be  an  integer

#### ANSWERE #####
import calendar
try:
    month_num = int(input('Enter month number (1-12):'))
    if 1<= month_num <= 12:
        print(calendar.month_name(month_num))
    else:
        print('Error: please enter value between (1-12):')
except :
        print('Input should be an integer:')

##########  QUESTION    #############################################################################
'''
Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)
0 - Zero
1 - One
2 - Two
....
9 - Nine
10 - Invalid
'''

######answere #####

a = int(input('Enter a single digit (0-9):'))

if a == 0 :
    print('zero')
else:
	if a == 1:
		print('one')
	else:
	    if a == 2:
		    print('two')
	    else:
	        if a == 3:
	        	print('three')
	        else:
	            if a == 4:
		            print('four')
	            else:
	                if a == 5:
	                	print('five')
	                else:
	                    if a == 6:
		                    print('six')
	                    else:
	                        if a == 7:
		                        print('seven')
	                        else:
	                            if a == 8:
		                            print('eight')
	                            else:
	                                if a == 9:
	    	                            print('Nine')
	                                else:
		                                   print('invalid')
	


############################################################################################################

