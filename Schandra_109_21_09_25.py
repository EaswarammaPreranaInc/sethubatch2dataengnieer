1) GCD of 3 numbers (without predefined function)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)   # handle negative values

def gcd_three(a, b, c):
    return gcd(gcd(a, b), c)

# Examples
print("gcd(12, 15, 9) =", gcd_three(12, 15, 9))
print("gcd(4, 7, 21) =", gcd_three(4, 7, 21))
print("gcd(0, 7, 14) =", gcd_three(0, 7, 14))
print("gcd(3, 0, 9) =", gcd_three(3, 0, 9))
print("gcd(12, -18, 6) =", gcd_three(12, -18, 6))
print("gcd(-4, -6, 2) =", gcd_three(-4, -6, 2))


2) Find all indexes of largest element in list

def largest_indexes(lst):
    largest = lst[0]
    for x in lst:
        if x > largest:
            largest = x
    indexes = []
    for i in range(len(lst)):
        if lst[i] == largest:
            indexes.append(i)
    return indexes

# Example
nums = [10, 40, 30, 40, 25, 40]
print("Indexes of largest element:", largest_indexes(nums))


3) Count characters, vowels, consonants, spaces, tabs, words
    

   def analyze_string(s):
    vowels = "aeiouAEIOU"
    num_chars = len(s)
    num_vowels = 0
    num_consonants = 0
    num_spaces = 0
    num_tabs = 0
    
    for ch in s:
        if ch in vowels:
            num_vowels += 1
        elif ch.isalpha():
            num_consonants += 1
        elif ch == " ":
            num_spaces += 1
        elif ch == "\t":
            num_tabs += 1

    num_words = len(s.split())  # split by space/tab

    return [num_chars, num_vowels, num_consonants, num_spaces, num_tabs, num_words]

# Example
s = "Sankar Dayal\tSarma"
result = analyze_string(s)
print("Characters:", result[0])
print("Vowels:", result[1])
print("Consonants:", result[2])
print("Spaces:", result[3])
print("Tabs:", result[4])
print("Words:", result[5])


4) Find largest and smallest from command line inputs (no predefined functions)

import sys

def find_min_max(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return largest, smallest

if __name__ == "__main__":
    # Command line input: py filename.py 10 20 5 15 30 3 25 40
    args = sys.argv[1:]  # skip filename
    nums = [int(x) for x in args]
    
    largest, smallest = find_min_max(nums)
    print("Largest element:", largest)
    print("Smallest element:", smallest)



5) Power function without using ** or predefined functions

    def power(a, b):
    if b == 0:
        return 1
    result = 1
    if b > 0:
        for _ in range(b):
            result *= a
    else:  # negative power
        for _ in range(-b):
            result *= a
        result = 1 / result
    return result

def power_three(a, b, c):
    return power(a, b * c)

# Examples
print("power(4.5, 3) =", power(4.5, 3))
print("power(4.5, -3) =", power(4.5, -3))
print("power(4.5, 0) =", power(4.5, 0))


6)Return index of 2nd largest element


def second_largest_index(lst):
    largest = second = float('-inf')
    for x in lst:
        if x > largest:
            second = largest
            largest = x
        elif x > second and x != largest:
            second = x
    
    if second == float('-inf'):
        return None  # no second largest
    for i in range(len(lst)):
        if lst[i] == second:
            return i

# Example
nums = [10, 20, 5, 15, 30]
print("Second largest index:", second_largest_index(nums))


7)Check if two strings are anagrams


def is_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            return False
    return True

# Example
print("Anagram test:", is_anagram("CINEMA", "ICEMAN"))


8) Count +ve, -ve, and zero values from command line

import sys

def count_numbers(numbers):
    pos = neg = zero = 0
    for num in numbers:
        if num > 0:
            pos += 1
        elif num < 0:
            neg += 1
        else:
            zero += 1
    return pos, neg, zero

if __name__ == "__main__":
    # Example run: py filename.py 25 -10 0 32 -20 0 -19
    args = sys.argv[1:]
    nums = [int(x) for x in args]
    pos, neg, zero = count_numbers(nums)
    print("Number of +ve values:", pos)
    print("Number of -ve values:", neg)
    print("Number of zeroes:", zero)

