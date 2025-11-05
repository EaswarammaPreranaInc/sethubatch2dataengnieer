'''
1.Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8
'''

#Program:
from pro7b import number , string
while True:
    ch=input('Enter choice (num/str/exit) : ')
    if ch=='num':
        a=[number(),number(),number()]
    elif ch=='str':
        a=[string(),string(),string()]
    else:
        break #How  to  stop  execution
    a[0].get()
    a[1].get()
    a[2].add(a[0],a[1])
    a[2].display()