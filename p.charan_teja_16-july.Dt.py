
1. Integer Conversion (int())
Python

print(int(10.8))
# Output: 10
# Explanation: Converts the float 10.8 to an integer by truncating the decimal part.

print(int(True))
# Output: 1
# Explanation: Converts the boolean True to its integer equivalent, which is 1.

print(int(False))
# Output: 0
# Explanation: Converts the boolean False to its integer equivalent, which is 0.

print(int('25'))
# Output: 25
# Explanation: Converts the string '25' into an integer 25.

print(int('0075'))
# Output: 75
# Explanation: Converts the string '0075' into an integer 75. Leading zeros are ignored.

print(int(0b11010))
# Output: 26
# Explanation: Converts the binary literal 0b11010 (which is 1*16 + 1*8 + 0*4 + 1*2 + 0*1 = 26) to an integer.

print(0b11010)
# Output: 26
# Explanation: This directly prints the integer value of the binary literal 0b11010.

print(int(0o6247))
# Output: 3239
# Explanation: Converts the octal literal 0o6247 (which is 6*512 + 2*64 + 4*8 + 7*1 = 3072 + 128 + 32 + 7 = 3239) to an integer.

print(0o6247)
# Output: 3239
# Explanation: This directly prints the integer value of the octal literal 0o6247.

print(int(0xA789))
# Output: 42889
# Explanation: Converts the hexadecimal literal 0xA789 (which is 10*4096 + 7*256 + 8*16 + 9*1 = 40960 + 1792 + 128 + 9 = 42889) to an integer. (A=10, B=11)

print(0xA789)
# Output: 42889
# Explanation: This directly prints the integer value of the hexadecimal literal 0xA789.

print(int(3 + 4j))
# Output: TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
# Explanation: The 'int()' function cannot convert complex numbers directly to integers. It expects real numbers (like floats or integers) or strings that represent integers.

print(int('25.4'))
# Output: ValueError: invalid literal for int() with base 10: '25.4'
# Explanation: The 'int()' function can only convert strings that represent whole numbers.

print(int('Ten'))
# Output: ValueError: invalid literal for int() with base 10: 'Ten'
# Explanation: The 'int()' function cannot convert strings that contain non-numeric characters.
<br><br><br><br><br>

2. Float Conversion (float())
Python

print(float(25))
# Output: 25.0
# Explanation: Converts the integer 25 to a float 25.0.

print(float(True))
# Output: 1.0
# Explanation: Converts the boolean True to its float equivalent, which is 1.0.

print(float(False))
# Output: 0.0
# Explanation: Converts the boolean False to its float equivalent, which is 0.0.

print(float('92'))
# Output: 92.0
# Explanation: Converts the string '92' (representing an integer) to a float 92.0.

print(float('36.4'))
# Output: 36.4
# Explanation: Converts the string '36.4' (representing a float) to a float 36.4.

print(float('0075'))
# Output: 75.0
# Explanation: Converts the string '0075' (representing an integer with leading zeros) to a float 75.0. leading zeros are ignored.

print(float(0b1010101))
# Output: 85.0
# Explanation: Converts the binary literal 0b1010101 (which is 1*64 + 0*32 + 1*16 + 0*8 + 1*4 + 0*2 + 1*1 = 64 + 16 + 4 + 1 = 85) to a float 85.0.

print(float(0o6247))
# Output: 3239.0
# Explanation: Converts the octal literal 0o6247 (which is 6*512 + 2*64 + 4*8 + 7*1 = 3072 + 128 + 32 + 7 = 3239) to a float 3239.0.

print(float(0xA789))
# Output: 42889.0
# Explanation: Converts the hexadecimal literal 0xA789 (which is 10*4096 + 7*256 + 8*16 + 9*1 = 40960 + 1792 + 128 + 9 = 42889) to a float 42889.0.

print(float(3 + 4j))
# Output: TypeError: float() argument must be a string or a real number, not 'complex'
# Explanation: The 'float()' function cannot convert complex numbers directly to floats. It expects real numbers (like integers or other floats) or strings that represent real numbers.

print(float('Ten'))
# Output: ValueError: could not convert string to float: 'Ten'
# Explanation: The 'float()' function cannot convert strings that contain non-numeric characters (unless they are valid numeric literals). 'Ten' is not a valid floating-point literal.
<br><br><br><br><br>

3. Complex Conversion (complex())
Python

print(complex(3, 4))
# Output: (3+4j)
# Explanation: Creates a complex number where the real part is 3 and the imaginary part is 4.

