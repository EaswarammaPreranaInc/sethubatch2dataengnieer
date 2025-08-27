'''One of the built-in functions of Python is divmod, 
which takes two arguments a and b and returns a tuple containing the quotient of a/b first and then the remainder a.

For example:
>>> print divmod(177,10)
(17, 7)
'''




a = int(input("Enter 1st number : "))
b = int(input("Enter 2nd number : "))
print(a//b)
print(a%b)
print(divmod(a,b)) 
