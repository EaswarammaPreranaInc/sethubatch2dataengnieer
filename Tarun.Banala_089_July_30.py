#Name: Tarun Banala   30-07-2025

n=int(input("enter number of lines: "))
for i in range(1,n+1):
    for j in range(i+1,n+1):
        print(" ",end="")
    print("*"*i,end="")
    for k in range(1,i):
        print("*",end="")
    print()