9)Largest element, row, and column in matrix


def largest_in_matrix(matrix):
    largest = matrix[0][0]
    row = col = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                row, col = i, j
    return [largest, row + 1, col + 1]  # 1-based indexing

# Example
matrix = [
    [10, 20, 15, 30],
    [40, 35, 50, 38]
]
result = largest_in_matrix(matrix)
print("Largest element:", result[0])
print("Row number:", result[1])
print("Column number:", result[2])


10) Print the given pattern (rows as input)
    Pattern example for n = 7:
ABCDEFGGFEDCBA
ABCDEF  FEDCBA
ABCDE    EDCBA
ABCD      DCBA
ABC        CBA
AB          BA
A            A


def print_pattern(n):
    for i in range(n, 0, -1):
        left = "".join(chr(65 + j) for j in range(i))   # ABC...
        right = left[::-1]                              # ...CBA
        spaces = " " * (2 * (n - i))                    # increasing spaces
        print(left + spaces + right)

# Example
print_pattern(7)



11) Convert decimal to binary without predefined function

We cannot use bin() or format methods. We’ll use division by 2.


def decimal_to_binary(num):
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary

# Example
print("Binary of 25:", decimal_to_binary(25))



12) Check if a matrix is symmetric

A matrix is symmetric if matrix[i][j] == matrix[j][i].

def is_symmetric(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    if rows != cols:
        return False  # not square matrix
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

# Example
matrix = [
    [10, 20, 30],
    [20, 40, 50],
    [30, 50, 60]
]

if is_symmetric(matrix):
    print("Symmetric matrix")
else:
    print("Not symmetric")




13) Pascal’s Triangle (using nCr formula)

Formula:  𝑛𝐶𝑟=𝑛!/𝑟!(𝑛−𝑟)!


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

def nCr(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

def pascals_triangle(n):
    for i in range(n):
        row = []
        for j in range(i+1):
            row.append(str(nCr(i, j)))
        print(" ".join(row))

# Example
pascals_triangle(5)



14)Convert binary to decimal (no predefined function)


def binary_to_decimal(binary_str):
    decimal = 0
    power = 0
    for digit in binary_str[::-1]:  # reverse string
        if digit == '1':
            decimal += 2 ** power
        power += 1
    return decimal

# Example
print("Binary 110101 =", binary_to_decimal("110101"))



15)Convert Decimal Number to Words


def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    if n == 0:
        return "Zero"
    elif n < 20:
        return ones[n]
    elif n < 100:
        return tens[n // 10] + ("" if n % 10 == 0 else " " + ones[n % 10])
    elif n < 1000:
        return ones[n // 100] + " Hundred" + ("" if n % 100 == 0 else " " + number_to_words(n % 100))
    elif n < 10000:
        return ones[n // 1000] + " Thousand" + ("" if n % 1000 == 0 else " " + number_to_words(n % 1000))

print(number_to_words(143))  # Output: One Hundred Forty Three



16)Roman to Decimal

def roman_to_decimal(s):
    roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    total = 0
    prev = 0
    for ch in reversed(s):
        if roman[ch] < prev:
            total -= roman[ch]
        else:
            total += roman[ch]
        prev = roman[ch]
    return total

print(roman_to_decimal("XIX"))  # Output: 19


17) Find Prime Numbers in Range


def primes_in_range(start, end):
    primes = []
    for num in range(start, end+1):
        if num > 1:
            for i in range(2, int(num**0.5)+1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(primes_in_range(10, 50))


18) Find Longest Word (no inbuilt string methods)

def longest_word(sentence):
    word = ""
    longest = ""
    for ch in sentence + " ":
        if ch != " ":
            word += ch
        else:
            if len(word) > len(longest):
                longest = word
            word = ""
    return longest

print(longest_word("Python is a powerful programming language"))

19) Fibonacci Series till n terms

def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a+b
    return series

print(fibonacci(10))

​
20) GCD of given numbers


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_list(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

print("GCD:", gcd_list([6, 12, 15]))


21)


    *    
   ***   
  *****  
 ******* 
*********
 ******* 
  *****  
   ***   
    *    


def diamond_pattern(n):
    # Upper pyramid
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    
    # Lower inverted pyramid
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

