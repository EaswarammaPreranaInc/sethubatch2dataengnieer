from sys import argv
try:
    a=[]
    for i in range(1,len(argv)):
        a.append(eval(argv[i]))
    print(max(a))
except NameError:
    print("give string input in single or triple quotes ")