print(complex(0, 4))
# Output: 4j
# Explanation: Creates a complex number where the real part is 0 and the imaginary part is 4. Python omits the '0+' when the real part is zero.

print(complex(3))
# Output: (3+0j)
# Explanation: Creates a complex number where the real part is 3 and the imaginary part defaults to 0.

print(complex(3.0, 4.0))
# Output: (3+4j)
# Explanation: Creates a complex number where the real part is 3.0 and the imaginary part is 4.0 (Both floats are retained).

print(complex(3.0))
# Output: (3+0j)
# Explanation: Creates a complex number where the real part is 3.0 and the imaginary part defaults to 0.

print(complex(3, 4.5))
# Output: (3+4.5j)
# Explanation: Creates a complex number where the real part is 3 and the imaginary part is 4.5.

print(complex(True, False))
# Output: (1+0j)
# Explanation: Booleans are treated as their integer equivalents (True=1, False=0). So, it's complex(1, 0).

print(complex(True))
# Output: (1+0j)
# Explanation: True is treated as 1, and the imaginary part defaults to 0.

print(complex(False))
# Output: 0j
# Explanation: False is treated as 0, and the imaginary part defaults to 0. Python omits '+0j' as just '0j'.

print(complex(True, 4))
# Output: (1+4j)
# Explanation: True is treated as 1 for the real part, and 4 is used for the imaginary part.

print(complex('3'))
# Output: (3+0j)
# Explanation: Parses the string '3' as the real part. The imaginary part defaults to 0.

print(complex('3.0'))
# Output: (3+0j)
# Explanation: Parses the string '3.0' as the real part (a float). The imaginary part defaults to 0.

print(complex('3', '4'))
# Output: TypeError: complex() second argument must be a number, not a str
# Explanation: When two arguments are provided to complex(), both must be numbers (int, float, bool). A string cannot be directly used as the imaginary part in this form.

print(complex('3j', 4))
# Output: TypeError: complex() can't take second arg if first is a string
# Explanation: If the first argument to complex() is a string, it is expected to be the *entire* complex number in string form (e.g., "3+4j"), you cannot provide a separate second argument (imaginary part) if the first argument is a string.

print(complex('3j', '4j'))
# Output: TypeError: complex() can't take second arg if first is a string
# Explanation: Similar to the previous case, if the first argument is a string, a second string argument is not allowed.

print(complex('Ten'))
# Output: ValueError: complex() arg is a malformed string
# Explanation: The string 'Ten' cannot be parsed as a valid complex number. It must be in a numeric format (e.g., "5", "3.14", "2+5j").
<br><br><br><br><br>

4. Boolean Conversion (bool())
Python

print(bool(0))
# Output: False
# Explanation: The integer 0 is considered falsy.

print(bool(10))
# Output: True
# Explanation: The integer 10 is a non-zero number, hence considered truthy.

print(bool(-25))
# Output: True
# Explanation: The integer -25 is a non-zero number, hence considered truthy.

print(bool(0.0))
# Output: False
# Explanation: The float 0.0 is considered falsy.

print(bool(0.1))
# Output: True
# Explanation: The float 0.1 is a non-zero number, hence considered truthy.

print(bool(0 + 0j))
# Output: False
# Explanation: A complex number where both the real and imaginary parts are zero is considered falsy.

print(bool(10 + 20j))
# Output: True
# Explanation: A complex number is considered truthy if either its real part or its imaginary part (or both) are non-zero. Here, both are non-zero.

print(bool(-15j))
# Output: True
# Explanation: A complex number with a non-zero imaginary part (-15) is considered truthy, even if the real part is implicitly zero.

print(bool('False'))
# Output: True
# Explanation: This is a non-empty string. Any non-empty string, regardless of its content, is considered truthy.

print(bool(''))
# Output: False
# Explanation: An empty string is considered falsy.

print(bool('Hyd'))
# Output: True
# Explanation: This is a non-empty string, hence considered truthy.

print(bool(' '))
# Output: True
# Explanation: This is a non-empty string (it contains a space character), hence considered truthy.

print(bool('True'))
# Output: True
# Explanation: This is a non-empty string, hence considered truthy.
<br><br><br><br><br>

5. String Conversion (str())
Python

print(str(25))
# Output: '25'
# Explanation: Converts the integer 25 into its string representation '25'.

print(str(10.8))
# Output: '10.8'
# Explanation: Converts the float 10.8 into its string representation '10.8'.

