# write a recursive function to find sum of the digits of a number

def sod(n):
    if n == 0:
        return 0
    else:
        return (n%10) + sod(n//10)
n = int(input("enter any number:"))
print("sum of any digits:",sod(n))
