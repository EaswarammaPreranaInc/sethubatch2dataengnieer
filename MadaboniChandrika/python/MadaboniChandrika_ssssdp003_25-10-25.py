from prog7b import *
while True:
    try:
        inp=input("Enter number/string/exit: ")
        if inp=="exit":
            break
        classname=eval(inp)
        a=[classname(), classname()]
        a[0].get()
        a[1].get()
        a[2].add(a[0], a[1])
        a[2].display()
    except:
        print("pls enter valid input")
