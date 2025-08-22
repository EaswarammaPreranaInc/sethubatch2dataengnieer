#1. program to print full pyramid
a = int(input("Enter a number :"))
for i in range(1,a+1):
    print(" " * (a-i)+ "* " * i)