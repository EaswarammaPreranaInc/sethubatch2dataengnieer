
def prime (n):
    if n > 1:
        for i in range(2,(n//2) + 1):
            if (n % i) == 0:
                return False
        return True
    else:
        return False

x = int(input("Enter a number: "))
count = 0
print("Prime numbers")
for i in range(2, x + 1):
    if prime(i):
        print(i)
        count += 1
print("Number of prime numbers:", count)


#2nd program
# Find  outputs (Home  work)
def   disp(ch = '*' , n = 4):
        print(ch *  n)
# End of the function
disp('-' , 6)#------
disp('$')#$$$$
disp()#****
disp(n = 5)#*****
disp(5)#20
disp(n = 7 , ch = '%')#%%%%%%%
disp(7 , '@')#@@@@@@@
disp(7 , n = 6)#42
#disp(ch = '!' , 5)#positional argument follows keyword argument


#3rd program
# Find  outputs (Home  work)
def  power(a , b  =  2):
        return  a ** b
#end of the function
print(power(2 , 6))#64
print(power(5))#25
print(power(b = 3 , a = 4.5))#
print(power(3 + 4j))#(-7+24j)
print(power(True))#1

'''
def   power(b = 2 , a):#parameter without a default follows parameter with a default
 	     pass'''

#4th program
# Find outputs  (Home  work)
def  disp(a , b):
        print('2-argument function  :  ' , a , b)
def  disp(a , b , c , d):
        print('4-argument  function  :  ' , a , b , c , d)
def disp(a , b , c = 25):
        print('3-argument  function  :  ' , a , b , c)
#end
disp(10 , 20 , 30)#3-argument  function  :   10 20 30
#disp(40 , 50 , 60 , 70)
disp(80 , 90)#3-argument  function  :   80 90 25


