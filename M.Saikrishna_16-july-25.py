a = "Rama Rao"
print(a)  # Rama Rao
print(type(a))  # <class 'str'>
print(id(a))  # Will print memory address of string object

b = 'Hyd'
print(b)  # Hyd

c = '''Hyd is green city.
Hyd is hitec city.
Hyd is beautiful city.'''
print(c)
# Hyd is green city.
# Hyd is hitec city.
# Hyd is beautiful city.

a = 'Hyd'
print(a[0])  # H
print(a[1])  # y
print(a[2])  # d
print(a[3])  # IndexError: string index out of range

print(a[-1])  # d
print(a[-2])  # y
print(a[-3])  # H
print(a[0] == a[-3])  # True
a[2] = 'c'  # TypeError: 'str' object does not support item assignment (strings are immutable)

print(25[0])  # TypeError: 'int' object is not subscriptable
print('25'[0])  # '2'
print(True[1])  # TypeError: 'bool' object is not subscriptable
print('True'[1])  # 'r'

a = 'Hyd'
print(a * 3)  # 'HydHydHyd'
print(a * 2)  # 'HydHyd'
print(a * 1)  # 'Hyd'
print(a * 0)  # ''
print(a * -1)  # ''
print(25 * 3)  # 75
print('25' * 3)  # '252525'
print('25' * 4.0)  # TypeError: can't multiply sequence by non-int
print(3 * 'Hyd')  # 'HydHydHyd'
print('25' * True)  # '25' (True = 1)

a = 'Hyd'
print(a, id(a))  # 'Hyd' and its memory ID

a = a * 3
print(a, id(a))  # New object with different memory ID

print(len('Hyd'))  # 3
print(len('Rama Rao'))  # 8 (space included)
print(len('9247'))  # 4
print(len(''))  # 0
print(len(' '))  # 1
print(len(689))  # TypeError: object of type 'int' has no len()

a = """"Hyd"""  # SyntaxError due to unmatched quotes
b = """""Hyd"""  # SyntaxError again

a = 'Sankar Dayal Sarma'
print(a[7:12])  # Dayal
print(a[7:])  # Dayal Sarma
print(a[:6])  # Sankar
print(a[:])  # Full string
print(a[::])  # Same as above
print(a[1:10:2])  # akrDa
print(a[0::2])  # SnkrDylSrm
print(a[1::2])  # aaaa aa
print(a[-5:-1])  # Sarm
print(a[::-1])  # amraS lay a rakaS
print(a[-1:-5:-1])  # amra
print(a[::-2])  # aSlyDraS
print(a[3:-3])  # kar Dayal Sa
print(a[2:-5])  # nkar Dayal
print(a[-1:-5])  # '' (empty string)
print(a[3:3])  # '' (empty string)

a = 'A'
print(a[1])  # IndexError: string index out of range
print(a[1:])  # '' (valid slice, returns empty string)

print(int(10.8))  # 10
print(int(True))  # 1
print(int(False))  # 0
print(int('25'))  # 25
print(int('0075'))  # 75
print(int(0B11010))  # 26
print(0B11010)  # 26
print(int(0O6247))  # 3231
print(0O6247)  # 3231
print(int(0XA7B9))  # 42937
print(0XA7B9)  # 42937
print(int(3 + 4j))  # TypeError
print(int('25.4'))  # ValueError
print(int('Ten'))  # ValueError

print(float(25))  # 25.0
print(float(True))  # 1.0
print(float(False))  # 0.0
print(float('92'))  # 92.0
print(float('36.4'))  # 36.4
print(float('0075'))  # ValueError: leading zeros not allowed
print(float(0B1010101))  # 85.0
print(float(0O6247))  # 3231.0
print(float(0XA7B9))  # 42937.0
print(float(3 + 4j))  # TypeError
print(float('Ten'))  # ValueError

print(complex(3, 4))  # (3+4j)
print(complex(0, 4))  # 4j
print(complex(3))  # (3+0j)
print(complex(3.8, 4.6))  # (3.8+4.6j)
print(complex(3.8))  # (3.8+0j)
print(complex(3, 4.5))  # (3+4.5j)
print(complex(True, False))  # (1+0j)
print(complex(True))  # (1+0j)
print(complex(False))  # 0j
print(complex(True, 4))  # (1+4j)
print(complex('3'))  # (3+0j)
print(complex('3.8'))  # (3.8+0j)
print(complex(3, '4'))  # TypeError
print(complex('3', 4))  # TypeError
print(complex('3', '4'))  # TypeError
print(complex('Ten'))  # ValueError

print(bool(0))  # False
print(bool(10))  # True
print(bool(-25))  # True
print(bool(0.0))  # False
print(bool(0.1))  # True
print(bool(0 + 0j))  # False
print(bool(10 + 20j))  # True
print(bool(-15j))  # True
print(bool('False'))  # True (non-empty string is always True)
print(bool(''))  # False
print(bool('Hyd'))  # True
print(bool(' '))  # True
print(bool('True'))  # True
print(str(25))  # '25'
print(str(10.8))  # '10.8'
print(str(3 + 4j))  # '(3+4j)'
print(str(True))  # 'True'
print(str(False))  # 'False'
print(str(None))  # 'None'

print(oct(195))  # '0o303'
print(oct(0B10101110010))  # '0o1352'
print(oct(0xA7B9))  # '0o123671'

print(hex(25))  # '0x19'
print(hex(0B10101111010111))  # '0xafd7'
print(hex(0O6247))  # '0xca7'

