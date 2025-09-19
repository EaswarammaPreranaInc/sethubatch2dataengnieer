a = range(10, 50, 5)
print(type(a))                # <class 'range'>
print(a)                      # range(10, 50, 5)
print(*a)                     # 10 15 20 25 30 35 40 45
print(id(a))                  # Some integer (memory address, changes each run)
print(len(a))                 # 8 (values: 10, 15, 20, 25, 30, 35, 40, 45)
print(*a[2:7], sep=', ')       # 20, 25, 30, 35, 40
print(*a[::-1])               # 45 40 35 30 25 20 15 10
a[4] = 32                     #  Error
print(a * 2)                  # Error


a = range(10, 20)
print(*a, sep=',')            # 10,11,12,13,14,15,16,17,18,19
b = range(5)
print(*b)                     # 0 1 2 3 4
c = range(10, 1, -1)
print(*c, sep='...')          # 10...9...8...7...6...5...4...3...2
d = range(-10, 0)
print(*d)                     # -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
e = range(-10)
print(*e)                     # (empty, because default start=0, stop=-10, step=1 → no values)
f = range(2, 2)
print(*f)                     # (empty, start=2, stop=2 → no values)
g = range(10, 11, 0.1)        #  Error
h = range('A', 'F')           #  Error 


r = range(10, 17, 3)  # values → 10, 13, 16
a, b, c = r
print(a, b, c)        # 10 13 16
r = range(3)          # values → 0, 1, 2
x, y = r              #  Error
p, q, r, s = r        # Error
a, b, c = *r          # Error
