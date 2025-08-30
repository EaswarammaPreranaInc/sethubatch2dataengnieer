# 1. Check Leap Year
year = int(input("Enter year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 2. Largest of Three Numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
if a > b and a > c:
    print("Largest number:", a)
elif b > c:
    print("Largest number:", b)
else:
    print("Largest number:", c)

# 3. Celsius ↔ Fahrenheit Converter
choice = int(input("Enter 1 for Celsius to Fahrenheit, 2 for Fahrenheit to Celsius: "))
if choice == 1:
    c = float(input("Enter Celsius temperature: "))
    print("Fahrenheit Equivalent:", 1.8 * c + 32)
elif choice == 2:
    f = float(input("Enter Fahrenheit temperature: "))
    print("Celsius Equivalent:", round((f - 32) / 1.8, 2))
else:
    print("Invalid input")

# 4. Point in Quadrant
x = int(input("Enter x-coordinate: "))
y = int(input("Enter y-coordinate: "))
if x > 0 and y > 0:
    print("1st Quadrant")
elif x < 0 and y > 0:
    print("2nd Quadrant")
elif x < 0 and y < 0:
    print("3rd Quadrant")
elif x > 0 and y < 0:
    print("4th Quadrant")
elif x == 0 and y != 0:
    print("Y-axis")
elif y == 0 and x != 0:
    print("X-axis")
else:
    print("Origin")

# 5. Largest, Smallest, Middle of Three Numbers
a = float(input("Enter first input: "))
b = float(input("Enter second input: "))
c = float(input("Enter third input: "))
maxi = a
if b > maxi:
    maxi = b
if c > maxi:
    maxi = c
mini = a
if b < mini:
    mini = b
if c < mini:
    mini = c
mid = a + b + c - maxi - mini
print("Largest number:", maxi)
print("Smallest number:", mini)
print("Middle number:", mid)

# 6. Triangle Type and Area/Perimeter
import math
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))
if a + b > c and b + c > a and c + a > b:
    print("Valid Triangle")
    if a == b == c:
        area = (math.sqrt(3) / 4) * a ** 2
        print("Equilateral Triangle - Area:", round(area, 2))
    elif a == b or b == c or c == a:
        perimeter = a + b + c
        print("Isosceles Triangle - Perimeter:", perimeter)
    else:
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        perimeter = a + b + c
        print("Scalene Triangle - Area:", round(area, 2), "Perimeter:", perimeter)
else:
    print("Not a Triangle")

# 7. Quadratic Equation Roots
a = float(input("Enter a (a ≠ 0): "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = b**2 - 4*a*c
if d > 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print("Real and Distinct Roots:", r1, "and", r2)
elif d == 0:
    r = -b / (2*a)
    print("Real and Equal Roots:", r)
else:
    real = -b / (2*a)
    imag = math.sqrt(-d) / (2*a)
    print("Complex Roots:", complex(real, imag), "and", complex(real, -imag))

# 8. Point and Circle
x = float(input("Enter x: "))
y = float(input("Enter y: "))
r = float(input("Enter radius: "))
dist = math.sqrt(x*2 + y*2)
if dist < r:
    print("Inside the circle")
elif dist == r:
    print("On the circle")
else:
    print("Outside the circle")

# 9. Electricity Bill with match-case
units = int(input("Enter units: "))
match units // 100:
    case 0:
        cost = units * 3.0
    case 1:
        cost = 100 * 3.0 + (units - 100) * 3.5
    case 2 | 3:
        cost = 100 * 3.0 + 100 * 3.5 + (units - 200) * 4.0
    case 4 | 5 | 6:
        cost = 100 * 3.0 + 100 * 3.5 + 200 * 4.0 + (units - 400) * 4.5
    case _:
        cost = 100 * 3.0 + 100 * 3.5 + 200 * 4.0 + 300 * 4.5 + (units - 700) * 5.0
print("Bill amount:", cost)

# 10. Fibonacci Series up to x
x = int(input("Enter value of x: "))
a, b = 0, 1
print("Fibonacci Series:")
while a <= x:
    print(a, end=' ')
    a, b = b, a + b
print()

# 11. Infinite and False while loops
# Uncomment each to test one at a time:
# while True:
#     print("Hello")
#     print("Bye")

# while False:
#     print("Hello")
#     print("Bye")

# 12. Print elements from list with for loop
lst = [10, 20, 15, 18]
for x in lst:
    print(x)

for ch in 'Hyd':
    print(ch)

for i in range(5):
    print(i)

# 13. Dictionary Looping
d = {10: 20, 30: 40, 50: 60}
for x in d.keys():
    print(x)
for x in d.values():
    print(x)
for x in d.items():
    print(x)
for x in d:
    print(x)

# 14. Dictionary unpacking and errors
a = {10: 20, 30: 40, 50: 60}
for x, y in a.items():
    print(x, y, sep='...')

# 15. Errors in for loops
# for x in 123:  # Error: 'int' is not iterable
#     print(x)

for x in (): print(x)
for x in []: print(x)
for x in {}: print(x)
for x in set(): print(x)
for x in '': print(x)
for x in range(10, 10): print(x)
# for x in range(): print(x)  # Error: missing arguments
for x in (25,): print(x)

# 16. Nested Loop
for i in range(1, 4):
    for j in range(1, 5):
        print(i, j)
print("Bye")

# 17. Print index and elements
a = [25, 10.8, 'Hyd', True]
print('Indexed based for loop')
for i in range(len(a)):
    print(i, a[i])
print('For each loop')
for x in enumerate(a):
    print(x)

# 18. Reverse list printing
print("Reverse with indexed loop:")
for i in range(len(a)-1, -1, -1):
    print(a[i])
print("Reverse with for-each and reversed():")
for x in reversed(a):
    print(x)

# 19. Add two lists into third
a = [10, 20, 15, 18]
b = [30, 40, 35, 12, 100, 200, 300]
c = []
for i in range(min(len(a), len(b))):
    c.append(a[i] + b[i])
print("3rd list:", c)

# 20. List index 2 to 4 without slicing
a = [25, 10.8, 'Hyd', True, 3 + 4j, None, 'Sec']
print("Indexed loop (index 2 to 4):")
for i in range(2, 5):
    print(a[i])

print("For each loop (index 2 to 4):")
for i, val in enumerate(a):
    if 2 <= i <= 4:
        print(val)

# 21. Tricky List Increment
a = [10, 20, 15, 18]
for i in range(len(a)):
    a[i] += 1
print("a:", a)

b = [10, 20, 15, 18]
for x in b:
    x += 1
print("b:", b)  # N
[30-07-2025 11:21 PM] Sanketh: Sanketh

# Full Pyramid Program

# Input: number of lines
lines = int(input("How many lines? : "))

# Loop through each line
for i in range(lines):
    spaces = lines - i - 1
    stars = 2 * i + 1
    print(' ' * spaces + '*' * stars)
