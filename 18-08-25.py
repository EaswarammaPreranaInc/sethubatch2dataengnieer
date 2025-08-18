
#  len()  function demo   program  (Home  work)
a = [ 25, 10.8, 'Hyd', True]
print(len(a))#4
b = []
print(len(b))#0
c = [[10 , 20] , 30 , 40]
print(len(c))#3

#2nd program
# sum()  function  demo  program  (Home  work)
a = [25 , 10.8 , True]
print(sum(a))#36.8
b= [3 + 4j , 5 + 6j]
print(sum(b))#(8+10j)
c = [25 , 10.8 , True , 3 + 4j , False]
print(sum(c))#(39.8+4j)
d = [10 , 20 , 15 , 18]
print(sum(d))#63
e = [25 , 10.8 , 'Hyd' , True]
print(sum(e))#error int and string can't be added

#3rd program
#  Find  outputs
a = [[10 , 20 , 15 , 18]]
print(sum(a))#[10,20,15,18]
print(sum(a[0]))
print(sum(x for x in a[0]))

#4rth program
# max()  and  min()  functions  demo  program  (Home  work)
a = [10 , 20 , 15 , 18 , 30, 5 , 12]
print(max(a))#30
print(min(a))#5
b = ['Rama' , 'Sita' , 'Rajesh' , 'Kiran' , 'Amar' , 'Vamsi' , 'Manohar']
print(max(b))#Vamsi
print(min(b))#Amar
c = [25 , 10.8 ,  3 + 4j , True]
print(max(c))#Error
d = [25 , '35']
print(max(d))#Error
print(max([]))#Error
print(min([]))#Error

#5th program
# list()  function  demo  program
a = (10 , 20 , 15, 18)
b = list(a)
print(b)#[10,20,15,18]
print(type(b))#<class'list'>
print(a  is  b)#False
print(a==b)#True

#6th program
#  Find  outputs (Home  work)
a = range(4 , 10 , 2)
b = list(a)
print(b)#[4,6,8]
print(type(b))#<class'list'>
a = list('Vamsi')
print(a)#['v','a','m','s','i']
a = list()
print(a)#[]
print(list(25))#[25]
print(list(10.8))#[10.8]
print(list(True))#[True]
print(list(None))#[None]

#7th program
# Find  outputs (Home  work)
a = ((10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90))
print(list(a))#[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
b = { (10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)}
print(list(b))#[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]
c = ([10 , 20] , (30 , 40) , {50 , 60})
print(list(c))#[(10 , 20) , (30 , 40 , 50) , (60 , 70 , 80 , 90)]


#8TH PROGRAM
# sorted()  function   demo  program
a = [10 , 20 , 15 , 5 , 12]
b = sorted(a)
print(b)#[5,10,12,15,20]
print(type(b))#<class'list'>
c = sorted(a , reverse = True)
print(c)#[20,15,12,10,5]
print(a)#[10,20,15,5,12]


#9th program
# Find  outputs  (Home  work)
a = ['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']
b = sorted(a)
print(b)#['Amar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
c = sorted(a , reverse = True)
print(c)#['Vamsi','Sita','Rama Rao','Rama','Rajesh','Kiran','Amar']
print(a)#['Rama',  'Rajesh',  'Amar',  'Sita',  'Vamsi'  ,  'Kiran'  , 'Rama  Rao']

#10th program
# all()  function demo  program  (Home  work)
a = [12 > 10 , 5 < 20 , 30 == 30]
print(all(a))#True
b = [9 >= 6 , 12 <= 9 , 6 == 6]
print(all(b))#False
c = [25 , 10.8 , '' , True , 3+4j , 'Hyd']
print(all(c))#False
d = [10 , 0 , 20]
print(all(d))#False
e = []
print(all(e))#False

#11th program
# any()  function demo program  (Home  work)
a  = [12 > 18 , 5 < 20 , 35 == 30]
print(any(a))#True
b = [12 > 18 , 25 < 20 , 35 == 30]
print(any(b))#False
c = [0 , 0.0 , '' , 25 , 0 + 0j , False]
print(any(c))#True
d = [0 , 0.0 , '' , 0 + 0j , False]
print(any(d))#False
e = []
print(any(e))#False

