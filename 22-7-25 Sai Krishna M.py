_ = 25
print(_)#25
print(type(_))#<class 'int'>
a , _ , c = 10 , 20 , 30
print(a)#10
print(_)#20
print(c)#30
for  _  in  range(5):
    print(_ , 'Hello') # 0 Hello 1 Hello 2 Hello 3 Hello 4 Hello

a = 25
print(id(a))#140715722153144
a = 35
print(id(a))#140715722153464


a = 25.7
print(id(a))#1942266227824
print(a)#25.7
a = 35.6
print(id(a))#1942269821904
print(a)#35.6
b = True
print(id(b))#140715721358992
b = False
print(id(b))#140715721359024
c = None
print(id(c))#140715721359056
c = None
print(id(c))#140715721359056

