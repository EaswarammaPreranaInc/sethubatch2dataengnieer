n = int(input("enter no.of lines: "))
for i in range(n):
    for j in range(n - i-1):
        print(chr(65 + j), end="")
    if i > 0:
        print(" " * (2 * i - 1), end=" ")
    for j in range(n - i - 1, -1, -1):
        print(chr(65 + j), end="")
    print()