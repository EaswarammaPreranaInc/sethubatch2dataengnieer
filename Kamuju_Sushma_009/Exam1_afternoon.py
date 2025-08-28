#check if string is palindrone or not
s=input("Enter the string: ")
n=len(s)
for i in range(len(s)/2):
    if s[i]!=s[n-1-i]:
        print("False")
        break
print(f'{s} is palindrone')

#check if n is armstrong
s=int(input("Enter the string: "))
x=int(s)
n=len(s)
res=0
for i in s:
    res+=(int(i),n)
if x==res:
    print("yes")
print("no")

#print pyramid of numbers
n=int(input(("Enter the no of rows: ")))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(i):
        print(j+1,end='')
    for j in range(i-1):
        print(j+1+i,end='')
    print()

#multiply matrices
# a=eval(input("Enter the 1st matrix: "))
# b=eval(input("Enter the 2nd matrix: "))
# n1=len(a)
# m1=len(a[0])
# n2=len(b)
# m2=len(b[0])
# if m1 !=n2 :
#     print("not possible to multiply")
#     exit()
# else:
#     for i in range(n1):
        

