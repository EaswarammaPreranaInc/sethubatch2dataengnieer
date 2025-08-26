n=int(input("Enter Number of Rows="))
for i in range(n):
    left = "".join(chr(65 + j) for j in range(n - i))
    right=left[::-1]
    space = " " * (i) 
    if i == 0:
        print(left + right[1:]) 
    else:
        print(left + space + right)
