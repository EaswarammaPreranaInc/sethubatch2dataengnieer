#str-demo
a="Rama rao"
print(a)                      # Rama rao
print(type(a))                # <class 'str'>
print(id(a))                  # address of object "Rama rao"
b='Hyd'
print(b)                         # Hyd
c='''Hyd is green city
     Hyd is hitec city
     Hyd is beautiful city
'''
print(c)                         # Hyd is green city <next line> Hyd is hitec city <next line> Hyd is beautiful city

#index() demo
'''
a='Hyd'
print('Hyd[0]')           # 'H'
print('Hyd[1]')           # 'y'
print('Hyd[2]')           # 'd'
#print(a[3])
print('Hyd[-1]')          # 'd'
print('Hyd[-2]')          # 'y'
print('Hyd[-3]')          # 'H'
#print(a[-4])             # error index 4 do not exist
print(a[0]==a[-3])        # 'H'=='H'
#a[2]='c'                 # str object is immutable it cannot be modified
#print(25[0])             # error non sequence is not indexed
print('25'[0])            # index 0 of object '25' i.e. '2'
#print(True[1])           # error non sequence is not is indexed
print('True'[1])          # char index 1 of 'True' i.e. 'r'
'''
#repeat-obj
'''
a='Hyd'
print(a*3)            # HydHydHyd
print(a*2)            # HydHyd
print(a*1)            # Hyd
print(a*0)            # 0 i.e. empty string
print(a*-1)           # empty string
print(25*3)           # 75
print('25'*3)         # '252525'
#print('25'*4.0)      # error due to float operand 4.0
print(3*'Hyd')        # HydHydHyd
print('25'*True)      # 25 
'''
#repeat-str-object
'''
a='Hyd'
print(a,id)        # Hyd  address of 'Hyd'
a=a*3              # 'HydHydHyd'
print(a,id(a))     # HydHydHyd  address of a
'''
# length()
'''
print(len('Hyd'))        # 3
print(len('Rama Rao'))   # 8
print(len('9247'))       # 4
print(len(''))           # 0 due to empty string
print(len(' '))          # 1 due to space
#print(len(689))  # error:argument should be a sequence but 689 is not a sequence
'''
#Excess-Quotes
'''
a=""""Hyd"""
print(a)             # "Hyd
print(len(a))        # 4
print(a[0])          # "
#print("""Hyd"""")   # error due to excess closing quote
b="""""Hyd"""        
print(b)             # ""Hyd
print(len(b))        # 5
'''
#slice-demo
'''
a='Sankar Dayal Sarma'
print(a[7:12])          # Dayal
print(a[7: ])           # Dayal Sarma
print(a[ :6])           # Sankar
print(a[ : ])           # Sankar Dayal Sarma
print(a[1:10:2])        # akrDy
print(a[0: :2])         # sna aa am
print(a[1: :2])         # akrDylSra
print(a[-5:-1])         # Sarm
print(a[::-1])          # Reverse string
print(a[-1:-5:-1])      # amra
print(a[::-2])          # arSlyDrka
print(a[3:-3])          # kar Dayal Sa
print(a[2:-5])          # nkar Dayal 
print(a[-1:-5])         # Empty string
print(a[3:3])           # Empty string
'''
#index-slice
'''
a='A'
#print(a[1])            # index 1 does not exist
print(a[1:])            
'''
#int() function
'''
print(int(10.8))        # convert 10.8 to 10
print(int(True))        # convert True to 1
print(int(False))       # convert False to 0
print(int('25'))        # convert '25' to 25
print(int('0075'))      # convert '0075' to 75
print(int(0B11010))     # convert binary to decimal i.e. 16+8+2=26
print(0B11010)          # convert binary to decimal i.e. 16+8+2=26
print(int(0O6247))      # convert octal to decimal i.e. 6*8^3+2*8^2+4*8^1+7*8^0=3239
print(int(0o6247))      # convert octal to decimal i.e. 6*8^3+2*8^2+4*8^1+7*8^0=3239
print(int(0XA7B9))      # convert hexa-decimal to decimal i.e. 10*16^3+7*16^2+11*16^1+9*16^0=42937
print(int(0xa7b9))      # convert hexa-decimal to decimal i.e. 10*16^3+7*16^2+11*16^1+9*16^0=42937
#print(int(3+4j))       # error complex cannot be converted to int
#print(int('25.4'))     # error string float cannot be converted to int
#print(int('Ten'))      # error 'Ten cannot be converted to int
'''
#float() function
'''
print(float(25))        # convert 25 to 25.0
print(float(True))      # convert True to 1.0
print(float(False))     # convert False to 0.0
print(float('92'))      # convert '92' to 92.0
print(float('36.4'))    # convert '36.4' to 36.4
print(float('0075'))    # convert '0075' to 75.0
print(float(0B1010101)) # convert binary to decimal i.e. 64+16+4+1=85.0
print(float(0o6247))    # convert octal to decimal i.e. 6*8^3+2*8^2+4*8^1+7*8^0=3239.0
print(float(0xa7b9))    # convert hexa decimal to decimal i.e. 10*16^3+7*16^2+11*16^1+9*16^0=42937.0
#print(float(3+4j))     # error complex cannot be converted to float
#print(float('Ten'))    # error 'Ten' cannot be converted to float
'''
#complex() function
'''
print(complex(3,4))            # (3+4j)
print(complex(0,4))            # 4j
print(complex(3))              # (3+0j)
print(complex(3.8 , 4.6))      # (3.8+4.6j)
print(complex(3,4.5))          # (3+4.5j)
print(complex(True , False))   # (1+0j)
print(complex(True))           # (1+0j)
print(complex(False))          # 0j
print(complex(True,4))         # (1+4j)
print(complex('3'))            # (3+0j)
print(complex('3.8'))          # (3.8+0j)
#print(complex(3,'4'))         # error 2nd argument cannot be string
#print(complex('3',4))         # error 2nd argument is not permitted as 1st argument is string
#print(complex('3','4'))       # error 2nd argument is not permitted as 1st argument is string
#print(complex('Ten'))         # error 'Ten' cannot be converted to complex
'''
#bool() function
'''
print(bool(0))            # False due to 0
print(bool(10))           # True 10 in non-zero
print(bool(-25))          # True -25 is non-zero
print(bool(0.0))          # False due to 0.0
print(bool(0.1))          # True 0.1 is non-zero
print(bool(0+0j))         # False both real and imag are zeros
print(bool(10+20j))       # True real is non-zero
print(bool(-15j))         # True imag is non-zero
print(bool('False'))      # True 'False' is non-empty string
print(bool(''))           # False due to empty string
print(bool('Hyd'))        # True 'Hyd' is non-empty string
print(bool(' '))          # True ' ' is non-empty string
print(bool('True'))       # True is non-empty string
'''
#str() function
'''
print(str(25))          # converts 25 to '25'
print(str(10.8))        # converts 10.8 to '10.8'
print(str(3+4j))        # converts 3+4j to '3+4j'
print(str(True))        # converts True to 'True'
print(str(False))       # converts False to 'False'
print(str(None))        # converts None to 'None'
'''
#bin() function
'''
print(bin(25))          # converts decimal 25 to binary i.e. 0B11001
print(bin(0o6247))      # converts ocatl to binary i.e. 0B110 010 100 111
print(bin(0xa7b9))      # converts hexa-decimal to binary i.e. 0B1010 0111 1011 1001
'''
#oct() function
'''
print(oct(195))            # converts decimal to octal i.e. 0o303
print(oct(0b10101110010))  # converts binary to octal i.e. 0o2562
print(oct(0xa7b9))         # converts hexa-decimal to octal i.e. 0o123671
'''
#hex() function
'''
print(hex(25))               # converts decimal to hexa-decimal i.e. 0X19
print(hex(0b10101111010111)) # converts binary to hexa-decimal i.e. 0x2BD7
print(hex(0o6247))           # converts octal to hexa-decimal i.e. 0xca7
''' 
#range demo1
'''
a=range(10,50,5)       
print(type(a))          # <class 'range'>
print(a)                # range(10,50,5)
print(*a)               # 10 15 20 25 30 35 40 45
print(id(a))            # addresss of range object
print(len(a))           # 8
print(*a[2:7])          # 20,25,30,35,40
print(*a[::-1])         # 45 40 35 30 25 20 15 10
#a[4]=32                # it is immutable range object cannot be modified
#print(a*2)             # range object cannot be repeated
'''
#range-demo2
'''
a=range(10,20)          # range(10,20,1)
print(*a,sep=',')       # 10,11,12,13,14,15,16,17,18,19
b=range(5)              # range(0,5,1)
print(*b)               # 0 1 2 3 4
c=range(10,1,-1)        
print(*c,sep='...')     # 10...9...8...7...6...5...4...3...2
d=range(-10,0)          # range(-10,0,1)
print(*d)               # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e=range(-10)            # range(0,-10,1)  empty object due to 0>=-10
print(*e)               # nothing
f=range(2,2)            # range(2,2,1)
print(*f)               # unpacks empty object nothing
#g=range(10,11,0.1)     # range object cannot hold float objects
#h=range('A','F')       # range object cannot hold str elements
'''
#unpack-range 1
'''
r=range(10 , 17 , 3)     
a,b,c = r
print(a,b,c)             # 10 13 16
r=range(3)               # elements from 0 to 2 in steps 1
#x,y=r                   # error due to excess elements in range object
#p,q,r,s=r               # error due to few elements in range object
#a,b,c=*r                # error due to * operator
m=r                      # ref 'm' points to object 'r'
print(id(r))             # address of range object 'm'
print(id(m))             # same address
'''
#list demo 
'''
a=[25,'10.8','Hyd',True,3+4j,None,'Hyd',25]
print(a)             # [25,'10.8','Hyd',True,3+4j,None,'Hyd',25]
print(*a)            # 25 10.8 'Hyd' True 3+4j None 'Hyd' 25
print(type(a))       # <class 'list'>
print(id(a))         # address of object a list 
print(len(a))        # 8
a[2]='Sec'           # list of index 2 is modified to 'Sec'
print(a)             # [25,'10.8','Sec',True,3+4j,None,'Hyd',25]
print(a[2:5])        # ['Sec',True,3+4j]
'''
#print list
'''
a=[25,20.8,'Hyd',True]
print(a)                    
for x in a:
    print(x)  
print()                
for i in range(len(a)):
    print(a[i])
print()
for i in range(1,len(a)+1):
    print(a[-i])
a[::-1]
'''
#output
'''
[25,20.8,'Hyd',True]
25
20.8
'Hyd'
True

25
20.8
Hyd
True

True
Hyd
20.8
25
'''
#append-remove
'''
a=[]
print(a)         # []
a.append(25)     # append 25 to empty list
a.append(10.8)   # append 10.8 to list
a.append('Hyd')  # append 'Hyd' to list
a.append(True)   # append True to list
print(a)         # [25,10.8,'Hyd',True]
a.remove('Hyd')  # removes 'Hyd' from list
print(a)         # [25,10.8,True]
#a.remove('25')  # error '25' is not in list
print(a)         # [25,10.8,True]
'''
#list-repeat
'''
a=[25,10.8,'Hyd']
print(a)        # [25,10.8,'Hyd']
print(id(a))    # address of list a
print(a*3)      # [25,10.8,'Hyd',25,10.8,'Hyd',25,10.8,'Hyd']
print(a*2)      # [25,10.8,'Hyd',25,10.8,'Hyd']
print(a*1)      # [25,10.8,'Hyd']
print(a*0)      # 0   i.e.[]
print(a*-1)     # []
#print(a*4.0)   # error due to float operand
a=a*3           
print(a)        # [25,10.8,'Hyd',25,10.8,'Hyd',25,10.8,'Hyd']
print(id(a))    # address of list a i.e. 9 elements
a=[25]  
print(a,id(a))  # [25]  address of list i.e. single element
#print(a*a)    # error operand should be an integer but not list
'''
# list() function
'''
a=list('Hyd')          # converts string to list
print(a)               # ['H','y','d']
print(type(a))         # <class 'list'>
print(len(a))          # 3
b=(10,20,15,18)        # tuple to ()
print(list(b))         # converts tuple to list  i.e. [10,20,15,18]
print(list(range(5)))  # converts range object to list i.e. [0,1,2,3,4]
#print(list(25))       # error 25 is not a sequence
'''
#empty list
'''
a=[]
print(type(a))         # <class 'int'>
print(a)               # []
print(len(a))          # 0
b=list()               # empty list
print(b)               # []
print(len(b))          # 0
'''
#list-slice-demo1
'''
list=[25,10.8,3+4j,'Hyd',True,None,10.8,'Hyd']
print(list[2:7])         # [3+4j,'Hyd',True,None,10.8]
print(list[::])          # [25,10.8,3+4j,'Hyd',True,None,10.8,'Hyd']
print(list[:])           # [25,10.8,3+4j,'Hyd',True,None,10.8,'Hyd']
print(list[::-1])        # ['Hyd',10.8,None,True,'Hyd',3+4j,10.8,25]
print(list[::2])         # [25,(3+4j),True,10.8]
print(list[1::2])        # [10.8,'Hyd',None,'Hyd']
print(list[::-2])        # ['Hyd',None,'Hyd',10.8]
print(list[-2::-2])      # [10.8,True,(3+4j),25]
print(list[1:4])         # [10.8,(3+4j),'Hyd']
print(list[-4:-1])       # [True,'Hyd',(3+4j),10.8,25]
print(list[3:-3])        # ['Hyd',True]
print(list[2:-5])        # [3+4j]
print(list[-1:-5])       # []
'''
# list-slice-demo2
'''
list=[25,10.8,3+4j,'Hyd',True,None,10.8,'Hyd']
x,y=list[3:5]
print('x:',x)
print('y:',y)
for x in list[2:7]:
    print(x)
'''
#output
'''
x,y=['Hyd',True]
x:Hyd
y:True
(3+4j)
'Hyd'
True
None 
10.8
'''
#list-slice-demo3
''' 
a=[10,20,30,40,50]      
print(a,id(a))           # [10,20,30,40,50]  address of list
a[1:4]=[60,70]           # modifies elements from list 1 to 3 to 60,70
print(a,id(a))           # [10,60,70,50]  same address 
a[2:4]=[100,200,300]     # modifies elements of list from 2 to 3 to 100,200,300
print(a,id(a))           # [10,60,100,200,300]  same address
'''
#index-slice
'''
a=[25]
#print(a[1])   #error index 1 do not exist
print(a[1:])
'''
#tuple demo
'''
a=(25,10.8,'Hyd',True,3+4j,None,'Hyd',25)
print(a)           # (25,10.8,'Hyd',True,3+4j,None,'Hyd',25)
print(*a)          # 25 10.8 'Hyd' True 3+4j None 'Hyd' 25
print(type(a))     # <class 'tuple'>
print(len(a))      # 8
print(a[2:5])      # ('Hyd',True,(3+4j))
print(*a[2:5])     # hyd True (3+4j)
#a[2]='Sec'        # tuple is immutable it cannot be modified
#a.append('Sec')   # no append method 
#a.remove('Hyd')   # no remove method
b=10,20,30         # tuple object () are optional
print(b)           # (10,20,30)
print(b*2)         # (10,20,30,10,20,30)
c=40,50,60,        # vaild tuple due to comma
print(c)           # (40,50,60)
print(type(c))     # <class 'tuple'>
'''
#single element
'''
a=(25)
b=25,
c=25
d=(25,)
print(type(a))      # <class 'int'>
print(type(b))      # <class 'tuple'>
print(type(c))      # <class 'int'>
print(type(d))      # <class 'tuple'>
print(a*4)          # 25*4=100
print(b*4)          # (25,25,25,25)
print(c*4)          # 100
print(d*4)          # (25,25,25,25)
'''
#tuple() function
'''
a=tuple('Hyd')          # convert tuple to string
print(a)                # ('H','y','d')
print(type(a))          # <class 'tuple'>
print(len(a))           # 3
b=[10,20,15,18]         # converts list to tuple
print(tuple(b))         # (10,20,15,18)
print(tuple(range(5)))  # converts range to tuple i.e. (0,1,2,3,4)
#print(tuple(25))       # 25 is not in sequence
'''
#empty tuple()
'''
a=()                 # empty tuple
print(type(a))       # <class 'tuple'>
print(a)             # ()
print(len(a))        # 0
b=tuple()            # empty tuple
print(b)             # ()
print(len(b))        # 0
'''
#tuple-repeat()
'''
a=(10,20,30)
print(a)             # (10,20,30)
print(id(a))         # address of tuple a
a=a*2                 
print(a)             # (10,20,30,10,20,30)
print(id(a))         # address of tuple a i.e. 6 elements
'''
#set-demo1
'''
a={25,10.8,'Hyd',True,3+4j,None,25,'Hyd'}
print(a)          # {25,10.8,'Hyd',True,3+4j,None,}
print(type(a))    # <class 'set'>
print(len(a))     # 6
#print(a[2])      # set is not indexed
#print(a[1:4])    # set cannot be sliced
#a[2]='Sec'       # tuple is immutable it cannot be modified
#print(a*2)       # set cannot be repeated
#print(a*a)       # set cannot be repeated
'''
#set-demo2
'''
a={1,'Hyd',False,True,0.0,'',1.0,0}
print(a)         # {'Hyd',True,0.0,''}
print(len(a))    # 4
print(type(a))   # <class 'set>
'''
#set() function
'''
a=set('Rama rAo')
print(a)                           # {'R','a','m',' ','r','A','o'}
print(len(a))                      # 7
print(set([10,20,15,20]))          # converts list to set i.e. {20,10,15}
print(set([25,10.8,'Hyd',10.8]))   # converts tuple to set i.e. {25,10.8,'Hyd'}
print(set(range(10,20,3)))         # converts range object to set i.e. {10,13,16,19}
#print(set(25))                    # 25 is not a sequence
'''
#empty-set
'''
a=[ ]             # empty list
b=( )             # empty tuple
c={ }             # empty dictionary
d=set()           # empty set
print(type(a))    # <class 'List'>
print(type(b))    # <class 'Tuple'>
print(type(c))    # <class 'dict'>
print(type(d))    # <class 'set'>
print(a)          # []
print(b)          # ()
print(c)          # {}
print(d)          # set()
'''
#add()-remove() methods
'''
a=set()             # empty set
a.add(25)           # insert 25 to empty set
a.add(10.8)         # insert 10.8 to set
a.add('Hyd')        # insert 'Hyd' to set
a.add(True)         # insert True to set
a.add(None)         # insert None to set
a.add('Hyd')        # set do not conatains duplicate elements
a.add(1)            # set do not conatains duplicate elements
print(a)            # {10.8,'Hyd',25,True,None}
print(len(a))       # 5
a.remove(25)        # removes 25 from set
print(a)            # {10.8,None,True,'Hyd'}
#a.appen(100)       # no append() method in set
#a.add(set())       # set is mutable it cannot be inserted
a.add(())           # inserted () anywhere in set
#a.add([])          # list is mutable it cannot be inserted
print(a)            # {10.8,None,True,(),'Hyd'}
#a.add({})          # dict is mutable it cannot be inserted
'''
#print-set
'''
a={25,True,'Hyd',10.8}
print(a)
for x in a:
    print(x)
'''