print(str(3 + 4j))
# Output: '(3+4j)'
# Explanation: Converts the complex number 3+4j into its string representation '(3+4j)'. Note the parentheses around the complex number.

print(str(True))
# Output: 'True'
# Explanation: Converts the boolean True into its string representation 'True'.

print(str(False))
# Output: 'False'
# Explanation: Converts the boolean False into its string representation 'False'.

print(str(None))
# Output: 'None'
# Explanation: Converts the special None object into its string representation 'None'.
<br><br><br><br><br>

6. Hexadecimal Conversion (hex())
Python

print(hex(25))
# Output: 0x19
# Explanation: Converts the decimal integer 25 to its hexadecimal representation.
# Reading remainders from bottom to top: 19.

print(hex(0b1010111010111))
# Output: 0x2b7
# Explanation: First, 0b1010111010111 is a binary literal. Python converts this binary number to an integer internally, then 'hex()' converts that integer to its hexadecimal string representation.
# Binary to Decimal: 1*8192 + 0*4096 + 1*2048 + 0*1024 + 1*512 + 1*256 + 1*128 + 1*64 + 0*32 + 1*16 + 0*8 + 1*4 + 1*2 + 1*1
# = 8192 + 2048 + 512 + 256 + 128 + 64 + 16 + 4 + 2 + 1 = 11223
# Reading remainders from bottom to top: 2B07.
# The calculation in the image seems to have a typo or error. The correct hexadecimal representation of the binary number is 0x15D7.
# Let's re-examine the image output. The image shows the hex for `0b1010111010111` as `0x2b7`. Let's re-calculate.
# 0b10 1011 1010 111 -> 2 B A 7. Wait, the image shows a different binary literal: 0b1010111010111. Let's convert this:
# 0b1010111010111 = 1 * 4096 + 0 * 2048 + 1 * 1024 + 0 * 512 + 1 * 256 + 1 * 128 + 1 * 64 + 0 * 32 + 1 * 16 + 0 * 8 + 1 * 4 + 1 * 2 + 1 * 1 = 4096 + 1024 + 256 + 128 + 64 + 16 + 4 + 2 + 1 = 5591.
# 5591 in hex is `0x15d7`. The image's output `0x2b7` is incorrect for the binary number shown. The image's text seems to have transcription errors. The correct transcription of the image shows: `0b1010111010111`, not a 13-bit number, but it's not a standard byte-aligned value. Let's assume there's a typo in the provided code snippet itself. The explanation provided in the image is also incorrect.
# I will transcribe the image content as it is, including the error.

print(hex(0o6247))
# Output: 0xca7
# Explanation: First, 0o6247 is an octal literal. Python converts this octal number to an integer internally, then 'hex()' converts that integer to its hexadecimal string representation.
# Octal to Decimal: 6*512 + 2*64 + 4*8 + 7*1 = 3072 + 128 + 32 + 7 = 3239.
# Reading remainders from bottom to top: CA7.
<br><br><br><br><br>

7. Octal Conversion (oct())
Python

print(oct(195))
# Output: 0o303
# Explanation: Converts the decimal integer 195 to its octal representation.
# Reading remainders from bottom to top: 303.

print(oct(0b10101110010))
# Output: 0o2562
# Explanation: First, 0b10101110010 is a binary literal. Python converts this binary number to an integer internally, then 'oct()' converts that integer to its octal string representation.
# Binary to Decimal: 1*1024 + 0*512 + 1*256 + 0*128 + 1*64 + 1*32 + 1*16 + 0*8 + 0*4 + 1*2 + 0*1 = 1024 + 256 + 64 + 32 + 16 + 2 = 1394
# Reading remainders from bottom to top: 2562.

print(oct(0xA789))
# Output: 0o123611
# Explanation: First, 0xA789 is a hexadecimal literal. Python converts this hexadecimal number to an integer internally, then 'oct()' converts that integer to its octal string representation.
# Hexadecimal to Decimal: A=10, B=11
# 10*4096 + 7*256 + 8*16 + 9*1 = 40960 + 1792 + 128 + 9 = 42889
# Reading remainders from bottom to top: 123611.
<br><br><br><br><br>

8. String Assignment and Immutability
Python

a = "Rama Rao"
print(a)
# Output: Rama Rao
print(type(a))
# Output: <class 'str'>
print(id(a))
# Output: [A unique memory address, e.g., 140700346337456]
b = 'Hyd'
print(b)
# Output: Hyd
c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)
# Output:
# Hyd is green city.
# Hyd is hitec city.
# Hyd is beautiful city.

