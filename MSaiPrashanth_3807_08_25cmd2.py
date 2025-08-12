from sys import argv
try:
    if (int(argv[1])) %2==0:
        print("Even")
    else:
        print("Odd")
except NameError:
    print("input must be integer")
except :
    print("enter any integer ")
