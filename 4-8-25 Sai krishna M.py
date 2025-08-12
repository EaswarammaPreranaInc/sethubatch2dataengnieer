'''
1)convert decimals to words
'''

def number_to_words(n):
    u = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    t = ["", "", "twenty", "thirty", "forty", "fifty",
         "sixty", "seventy", "eighty", "ninety"]
    teen = ["ten", "eleven", "twelve", "thirteen", "fourteen",
            "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    if n == 0:
        return "zero"

    words = []

    if n >= 1000:
        words.append(u[n // 1000] + " thousand")
        n %= 1000

    if n >= 100:
        words.append(u[n // 100] + " hundred")
        n %= 100
        if n > 0:
            words.append("and")

    if 10 <= n <= 19:
        words.append(teen[n - 10])
    else:
        if n >= 20:
            words.append(t[n // 10])
            n %= 10
        if n > 0:
            words.append(u[n])

    return " ".join(words)

# --- Main ---
if __name__ == "__main__":
    num = int(input("Enter an input: "))
    if 0 <= num <= 9999:
        print("Output:", number_to_words(num))
    else:
        print("Only numbers between 0 and 9999 are supported.")

'''
2)Convert Roman numbers to Decimals

def roman_to_decimal(roman):
    roman_values = {
        'I': 1,    'V': 5,    'X': 10,   'L': 50,
        'C': 100,  'D': 500,  'M': 1000
    }

    total = 0
    prev = 0

    for char in reversed(roman.upper()):
        value = roman_values[char]
        if value < prev:
            total -= value
        else:
            total += value
            prev = value

    return total

# --- Main ---
if __name__ == "__main__":
    roman_input = input("Enter a Roman numeral: ")
    try:
        decimal_value = roman_to_decimal(roman_input)
        print("Decimal value:", decimal_value)
    except KeyError:
        print("Invalid Roman numeral!")
'''
'''
3)prime numbers in a given range 


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_range(start, end):
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=' ')

# --- Main ---
if __name__ == "__main__":
    start = int(input("Enter start of range: "))
    end = int(input("Enter end of range: "))
    print(f"Prime numbers between {start} and {end}:")
    prime_range(start, end)
'''
'''
4)longest word in a sentence

sentence = input("Enter a sentence: ")

longest_word = ""
current_word = ""
max_length = 0
current_length = 0

for ch in sentence + " ":  # Add a space to process the last word
    if ch != ' ':
        current_word += ch
        current_length += 1
    else:
        if current_length > max_length:
            max_length = current_length
            longest_word = current_word
        current_word = ""
        current_length = 0

print("Longest word:", longest_word)
print("Length:", max_length)
'''
'''
5)Generate Fibnacci series till nth number 

n = int(input("Enter number of terms: "))

a = 0
b = 1
count = 0

print("Fibonacci Series:")
while count < n:
    print(a, end=' ')
    next_term = a + b
    a = b
    b = next_term
    count += 1
'''
'''
6)GCD of given numbers 

def find_gcd(a, b):
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def gcd_of_list(numbers):
    result = numbers[0]
    for i in range(1, len(numbers)):
        result = find_gcd(result, numbers[i])
    return result

# --- Main ---
nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
if len(nums) < 2:
    print("Enter at least two numbers.")
else:
    result = gcd_of_list(nums)
    print("GCD of", nums, "is:", result)
'''
'''
7)star program 


pattern = [1, 2, 4, 6, 4, 2, 1]
max_stars = max(pattern)

for i in range(len(pattern)):
    # Print leading spaces to center the stars
    spaces = (max_stars - pattern[i]) // 2
    print("  " * spaces, end="")  # 2 spaces per space unit

    # Print stars
    for j in range(pattern[i]):
        print("*", end=" ")
    print()
'''