from sys  import argv
try:
    a=[]
    for i in range(1,len(argv)):
        a.append(eval(argv[i]))
    s=sum(a)
    b=len(a)
    print(s/b)
except NameError:
    print("Pls send number input")
except ZeroDivisionError:
    print(" Pls  send  number  inputs")

