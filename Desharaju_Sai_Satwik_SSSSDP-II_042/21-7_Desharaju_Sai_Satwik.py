a  =  {10 : 'Ramesh' ,  20 : 'Kiran' , 15 : 'Amar' , 18 : 'Sita'}

# How  to  print  dictionary  with  print()  function
print(a)  # {10: 'Ramesh', 20: 'Kiran', 15: 'Amar', 18: 'Sita'}
for key a:
    print(key)

# How  to  print  each  key  of  dict  'a'
for i in a: 
    print(i)  # 10\n20\n15\n18 (each on new line)
print('Values  of  dictionary')  # Values  of dictionary
# How  to  print  each  value  of dict 'a'
for i in a:
   print(a[i])  # Ramesh\nKiran\nAmar\nSita

print('All  the  tuples  of  dict_items   object')  # All the tuples of dict_items object
# How to print each tuple of the list in dict_items object
for i in a.items():
    print(i)  # (10, 'Ramesh')\n(20, 'Kiran')\n(15, 'Amar')\n(18, 'Sita')

print('Elements  of  each   tuple')  # Elements of each tuple
# How to print elements of each tuple in the list of dict_items object
for i in a.items():
    print(i[0], i[1])  # 10 Ramesh\n20 Kiran\n15 Amar\n18 Sita
print('Keys  and  values  of  dictionary')  # Keys and values of dictionary
# How to print each key and corresponding value in dict 'a'
for i in a:
     print(i, a[i])  # 10 Ramesh\n20 Kiran\n15 Amar\n18 Sita


a = {
	print('Hyd') ,  # Hyd
	print('Sec') ,  # Sec
	print('Cyb')    # Cyb
}
print(type(a))  # <class 'set'>
print(a)        # {None}
print(len(a))   # 1
[21-07-2025 19:20] Sai Satwik: _ = 25
print(_)  # 25
print(type(_))  # <class 'int'>
a , _ , c = 10 , 20 , 30
print(a)  # 10
print(_)  # 20
print(c)  # 30
for  _  in  range(5):
	print(_ , 'Hello')  # 0 Hello\n1 Hello\n2 Hello\n3 Hello\n4 Hello

a = 25
print(id(a))  #  9785472
a = 35
print(id(a))  #  9785792
[21-07-2025 19:20] Sai Satwik: a = 25.7
print(id(a))  # (some id)
print(a)      # 25.7
a = 35.6
print(id(a))  # id
print(a)      # 35.6
b = True
print(id(b))  #   9480544
b = False
print(id(b))  # 478112
c = None
print(id(c))  # id
c = None
print(id(c))  # id
[21-07-2025 19:22] Sai Satwik: a = 'Hyd'
print(id(a))  #id
a[1] = 'e'  # error
a = 'Sec'
print(id(a))  # id
b = (10 , 20 , 15 , 18)
print(id(b))  #  id
b[2] = 19  # error
b = (30 , 40 , 35 , 32)
print(id(b))  #  id
c = range(5)
print(id(c))  #  id
c[3] = 10  # error
c = range(5)
print(id(c))  # id
[21-07-2025 19:22] Sai Satwik: a = 25
b = 25
print(a is b)  # True
c = 'Hyd'
d = 'Hyd'
print(c is d)  # True
e = False
f = False
print(e is f)  # True
g = range(10)
h = range(10)
print(g is h)  # False
[21-07-2025 19:23] Sai Satwik: a = [10 , 20 , 15 , 18]
b = [10 , 20 , 15 , 18]
print(a is b)  # False
c =  {10 : 20, 30 : 40}
d =  {10 : 20, 30 : 40}
print(c is d)  # False
e = (10 , 20 , 15 , 18)
f = (10 , 20 , 15 , 18)
print(e is f)  # True
g = {10 , 20 , 15 , 18}
h = {10 , 20 , 15 , 18}
print(g is h)  # False
[21-07-2025 19:23] Sai Satwik: print(10 + 20)  # 30
print(10.8 + 20.6)  # 31.4
print(3 + 4j + 5 + 6j)  # (8+10j)
print(True + False)  # 1
print('Hyder' + 'abad')  # Hyderabad
print('Sankar' + 'Dayal' + 'Sarma')  # SankarDayalSarma
print('10' + '20')  # 1020
print([10 , 20 , 30] + [1 , 2 , 3])  # [10, 20, 30, 1, 2, 3]
print((25 , 10.8 , 'Hyd') + (3 + 4j , True , None))  # (25, 10.8, 'Hyd', (3+4j), True, None)
print({10 , 20} + {30 , 40})  # error
print({10 : 'Hyd'} + {20 : 'Sec'})  # error
print(range(4) + range(5))  # error
print(10 + '20')  # error
print([10 , 20 , 30] + 5)  # error
print([10 , 20 , 30] + (40 , 50 , 60))  # error
[21-07-2025 19:23] Sai Satwik: print(25 * 3)  # 75
print(10.8 * 25.6)  # 276.48
print(True * False)  # 0
print((3 + 4j) * (5 + 6j))  # (-9+38j)
print(3 + 4j * 5 + 6j)  # (3+26j)
print('25' * 3)  # 252525
print(3 * '25')  # 252525
print('Hyd' * 4)  # HydHydHydHyd
print([10 , 20 , 15] * 2)  # [10, 20, 15, 10, 20, 15]
print((25, 10.8, 'Hyd', True) * 3)  # (25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True, 25, 10.8, 'Hyd', True)
print([10 , 20 , 15] * 3.0)  # error
print({10 , 20 , 15} * 2)  # error
print({10 : 20 , 30 : 40} * 2)  # error
print([10] * [20])  # error