#output
'''
{25, 10.8, 'Hyd', True}
25
10.8
Hyd
True
'''
#dict-demo1
'''
a={10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}
print(a)            # {10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}
print(type(a))      # <claa 'dict'>
print(a[10])        # Ramesh
print(a[20])        # Kiran
print(a[15])        # Amar
print(a[18])        # Sita
#print(a[19])       # a[19] does not exist
#print(a[0])        # a[0]  does not exist
#print(a['Amar'])   # a['Amar'] does not exist
a[15]               # value of key 15 is modified to 'krishna' in dict 'a'
del a[20]           # removes 20:'Kiran' from dict 'a'
a[25]='Vamsi'       # appends 25:'Vamsi' to dict 'a'
print(a)            # {10:'Ramesh',15:'Krishna',18:'Sita',25:'Vamsi'}
print(len(a))       # 4
#print(a*2)          # dict cannot be repeated it does not has duplicate keys
'''
#dict-demo2
'''
a={10:'Hyd',10:'Sec'}
print(a)                  # {10:'Sec'}
print(len(a))             # 1
b={'R':'Red','G':'Green','B':'Blue','Y':'Yellow','G':'Grey','B':'Black'}
print(b)                  # {'R':'Red','G':'Grey','B':'Black','Y':'Yellow',}
print(len(b))             # 4
'''
#dict-demo3
'''
a={True:'Yes',1:'No',1.0:'May be'}
print(a)          # {True:'May be'}
print(len(a))     # 1
'''
#dict-demo4
'''
#a={[]:25}     # key cannot have mutable object such as list
b={():25}
print(b)            # {():25}
#c={{}:25}        # key cannot have mutable object such as dict
d={'Ramesh':[12345,12354,12543]}
print(len(d))      # 1
#e={set():10.8}   # key cannot have mutable object such as set
'''
#empty-dict
'''
a={}                 # empty dictionary
print(type(a))       # <class 'dict'>     
print(len(a))        # 0
print(a)             # {}
b=dict()             # empty dictionary
print(type(b))       # <class 'dict'>
print(len(b))        # 0
print(b)             # {}
'''
#keys-values-items
'''
a={10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}
print(a.keys())         # dict_keys([10,20,15,18])
print(a.values())       # dict_values(['Ramesh','kiran','Amar','Sita'])
print(a.items())        # dict_items([(10,'Ramesh'),(20,'kiran'),(15,'Amar'),(18,'Sita)])
print(a)                # {10:'Ramesh',20:'Kiran',15:'Amar',18:'Sita'}
'''
#suite1
'''
print('Hyd')
 #print('Sec')  # error due to space before print
 #print('Cyb')  # error due to space before print
'''
#suite2
'''
a={
    print('Hyd'),
    print('Sec'),
    print('Cyb'),
}
print(type(a))
print(a)
print(len(a))
'''
#anonymous-object
'''
_=25
print(_)             # 25
print(type(_))       # <class 'int'>
a,_,c=10,20,30
print(a)             # 10
print(_)             # 20
print(c)             # 30
for _ in range(5):
    print(_,'Hello')  
'''
#output
'''
25
<class 'int'>
10
20
30
0 Hello
1 Hello
2 Hello
3 Hello
4 Hello
'''
