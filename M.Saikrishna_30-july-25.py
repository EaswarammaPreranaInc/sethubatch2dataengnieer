n = int(input("Enter number of lines: "))

for i in range(1, n + 1):
    # Print spaces
    print(" " * (n - i), end="")
    # Print stars
    print("*" * (2 * i - 1))