x=complex(input("Enter first complex number:"))
y=complex(input("Enter second complex number:"))

print("sum:",x+y)
print("Difference:",x-y)
print("Product:",x*y)
print("Division:",x/y)
#=================================
# Identify  error
# else:
# 		print('else  suite')
# print('Outside')

# Ans: There is no if condition, so there is a syntax error in it 
# without the 'if' condition at the start of the program.
# =======================================
# Identify  error
#if  9 > 5
# 	print('Hello')
# print('Bye')
#Ans: There is no (:) for every if condition at the end, there should be a :
#===========================================
# Identify  error
if  9 > 12:
	print('Hyd')
# else
# 	print('Sec')
# Ans: There is no ':' to else condition in Python, for if, else there should be: at the end
# =======================================
# Identify  error
if  (10,20,15):
# print('Hyd')
# else:
# print('Sec')

# Ans: Indentation error because after: for if and else the line should contain one space(or)one tab space.
# =========================================
# Identify  error
#if  ():
			print('Hyd')
	#else:
					#print('Sec')
print('Bye')
# Ans: else: must be at the same level of indentation as if.
# =================================================
# Identify  error
# if  { }:
# {
# 	print('One')
# 	print('Two')
# 	print('Three')
# }
# else:
# {
# 	print('Four')
# 	print('Five')
# 	print('Six')
# }
print('Bye')
# Ans:No need of {} in python
# ===========================================
# Identify  error
if  ():
	print('One')
	print('Two')
	print('Three')
else:
#if  []:
	print('Four')
	print('Five')
	print('Six')
#else:
#if  {}:
# 	print('Seven')
# 	print('Eight')
# 	print('Nine')
# else:
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# print('Bye')
# Ans:Empty tuple is invalid & else if is not proper indentation & we can not use else if we can use only elif:
# =============================================
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")

# ==========================
if():
        print('Hyd')
        print('Sec')
        print('Cyb')
else:
        print('One')
        print('Two')
        print('Three')
print('Bye')
# Ans:one (here the if() is false so else will be displayed)
#     Two (because here the if condition is empty it displays else)
#     Three
# ===========================================
# Find  outputs  (Home  work)
if{10 : 20 , 30 : 40}:
        print('Hyd')
        print('Sec')
        print('Cyb')
print('Bye')
# Ans:{10: 20, 30: 40} is a non-empty dictionary, and in Python,the if condition is True
# ==========================================
# Find outputs  (Home  work)
if { }:
	print('Hyd')
	print('Sec')
	print('Cyb')
print('Bye')
# Ans: {} is a empty dict so no output
# 	Bye
# ========================================
import calendar

try:
    mnth = int(input("Enter month (1-12): "))
    year = int(input("Enter year: "))
    print(calendar.month(year, mnth))
except:
    print("Input month number should be between 1 and 12")
#Output:
	# Enter month number (1 - 12): 6
	# 			June
    #     Enter month number (1 - 12): 13
    #     Input  should  be  between  1  and   12
    #     Enter month number (1 - 12): 10.8
    #     Input  should  be  an  integer