# Example usage:
diamond_pattern(5)

22) Print Each Digit of a Number in Words


def print_digits_in_words(number):
    """
    Prints each digit of a number in words.
    Example: 9247 -> Nine two four seven
    """
    digit_map = {
        '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
        '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
    }
    
    number_str = str(number)
    
    words = [digit_map[digit] for digit in number_str]
    
    print(' '.join(words).capitalize())

# Example usage:
print_digits_in_words(9247)



23) Transpose a Matrix


def transpose_matrix(matrix):
    """
    Transposes a given matrix.
    Example: [[1, 2], [3, 4]] -> [[1, 3], [2, 4]]
    """
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Create an empty matrix with swapped dimensions (cols x rows)
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
            
    return transposed

# Example usage:
input_matrix = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
]

output_matrix = transpose_matrix(input_matrix)

for row in output_matrix:
    print(row)



24)Rotate a String


def rotate_string(s):
    """
    Prints all rotations of a string.
    Example: 'SPACE' -> 'PACES', 'ACESP', 'CESPA', 'ESPAC', 'SPACE'
    """
    length = len(s)
    
    for i in range(length):
        rotated_string = s[i:] + s[:i]
        print(rotated_string)

# Example usage:
rotate_string('SPACE')



25). Print a Mathematical Table



def print_math_table(number):
    """
    Prints the multiplication table for a given number.
    Example: 7 -> 7*1=7, 7*2=14, ..., 7*10=70
    """
    for i in range(1, 11):
        product = number * i
        print(f"{number}*{i} = {product}")

# Example usage:
print_math_table(7)


26)abcde pyramid


def alphabet_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces before letters (2 spaces for alignment)
        print("  " * (n - i), end="")
        # Print letters with one space between
        for j in range(1, i + 1):
            print(chr(64 + j), end=" ")
        print()  # Move to next line

# Example usage
alphabet_pyramid(5)


27)Converting a Number to Roman Numerals


def int_to_roman(num):
    """
    Converts an integer to its Roman numeral representation.
    Example: 3878 -> MMMDCCCLXXVIII
    """
    roman_map = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C',
        90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V',
        4: 'IV', 1: 'I'
    }

    result = ""
    for value, symbol in roman_map.items():
        while num >= value:
            result += symbol
            num -= value
            
    return result

# Example usage:
input_num = 3878
roman_numeral = int_to_roman(input_num)
print(f"The Roman numeral for {input_num} is: {roman_numeral}")


28)Expression Evaluation Program


def evaluate_expression():
    """
    Evaluates a mathematical expression provided by the user.
    """
    try:
        # Prompt the user to enter an expression
        expression = input("Enter a mathematical expression (e.g., (3+4)*5-6/2): ")
        
        # Use eval() to safely evaluate the expression
        result = eval(expression)
        
        # Print the result
        print(f"Result: {result}")
        
    except Exception as e:
        # Handle potential errors, such as invalid syntax or division by zero
        print(f"Error: Invalid expression. {e}")

# Call the function to run the program
evaluate_expression()


29)Matchstick Game


def play_matchstick_game(total_matches=5):
    matches_remaining = total_matches
    
    while matches_remaining > 0:
        print(f"There are {matches_remaining} matchsticks left.")
        
        # User's turn
        user_pick = 0
        while not (1 <= user_pick <= 4 and user_pick <= matches_remaining):
            try:
                user_pick = int(input("How many matchsticks do you pick (1-4)? "))
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        matches_remaining -= user_pick
        print(f"You picked {user_pick} matchsticks. {matches_remaining} left.")
        if matches_remaining == 0:
            print("You picked the last matchstick. Computer wins!")
            return
        
        # Computer's turn
        computer_pick = 5 - user_pick
        if computer_pick > matches_remaining:
            computer_pick = matches_remaining
        
        matches_remaining -= computer_pick
        print(f"Computer picks {computer_pick} matchsticks. {matches_remaining} left.")
        if matches_remaining == 0:
            print("Computer picked the last matchstick. Computer wins!")
            return

# Play the game with the given total
play_matchstick_game(5)


30)Roman Numeral to Regular Number



