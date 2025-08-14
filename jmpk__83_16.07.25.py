# ==============================
# Boolean Object Demo Program
# ==============================
a = True  # Ref 'a' points to Object True
print(a)  # Value of Object 'a' is True
print(type(a))  # Type of Object 'a' is class bool
print(id(a))    # Address of Object 'a'

b = False  # Ref 'b' points to Object False
print(b)  # Value of Object 'b' is False
print(type(b))  # Type of Object 'b' is class bool

print(True + True)   # 1+1=2 (True is 1, False is 0)
print(True + False)  # 1+0=1
print(False + True)  # 0+1=1
print(False + False) # 0+0=0
print(True + True + True) # 1+1+1=3
print(25 + 10.8 + True)   # int + float + 1 → 36.8

print(True > False) # True
print(True)         # Value is True
print(False)        # Value is False
# print(true)       # Error: constants should be uppercase
# print(false)      # Error

# ==============================
# Complex Object Demo Program
# ==============================
a = 3 + 4j  # 3 is real, 4 is imaginary
print(a)
print(type(a))
print(id(a))
print(a.real)  # 3.0
print(a.imag)  # 4.0

a = 6j
print(a)
print(type(a))
print(a.real)  # 0.0
print(a.imag)  # 6.0

# print(5 + j6)   # Error
# Python uses 'j' for imaginary
print(4 + 1j)   # (4+1j)
print(4 + 0j)   # (4+0j)

# ==============================
# Float Object Demo Program
# ==============================
a = 10.8
print(a)
print(type(a))
print(id(a))

b = 25.0
print(b)
print(type(b))

c = 0.689
print(c)

d = 3.4E2
print(d)       # 340.0
print(type(d))

e = 9.62e-2
print(e)       # 0.0962

# print(9.8.2)  # Error

# ==============================
# float() Function Demo
# ==============================
print(float(25))
print(float(True))
print(float(False))
print(float("92"))
print(float("36.4"))
# print(float("100f"))  # Error
print(float(0b1010101))
print(float(0o6247))
print(float(0xA7B9))
# print(float(3 + 4j))  # Error
# print(float("ten"))   # Error

# ==============================
# complex() Function Demo
# ==============================
print(complex(3, 4))
print(complex(0, 7))
print(complex(3))
print(complex(3.8, 4.6))
print(complex(3.8))
print(complex(3, 9.5))
print(complex(True, False))
print(complex(True))

# ==============================
# int() Function Demo
# ==============================
print(int(10.9))
print(int(True))
print(int(False))
print(int("25"))
# print(int("0075"))  # Error
print(int(0b11010))
print(int(0o6247))
print(int(0xA7B9))
# print(int(3 + 4j))  # Error
print(int(25.41))
# print(int("ten"))   # Error

# ==============================
# len() Function Demo
# ==============================
print(len("Hyd"))
print(len("Rama Rao"))
print(len("9247"))
print(len(""))
print(len(" "))
# print(len(699))  # Error

a = "Hyd"
print(a)
print(len(a))
print(a[0])

b = """uuuHyd"""
print(b)
print(len(b))

# ==============================
# String Multiplication Demo
# ==============================
a = "Hyd"
print(a * 3)
print(a * 2)
print(a * 1)
print(a * 0)
print(a * -1)
print(25 * 3)
print("25" * 3)
# print("25" * 4.0)  # Error
print(3 * "Hyd")
print("25" * True)

a = "Hyd"
print(a, id(a))
a = a * 3
print(a, id(a))

# ==============================
# Index Demo
# ==============================
a = "Hyd"
print(a[0])
print(a[1])
print(a[2])
# print(a[3])  # Error
print(a[-1])
print(a[-2])
print(a[-3])
# print(a[-4]) # Error
print(a[0] == a[-3])
# a[2] = "c"  # Error
print("25"[0])
# print(True[1])  # Error
print("True"[1])

# ==============================
# String Object Demo
# ==============================
a = "Rama Rao"
print(a)
print(type(a))
print(id(a))

b = "Hyd"
print(b)

c = """Hyd is green city.
Hyd is hitech city.
Hyd is beautiful city."""
print(c)