#12th program
# del  operator  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10 , 20 , 15 , 18]
del    a[2]
print(a)#[10 , 20 , 18]
del  a[3]#Error
del a
print(a)#Error

#13th program
#  append()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18]
print(list)#[10 , 20 , 15 , 18]
list . append(19)
print(list)#[10 , 20 , 15 , 18 , 19]

#14th program
#  Find  outputs (Home  work)
list = []
print(list)#[]
list . append(25)#[25]
list . append(10.8)#[25,10.8]
list . append('Hyd')#[25,10.8,'Hyd']
list . append(True)#[25,10.8,'Hyd',True]
print(list)#[25,10.8,'Hyd',True]

#15th program
# Find  outputs  (Home  work)
list = []
for  x  in   range(0 , 50 , 10):
	list . append(x)
print(list)#[0,10,20,30,40]

#16th program
#  Find  outputs  (Home  work)
a = [10 , 20 , 30]
a . append('Hyd')
print(a)#[10 , 20 , 30 , 'Hyd']
print(len(a))#4
print(a[3])
print(a[3][0])
print(a[3][1])
print(a[3][2])

#17th program
# remove()  method  demo  program  (Home  work)
try:
	list = [10 , 20 , 15 , 18 , 15 , 12 , 15 , 19]
	list . remove(15)
	print(list)#[10 , 20 , 18 , 15 , 12 , 15 , 19]
	list . remove(25)
except:
	print('25  is   not  in  the  list')
	

#18th program
a=eval(input("Enter List: "))
b=eval(input("Enter element to be deleted: "))
for i in a:
  if i==b:
    a.remove(b)
print(a)


#19th program
# clear() method  demo program  (Home  work)
list = [10 , 20 , 15 , 18]
print(list)#[10 , 20 , 15 , 18]
list . clear()
print(list)#[]


#20th program
# reverse()  method  demo  program (Home  work)
a = [10 , 20 , 15 , 18]
print(a)#[10 , 20 , 15 , 18]
a . reverse()
print(a)#[18,15,20,10]


#21st program
#  sort()  method  demo  program (Home  work)
list = [10 , 20 , 15 , 18 , 5]
print(list)#[10 , 20 , 15 , 18 , 5]
list . sort()
print(list)#[5,10,15,18,20]
list . sort(reverse = True)
print(list)#[20,18,15,10,5]


#22nd program
# Find  outputs (Home  work)
a = ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
print(a)# ['Rama' , 'Rajesh' , 'Amar' ,  'Sita' ,  'Vamsi' , 'Kiran' , 'Rama  Rao']
a . sort()
print(a)#['Aamar','Kiran','Rajesh','Rama','Rama Rao','Sita','Vamsi']
a . sort(reverse =True)
print(a)#['Vamsi','Sita','Rama Rao','Rama','Rajesh','Kiran','Amar']


#23rd program
# Identify  error (Home  work)
a = [25 , 10.8 ,  'Hyd' ,  True]
a.sort()#Error due to string 'Hyd'


#24th program
#  count()  method  demo    program (Home  work)
a = [10 , 20 , 15 , 18 , 15 , 12 , 14 , 15 , 19]
print(a . count(15))#3
print(a . count(25))#Error
print(len(a))#7


#25th program
a = eval(input("Enter any list: "))
b = []
for x in a:
    if a.count(x) == 1:
        b.append(x)
print("List aremoving all duplicatesfter :", b)


#26th program
a=eval(input("enter any list:"))
if a.count(a[0])==len(a):
     print("identical")
else:
     print("not identical")

#27th program
# index()  method  demo  program  (Home  work)
a = [10 , 20 , 15 , 12 , 14 , 15 , 18 , 19 , 15 , 12 , 25]
#     0     1     2    3    4     5    6    7     8    9    10
try:
	i = a . index(15)
	while  True:
		print(i)
		i = a . index(15 , i + 1)
except:
	print(F'15  is  found  {a . count(15)}  times ')
#2\n5\n8

    
    