# ===================================== Operators(Arithmetic,Relational,Logical) ===========================================

# ===================================== Arithemetic(+,-,*,/,%,//,**) ===========================================
print(10 + 20)#30
print(10.8 + 20.6)#34.6
print(3 + 4j + 5 + 6j)#8+10j
print(True + False)#1+0 = 1
print('Hyder' + 'abad')#Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')#SankarDayalSarma
print('10' + '20')#1020
print([10,20,30]+[1,2,3])#[10,20,30,1,2,3]
print((25,10.8,'Hyd')+(3 + 4j,True,None))#(25,10.8,'Hyd'(3 + 4j),True,None)
#print({10,20}+{30,40})#TypeError: unsupported operand type(s) for +: 'set' and 'set'
#print({10:'Hyd'}+{20:'Sec'})#TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
#print(range(4)+range(5))#TypeError: unsupported operand type(s) for +: 'range' and 'range'
#print(10+'20')#Error TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print([10,20,30]+5)#TypeError: can only concatenate list (not "int") to list
#print([10,20,30]+(40,50,60))#Error TypeError: can only concatenate list (not "tuple") to list

print(25 * 3)#75
print(10.8 * 25.6)#
print(True * False)#0
print((3+4j)*(5+6j))#(a+bj)*(a+bj) = (a*a)+(abj+abj)+(bj*bj) = (15+18j+20j+(24*-1)) = (-9 + 38j)
print(3 + 4j * 5 + 6j)#3+20j+6j = (3+26j)
print('25'*3)#252525
print(3*'25')#252525
print('Hyd'*4)#HydHydHydHyd
print([10,20,15]*2)#[10,20,15,10,20,15]
print((25,10.8,'Hyd',True)*3)#(25,10.8,'Hyd',True,25,10.8,'Hyd',True,25,10.8,'Hyd',True)
#print([10,20,15]*3.0)#Error TypeError: can't multiply sequence by non-int of type 'float'
#print({10,20,15}*2)#Error TypeError: unsupported operand type(s) for *: 'set' and 'int'
#print({10:20,30:40}*2)#Error TypeError: unsupported operand type(s) for *: 'dict' and 'int'
#print([10]*[20])#Error TypeError: can't multiply sequence by non-int of type 'list'

print(9.0 / 2)#4.5
print(9 / 2.0)#4.5
print(9.0 / 2.0)#4.5
print(9 / 2)  #  4.5
print(10.5 / 2)#5.25
print(10 / 3)#3.33
print(10 / 2)#5.0

print(9 // 2)  # prev  integer  of (4.5) = 4
print(9.0 // 2)# prev  integer  of (4.5) = 4.0
print(9 // 2.0)# prev  integer  of (4.5) = 4.0
print(9.0 // 2.0)# prev  integer  of (4.5) = 4.0
print(10.5 // 2)# prev  integer  of (5.25) = 5.0
print(10 // 3)# prev  integer  of (3.3333) = 3
print(10.0 // 3)# prev  integer  of (3.333) = 3.0
print(8.5 // 3)# prev  integer  of (2.8) = 2.0
print(18 // 4)# prev  integer  of (4.5) = 4
print(-18 // 4)# prev  integer  of (4.5) = -5
print(-(18 // 4))# prev  integer  of (4.5) = -4

print(9 % 5)#4
print(9.0 % 5)#4.0
print(9 % 5.0)#4.0
print(9.0 % 5.0)#4.0
print(10.5 % 2)#0.5
print(8.9 % 3)#2.90

#print(7 / 0)#Undefined ZeroDivisionError: division by zero
#print(7 // 0)#Undefined ZeroDivisionError: integer division or modulo by zero
#print(7%0)#ZeroDivisionError: integer modulo by zero

print(3 ** 4)#81
print(10 ** -2)#0.01
print(4 ** 3 ** 2)#(4**9) - 262144
print(3 + 4 * 5 - 32 / 2 ** 3)#19.0

# ===================================== Relational(>,>=,<,<=,==,!=) ===========================================
print(9 >= 5) #   True :  >  is  satisfied
print(9 >= 9) #   True :  =  is  satisfied
print(9 >= 12)#  False :  Both  are  not  satisfied
print(6 <= 8) #   True :  < is  satisfied
print(6 <= 6) #   True :  =  is  satisfied
print(6 <= 4) #  False :  Both  are  not  satisfied
print(9 != 7) #   True :  !  is  satisfied
print(6 == 8) #  False :  ==  is  not satisfied
print(True  >  False)# #   True : 1 > 0  is  satisfied
print(3 + 4j == 3 + 4j)#   True :  ==  is  satisfied
print(3 + 4j == 5 + 6j)#  False :  ==  is  not satisfied
print(3 + 4j != 5 + 6j)#   True :  !=  is  satisfied
print(10 == 10.0)#True :  ==  is  satisfied
#print(3 + 4j >  3 + 4j)#TypeError: '>' not supported between instances of 'complex' and 'complex'

print('Rama'   >  'Rajesh')# True :  'm' > 'j'
print('Rama'  <  'Sita')# True : 'R' < 'S'
print('Hyd'  ==  'Hyd')# True : 'H' == 'H'
print('Rama'  <=   'Ramana')#True 
print('Rama  Rao'  >=  'Rama')#True 
print('Hyd'  != 'Sec')#True
print('HYD'  <   'hyd')#True 

print(10 < 20 < 30)# True
print(10 >= 20 < 30)# False : 10  is  not  >= 20
print(10 < 20 > 30)#False : 10<20 True 1>30 is False 
print(1 < 2 < 3 < 4)#True : 1<2 True and 1<3 True and 1<4 True 
print(1 < 2 > 3 > 1)#False : 1<2 True and 1>3 False
print(4>3>=3>2)#True 


# ===================================== Logical(and,or,not) ===========================================

print(True  or  False)# True
print(False  or  True)# True
print(True  or  True)#  True
print(False  or   False)# False
print(10  or  20)#  10
print(0   or  20)#  20
print(-25  or  0)# -25
print(''  or  35)# 35
print(6j  or  'Hyd')#6j
print(0.0  or  3 + 4j)#(3+4j)
print('Hyd'   or   10.8)#Hyd 


print(not  True) #   False
print(not  False) #  True
print(not  25)#False 
print(not  0)#True
print(not  'Hyd')#False
print(not  '')#True 
print(not  -10)#False 
print(not  not  'Hyd')#True


i = 10
i = not  i > 14#True 
print(i)#10
print(not(6<4 or 9>=5 and 6!=6))#not(False or True and False) -> not(True and False) -> True 