a = 'Hyd'
print(a, id(a))
# Output: Hyd 1407xxxxxxxxxx (where 1407xxxxxxxxxx is a memory address)
# Explanation: 'a' is assigned the string 'Hyd'. This line prints the string value and its unique memory address.
a = a * 3
print(a, id(a))
# Output: HydHydHyd 2049xxxxxxxxxx (where 2049xxxxxxxxxx is a *different* memory address)
# Explanation: The expression 'a * 3' creates a *new* string object 'HydHydHyd'.
# Because strings are immutable in Python, the original 'Hyd' object is not modified.
# The variable 'a' is then reassigned to point to this new 'HydHydHyd' string object.
<br><br><br><br><br>

9. String Repetition (* operator)
Python

a = 'Hyd'
print(a * 3)
# Output: HydHydHyd
# Explanation: The string 'a' is repeated 3 times.
print(a * 2)
# Output: HydHyd
# Explanation: The string 'a' is repeated 2 times.
print(a * 1)
# Output: Hyd
# Explanation: The string 'a' is repeated 1 time.
print(a * 0)
# Output:
# Explanation: The string 'a' is repeated 0 times, resulting in an empty string.
print(a * -1)
# Output:
# Explanation: The string 'a' is repeated -1 times, which also results in an empty string. Python treats negative repetitions the same as zero repetitions for strings.
print(25 * 3)
# Output: 75
# Explanation: Standard multiplication of two integers.
print('25' * 3)
# Output: 252525
# Explanation: The string '25' is repeated 3 times.
print('25' * 4.0)
# Output: TypeError: can't multiply sequence by non-int of type 'float'
# Explanation: String multiplication (repetition) only works with an integer. You cannot multiply a string by a float.
print(3 * 'Hyd')
# Output: HydHydHyd
# Explanation: The string 'Hyd' is repeated 3 times. The order of the string and integer in multiplication doesn't matter.
print('25' * True)
# Output: 25
# Explanation: In Python, True is treated as 1 in numerical contexts. So, '25' is repeated 1 time.
<br><br><br><br><br>

10. String Indexing and Slicing
Python

a = 'Hyd'
print(a[0])
# Output: H
# Explanation: Accesses the character at index 0 (the first character) of the string 'a'.
print(a[1])
# Output: y
# Explanation: Accesses the character at index 1 (the second character) of the string 'a'.
print(a[2])
# Output: d
# Explanation: Accesses the character at index 2 (the third character) of the string 'a'.
print(a[3])
# Output: IndexError: string index out of range
# Explanation: The string 'Hyd' only has indices 0, 1, and 2. Index 3 is out of bounds.
print(a[-1])
# Output: d
# Explanation: Accesses the character at the last position using negative indexing.
print(a[-2])
# Output: y
# Explanation: Accesses the character at the second to last position using negative indexing.
print(a[-3])
# Output: H
# Explanation: Accesses the character at the third to last position (which is the first character) using negative indexing.
print(a[-4])
# Output: IndexError: string index out of range
# Explanation: The string 'Hyd' only has negative indices -1, -2, and -3. Index -4 is out of bounds.
print(a[0] == a[-3])
# Output: True
# Explanation: Both a[0] and a[-3] refer to the character 'H', so the comparison is true.
# a[2] = 'c'
# Output: TypeError: 'str' object does not support item assignment
# Explanation: Strings in Python are immutable, meaning you cannot change individual characters after the string is created.
print(25[0])
# Output: TypeError: 'int' object is not subscriptable
# Explanation: Integers are not sequences and do not support indexing.
print('25'[0])
# Output: 2
# Explanation: '25' is a string, and [0] correctly accesses its first character.
print(True[1])
# Output: TypeError: 'bool' object is not subscriptable
# Explanation: Boolean values are not sequences and do not support indexing.
print('True'[1])
# Output: r
# Explanation: 'True' is a string, and [1] correctly accesses its second character.

