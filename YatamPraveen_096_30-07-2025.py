# Input: number of lines for the pyramid

n = int(input("Enter the number of lines: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))