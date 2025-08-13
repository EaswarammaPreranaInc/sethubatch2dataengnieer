
n=int(input("how many lines:"))
for i in range(n):
    spaces = n - i - 1             # Decreasing spaces
    stars = 2 * i + 1              # Increasing stars
    print(' ' * spaces + '*'* stars)