print(9.0 / 2)  # 4.5
print(9 / 2.0)  # 4.5
print(9.0 / 2.0)  # 4.5
print(9 / 2)  # 4.5
print(10.5 / 2)  # 5.25
print(10 / 3)  # 3.3333333333333335
print(10 / 2)  # 5.0


print(9 // 2)  # 4
print(9.0 // 2)  # 4.0
print(9 // 2.0)  # 4.0
print(9.0 // 2.0)  # 4.0
print(10.5 // 2)  # 5.0
print(10 // 3)  # 3
print(10.0 // 3)  # 3.0
print(8.5 // 3)  # 2.0
print(18 // 4)  # 4
print(-18 // 4)  # -5
print(-(18 // 4))  # -4


print(9 % 5)  # 4
print(9.0 % 5)  # 4.0
print(9 % 5.0)  # 4.0
print(9.0 % 5.0)  # 4.0
print(10.5 % 2)  # 0.5
print(8.9 % 3)  # 2.9


print(7 / 0)  # error
print(7 // 0)  # error
print(7 % 0)  # error


print(3 ** 4)  # 81
print(10 ** -2)  # 0.01
print(4 ** 3 ** 2)  # 262144
print(3 + 4 * 5 - 32 / 2 ** 3)  # 21.0


print(9 >= 5)  # True
print(9 >= 9)  # True
print(9 >= 12)  # False
print(6 <= 8)  # True
print(6 <= 6)  # True
print(6 <= 4)  # False
print(9 != 7)  # True
print(6 == 8)  # False
print(True  >  False)  # True
print(3 + 4j == 3 + 4j)  # True
print(3 + 4j == 5 + 6j)  # False
print(3 + 4j != 5 + 6j)  # True
print(10 == 10.0)  # True
print(3 + 4j >  3 + 4j)  # error


print('Rama'   >  'Rajesh')  # True
print('Rama'  <  'Sita')  # True
print('Hyd'  ==  'Hyd')  # True
print('Rama'  <=   'Ramana')  # True
print('Rama  Rao'  >=  'Rama')  # True
print('Hyd'  != 'Sec')  # True
print('HYD'  <   'hyd')  # True


print(10 < 20 < 30)  # True
print(10 >= 20 < 30)  # False
print(10 < 20 > 30)  # False
print(1 < 2 < 3 < 4)  # True
print(1 < 2 > 3 > 1)  # False
print(4 > 3 >= 3 > 2)  # True


print(True  or  False)  # True
print(False  or  True)  # True
print(True  or  True)  # True
print(False  or   False)  # False
print(10  or  20)  # 10
print(0   or  20)  # 20
print(-25  or  0)  # -25
print(''  or  35)  # 35
print(6j  or  'Hyd')  # 6j
print(0.0  or  3 + 4j)  # (3+4j)
print('Hyd'   or   10.8)  # Hyd


print(not  True)  # False
print(not  False)  # True
print(not  25)  # False
print(not  0)  # True
print(not  'Hyd')  # False
print(not  '')  # True
print(not  -10)  # False
print(not  not  'Hyd')  # True
[21-07-2025 19:25] Sai Satwik: i = 10
i = not  i > 14
print(i)  # True
print(not(6 < 4  or  9 >= 5  and  6 != 6))  # True
