#int object
'''
a=25
print(id(a))        # address of object 25
a=35                # modifies ref a to object 35
print(id(a))        # address of object 35
'''
#float-bool-None
'''
a=25.7
print(id(a))        # address of object 25.7
print(a)            # 25.7
a=35.6              # modifies ref 'a' to object 35.6
print(id(a))        # address of object 35.6
print(a)            # 35.6
b=True              # ref 'b' points to object True
print(id(b))        # address of object True
b=False             # ref 'b' points to object False
print(id(b))        # address of object False
c=None              # ref 'c' points to object None
print(id(c))        # address of object None
c=None              # Nothing is modified 'c' already exists
print(id(c))        # address of object None
'''
#str-tuple-range
'''
a='Hyd'
print(id(a))          # address of object a
a[1]='e'              # error char string cannot be modified str is immutable
a='Sec'               # modifies ref 'a' to object 'Sec
print(id(a))          # address of object 'Sec'
b=(10,20,15,18)
print(id(b))          # address of tuple
b[2]=19               # error due to tuple is immutable it cannot be modified
b=(30,40,35,32)
print(id(b))          # address of another tuple
c=range(5)
print(id(c))          # address of range object
c[3]=10               # error range object is immutable it cannot be modified
c=range(5)
print(id(c))          # address of 2nd range object
'''
#reuse
'''
a=25
b=25
print(a is b)     # True ref a and b points to same object
#int object is immutable and reusable
c='Hyd'
d='Hyd'
print(c is d)     # True ref c and d points to same object
#str object is immutable and reusable
e=False
f=False
print(e is f)      # True ref e and f points to same object
#bool object is immutable and reusable
g=range(10)
h=range(10)
print(g is h)     # False ref g and h points to different range objects
#range object is immutable but not reusable
'''
# reusable
'''
a=[10,20,15,18]
b=[10,20,15,18]
print(a is b)      # False ref a and b points to different lists
#list is mutable and not reusable
c={10:20,30:40}
d={10:20,30:40}
print(c is d)      # False ref c and d points to different dictionaries
#dict is mutable and not reusable
e=(10,20,15,18)
f=(10,20,15,18)
print(e is f)      # True ref e and f points to same tuple
#tuple is immutable and reusable
g={10,20,15,18}
h={10,20,15,18}
print(g is h)      # False ref g and h point to different sets
# set is mutable and not reusable
'''