def roman_to_int(s):
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    
    result = 0
    i = 0
    while i < len(s):
        # Check for two-character combinations (e.g., IV, IX)
        if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i+1]]:
            result += roman_map[s[i+1]] - roman_map[s[i]]
            i += 2
        else:
            result += roman_map[s[i]]
            i += 1
            
    return result

# Example usage
roman_numeral = "MMMDCCCLXXVIII"
integer_value = roman_to_int(roman_numeral)
print(f"The integer for {roman_numeral} is: {integer_value}")



31) Print Number in Words


def num_to_words(num):
    # This is a complex problem, here is a simplified solution for a smaller range
    # A full solution requires handling places (thousands, lakhs, crores, etc.)
    
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    
    def convert_hundreds(n):
        if n == 0:
            return ""
        
        hundreds = n // 100
        n %= 100
        
        word = ""
        if hundreds > 0:
            word += units[hundreds] + " hundred "
            
        if 10 < n < 20:
            word += teens[n - 10]
        else:
            word += tens[n // 10] + " "
            word += units[n % 10]
        
        return word.strip()

    # The full solution would use a recursive approach or a loop over chunks of 3 digits
    
    # For a number like 123456789
    parts = []
    
    if num == 0:
        return "zero"
        
    num_str = str(num).zfill(12)  # Pad with zeros to handle crores, lakhs etc.
    crores = int(num_str[-12:-9])
    lakhs = int(num_str[-9:-6])
    thousands = int(num_str[-6:-3])
    hundreds = int(num_str[-3:])

    result = ""
    if crores > 0:
        result += convert_hundreds(crores) + " crore "
    if lakhs > 0:
        result += convert_hundreds(lakhs) + " lakh "
    if thousands > 0:
        result += convert_hundreds(thousands) + " thousand "
    if hundreds > 0:
        result += convert_hundreds(hundreds)
        
    return result.strip()
    
# Example usage
number = 123456789
words = num_to_words(number)
print(f"Output: {words}")



32)Multiply Two Matrices


def multiply_matrices(matrix_a, matrix_b):
    # Get dimensions
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    # Check if multiplication is possible
    if cols_a != rows_b:
        return "Error: Number of columns in the first matrix must equal the number of rows in the second matrix."

    # Create the result matrix with the correct dimensions
    result_matrix = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    # Perform matrix multiplication
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result_matrix

# Example usage based on the image's "Matrix a"
matrix_a = [
    [1, 2, 3]
]
# We need a second matrix with 3 rows to multiply
matrix_b = [
    [4, 5],
    [6, 7],
    [8, 9]
]

result = multiply_matrices(matrix_a, matrix_b)

if isinstance(result, list):
    for row in result:
        print(row)
else:
    print(result)




33) Armstrong


def is_armstrong(num):
    # Convert to string to count digits
    digits = str(num)
    power = len(digits)
    
    total = 0
    for d in digits:
        total += int(d) ** power
    
    return total == num


# Example usage
n = int(input("Enter a number: "))
if is_armstrong(n):
    print(n, "is an Armstrong number")
else:
    print(n, "is not an Armstrong number")




34)pyramid


    1
   123
  12345
 1234567
123456789



def number_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        print(" " * (n - i), end="")
        # Print numbers 1,2,3,...(2*i-1)
        for j in range(1, 2 * i):
            print(j, end="")
        print()  # New line

# Example usage
number_pyramid(5)


35) palindrome

def is_palindrome(s):
    # Manually reverse the string
    rev = ""
    for ch in s:
        rev = ch + rev   # build reversed string
    
    # Compare original and reversed
    return s == rev


# Example usage
text = input("Enter a string: ")
if is_palindrome(text):
    print(text, "is a palindrome")
else:
    print(text, "is not a palindrome")



36)Write a function to generate the permutations for a given list of numbers.

Example Input:
[1, 2, 3]

Example Output:
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)



import itertools

def generate_permutations(lst):
    return list(itertools.permutations(lst))

# Example
print(generate_permutations([1, 2, 3]))



37)Write function to return the first string which is repeated max number of times.

Example Input:
"Hyd is green city. Hyd is hitec city. Hyd is beautiful city."

Output:
Hyd

 Python Solution:

