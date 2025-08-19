from sys import argv
try:
    a=[]
    for i in range(1,len(argv)):
        a.append(eval(argv[i]))
    b=sorted(a)
    c=sorted(a,reverse=True)
    print("sorted array",b)
    print("desc sorted array",c)
except NameError:
    print("enter str in single or triple quotes")