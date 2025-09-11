# Wite a program to calculate L.C.M for a given set of numbers

import math

def lcm(num):
    if not num:
        return None
    lcm = num[0]
    for n in num[1:]:
        lcm = lcm * n // math.gcd(lcm, n)
    return lcm

n = input("Enter numbers separated by space: ").split()
num = []
for x in n:
    num.append(int(x))
print("LCM:", lcm(num))
