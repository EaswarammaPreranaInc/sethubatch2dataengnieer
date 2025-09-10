n= int(input())
s=n-1
for i in range(n):
    spaces = n - i - 1
    stars = 2 * i + 1
    print(' ' * spaces + '*' * stars)