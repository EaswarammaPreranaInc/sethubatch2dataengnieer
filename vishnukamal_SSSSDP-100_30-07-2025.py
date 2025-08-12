(30-07-2025)


# Input: number of lines for the pyramid
n = int(input("Enter the number of lines: "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))


# output:
Enter the number of lines:5
      *
    ***
   *****
 *******
*********