a = 'Sankar Dayal Sarma'
print(a[7:12])
# Output: Dayal
# Explanation: Slices from index 7 (inclusive 'D') up to, but not including, index 12 ('l'). So, 'Dayal'.
print(a[7:])
# Output: Dayal Sarma
# Explanation: Slices from index 7 (inclusive 'D') to the end of the string.
print(a[:6])
# Output: Sankar
# Explanation: Slices from the beginning of the string (index 0) up to, but not including, index 6 (the space).
print(a[:])
# Output: Sankar Dayal Sarma
# Explanation: Slices from the beginning to the end, with a step of 1 (default). This creates a full copy of the string. Equivalent to a[0:18:1].
print(a[::2])
# Output: SakrDya Sm
# Explanation: Slices from index 0(S), taking every 2nd character.
# Indices: 0(S), 2(k), 4(a), 6(r), 8(D), 10(y), 12( ), 14(a), 16(r) -> 'SakrDya Sm'.
print(a[1::2])
# Output: anr aa ar
# Explanation: Slices from index 1 to the end, taking every 2nd character.
# Indices: 1(a), 3(n), 5(r), 7( ), 9(a), 11(a), 13( ), 15(r), 17(a) -> 'anr aa ar'.
print(a[-5:-1])
# Output: Sarm
# Explanation: Slices from index -5 (inclusive 'S') up to, but not including, index -1 ('a').
print(a[::-1])
# Output: amraS layaD raknaS
# Explanation: Slices the entire string in reverse order (step of -1).
print(a[::-2])
# Output: amSya kS
# Explanation: Slices from index -1 (inclusive 'a') down to, but not including, index -5 ('S'), with a step of -1.
# Characters are a(-1), m(-3), r(-5), a(-7), S(-9), y(-11), a(-13), D(-15), k(-17), S(-18) -> 'amSya kS'
print(a[-1:-5:-1])
# Output: amraS
# Explanation: Slices the entire string in reverse order, taking every second character.
# Slices from index -1 down to, but not including, index -5, with a step of -1.
# Characters included: a(-1), m(-2), r(-3), a(-4), S(-5) -> 'amraS'.
print(a[-2:5])
# Output:
# Explanation: An empty string is returned. When slicing with a positive step (default 1), if the start index is greater than or equal to the stop index, an empty string is returned. Here, -2 is effectively "after" -5 when moving forward, so it results in an empty slice.
print(a[3:-3])
# Output: kar Dayal Sar
# Explanation: Slices from index 3 (inclusive 'k') up to, but not including, index -3 ('r').
print(a[-2:-5])
# Output: (empty string)
# Explanation: The start index -2 is to the right of the stop index -5, and the step is positive (default). When slicing with a positive step, if the start index is greater than or equal to the stop index, an empty string is returned.
print(a[3: -3:-1])
# Output: (empty string)
# Explanation: When the start index is equal to the stop index, an empty string is returned because the slice range is exclusive of the stop index.
print(a[3: -2])
# Output: kar Dayal Sar
# Explanation: Slices from index 3 (inclusive 'k') up to, but not including, index -2 ('a').
<br><br><br><br><br>

11. String Length (len())
Python

print(len('Hyd'))
# Output: 3
# Explanation: The 'len()' function returns the number of characters in the string 'Hyd', which is 3.

print(len('Rama Rao'))
# Output: 8
# Explanation: The 'len()' function returns the number of characters in the string 'Rama Rao'. Spaces are counted as characters.

print(len('9247'))
# Output: 4
# Explanation: The 'len()' function returns the number of characters in the string '9247'.

print(len(''))
# Output: 0
# Explanation: The 'len()' function returns the number of characters in an empty string, which is 0.

print(len(' '))
# Output: 1
# Explanation: The 'len()' function returns the number of characters in the string containing a single space, which is 1.

print(len(689))
# Output: TypeError: object of type 'int' has no len()
# Explanation: The 'len()' function is designed to work with sequences (like strings, lists, tuples, etc.) to return their length. It cannot be used directly on an integer (689) as integers do not have a concept of length.
<br><br><br><br><br>

12. String Literals and Syntax Errors
Python

a = """ "Hyd" """
print(a)
# Output:  "Hyd"
# Explanation: This statement assigns the string """ "Hyd" """ to 'a'.
print(len(a))
# Output: 7
# Explanation: The string 'a' has a length of 7 characters (including the space and the quotes).
print(a[0])
# Output:
# Explanation: a[0] is the first character, which is a space.
print("""Hyd""")
# Output: Hyd
# Explanation: This is a valid multi-line string literal defined by triple double quotes """""". It prints the string 'Hyd'.
b = """ "" "Hyd" """""
# Output: SyntaxError: invalid syntax
# Explanation: The sequence of five double quotes """"" at the beginning is not a valid string literal definition in Python, resulting in a SyntaxError. Variable 'b' would not be assigned.
print(b)
# Output: (This line would not be reached due to the SyntaxError above)
# Explanation: If the previous line had been valid, this would print the value of 'b'.
print(len(b))
# Output: (This line would not be reached due to the SyntaxError above)
# Explanation: If 'b' were a valid string, this would print its length.
