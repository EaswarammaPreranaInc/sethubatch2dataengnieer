1.
def print_full_pyramid (num_lines):
Prints a full pyramid pattern of asterisks.
Args:
num lines (int): The number of lines (rows) for the pyramid.
if num_lines <= 0:
print("Please enter a positive number of lines.")
return
# Outer loop for the number of rows for i in range(1, num_lines + 1):
# Print leading spaces
# The number of spaces decreases with each row
# For n lines, the first row has (n-1) spaces, second (n-2), etc. # This can be calculated as num_lines - i
print(" " * (num_lines - i), end="")
# Print asterisks
# The number of asterisks increases by 2 with each row
# For row i, the number of asterisks is (2 * i - 1) print("*"* (2* i - 1))
# Get input from the user
try:
lines = int(input("Enter the number of lines for the pyramid: ")) print_full_pyramid(lines)
except ValueError:
print("Invalid input. Please enter an integer.")
