a = 10.8
print(a)  # 10.8
print(type(a))  # <class 'float'>
print(id(a))  # memory address of 10.8
b = 25.
print(b)  # 25.0
print(type(b))  # <class 'float'>
c = .689
print(c)  # 0.689
d = 3.4E2
print(d)  # 340.0
print(type(d))  # <class 'float'>
e = 9.62e-2
print(e)  # 0.0962
print(9.8.2)  # error: two dots not allowed in a number

a = 3 + 4j
print(a)  # (3+4j)
print(type(a))  # <class 'complex'>
print(id(a))  # memory address of (3+4j)
print(a.real)  # 3.0
print(a.imag)  # 4.0
print(type(a.real))  # <class 'float'>
print(type(a.imag))  # <class 'float'>

a = 6j
print(a)  # 6j
print(type(a))  # <class 'complex'>
print(a.real)  # 0.0
print(a.imag)  # 6.0
print(5 + j6)  # error: 'j' must come after number, not before
print(3 + 4i)  # error: use 'j' not 'i' for imaginary numbers
print(4 + j)  # error: no number before 'j'
print(4 + 1j)  # (4+1j)
print(4 + 0j)  # (4+0j)

a = True
print(a)  # True
print(type(a))  # <class 'bool'>
print(id(a))  # memory address of True
b = False
print(b)  # False
print(type(b))  # <class 'bool'>
print(True + True)  # 2
print(True + False)  # 1
print(False + True)  # 1
print(False + False)  # 0
print(True + True + True)  # 3
print(25 + 10.8 + True)  # 36.8
print(True > False)  # True
print(True)  # True
print(False)  # False
print(true)  # error: 'true' must start with capital T → True
print(false)  # error: 'false' must start with capital F → False

a = 0O6247
print(a)  # 3239  (6×512 + 2×64 + 4×8 + 7 = 3072 + 128 + 32 + 7)
print(type(a))  # <class 'int'>
print(id(a))  # memory address of 3239
b = 0o6247
print(id(b))  # value of 0o6247 = 3239, id same as id(a)
print(b)  # 3239
c = 3239
print(c)  # 3239
print(id(c))  # same as id(a) and id(b)
print(0o9248)  # error: 9 and 8 are not valid digits in octal (only 0–7 allowed)

a = 0XA7B9
print(a)  # 42937  (A=10, 7, B=11, 9 → 10×16^3 + 7×16^2 + 11×16 + 9)
print(type(a))  # <class 'int'>
b = 0xBEEF
print(b)  # 48879  (11×16^3 + 14×16^2 + 14×16 + 15)
print(A7B9)  # error: A7B9 not defined as variable or number
print('A7B9')  # A7B9. it is treated as string
print(0XBEER)  # error: 'R' not allowed in hex (only 0–9, A–F)
print(0XHYD)  # error: 'H' and 'Y' not allowed in hex
print(0xA7G9B)  # error: 'G' not allowed in hex

a = 9248
print(a)  # 9248
print(type(a))  # <class 'int'>