def most_repeated_word(sentence):
    words = sentence.replace(".", "").split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    # Find max frequency word
    max_word = max(freq, key=freq.get)
    return max_word

# Example
print(most_repeated_word("Hyd is green city. Hyd is hitec city. Hyd is beautiful city."))



38)Write a function to test a matrix is unit matrix or not.

Unit Matrix (Identity Matrix): Diagonal elements are 1 and all other elements are 0.

Example Input:

1 0 0
0 1 0
0 0 1



def is_unit_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == j and matrix[i][j] != 1:
                return False
            elif i != j and matrix[i][j] != 0:
                return False
    return True

# Example
print(is_unit_matrix([[1,0,0],[0,1,0],[0,0,1]]))  # True
print(is_unit_matrix([[1,0,0],[0,0,0],[0,0,1]]))  # False



39)Write a recursive function to count number of occurrences of a value in a list.

def count_occurrences(lst, x):
    if not lst:  # Base case: empty list
        return 0
    return (1 if lst[0] == x else 0) + count_occurrences(lst[1:], x)

# Example
print(count_occurrences([10,20,15,18,20], 20))  # 2
print(count_occurrences([10,20,15,18,20], 25))  # 0


40)Write a Python program to generate all sublists of a list.

Example Input: [X, Y, Z]
Output:[], [X], [Y], [Z], [X,Y], [X,Z], [Y,Z], [X,Y,Z]


from itertools import combinations

def all_sublists(lst):
    result = []
    for r in range(len(lst)+1):
        for combo in combinations(lst, r):
            result.append(list(combo))
    return result

# Example
print(all_sublists(['X','Y','Z']))


41)Write a Python program to print the following number pattern for n rows.

For n = 5:

1
212
32123
4321234
543212345

def number_pattern(n):
    for i in range(1, n+1):
        # descending part
        for j in range(i, 0, -1):
            print(j, end="")
        # ascending part
        for j in range(2, i+1):
            print(j, end="")
        print()

# Example
number_pattern(5)

42.)Write a function to print frequency of each alphabet in a string in alphabetical order ignoring the case.

Example Input: "RaMa Rao"
Output:
A..3, M..1, O..1, R..2


def char_frequency(s):
    s = s.replace(" ", "").lower()
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in sorted(freq):
        print(f"{ch.upper()}..{freq[ch]}", end=", ")

# Example
char_frequency("RaMa Rao")





43.) Next Bigger Number from Digits


def next_bigger_number(n):
    digits = list(str(n))
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    if i == -1:
        return n
    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1
    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    return int("".join(digits))

print(next_bigger_number(21))   # 12
print(next_bigger_number(445))  # 454



44). First Character Repeated Max Times


def max_repeated_char(s):
    s = s.upper()
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return max(freq, key=freq.get)

print(max_repeated_char("RAMA RAO"))  # A


45).Sort Each Row in Matrix


def sort_matrix(matrix):
    return [sorted(row) for row in matrix]

matrix = [[10,20,15,5,30,40],[35,25,100,200,150,50]]
print(sort_matrix(matrix))



46). Recursive Sum of List

def recursive_sum(lst):
    if not lst:
        return 0
    return lst[0] + recursive_sum(lst[1:])

print(recursive_sum([10,20,30,40]))  # 100



47). Count Strings with Same Start and End


def count_special_strings(strings):
    count = 0
    for s in strings:
        if len(s) >= 2 and s[0] == s[-1]:
            count += 1
    return count

sample = ['abc', 'xyz', 'aba', '1221']
print(count_special_strings(sample))  # 2



48). Odd Numbers Pattern

def odd_pattern(n):
    num = 1
    for i in range(n):
        row = []
        for j in range(n):
            row.append(str(num))
            num += 2
        print(" ".join(row))

odd_pattern(4)

Output for n=4:

1 3 5 7
9 11 13 15
17 19 21 23
25 27 29 31



49).Frequency of Vowels


def vowel_frequency(s):
    vowels = "aeiou"
    freq = {v:0 for v in vowels}
    for ch in s.lower():
        if ch in freq:
            freq[ch] += 1
    for v in sorted(freq):
        if freq[v] > 0:
            print(f"{v.upper()}...{freq[v]}")

vowel_frequency("RaMaRAo")
# A...3, O...1





