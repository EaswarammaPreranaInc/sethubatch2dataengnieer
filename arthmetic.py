import math

class rat:
    def get(self):
        # Reads variable nr to object self with user input
        self.nr = int(input('Enter numerator : '))
        # Adds variable dr to object self with user input
        self.dr = int(input('Enter denominator : '))
        self.test() # Is denom of object self zero

    def test(self):
        # Repeat until dr is non-zero
        while self.dr == 0:
            # Reads non-zero denominator to object self
            self.dr = int(input('Denom can not be zero, reenter : '))

    def __str__(self):
        # Concatenates values of self to form a string with '/'
        return f'{self.nr} / {self.dr}'

    def add(self, a, b):
        self.nr = a.nr * b.dr + a.dr * b.nr # Adds variable nr to object self with the result
        self.dr = a.dr * b.dr # Adds variable dr to object self with the result
        self.simplify() # Simplifies values of object self

    def sub(self, a, b):
        self.nr = a.nr * b.dr - a.dr * b.nr # Adds variable nr to object self with the result
        self.dr = a.dr * b.dr # Adds variable dr to object self with the result
        self.simplify() # Simplifies values of object self

    def mul(self, a, b):
        self.nr = a.nr * b.nr # Adds variable nr to object self with the result
        self.dr = a.dr * b.dr # Adds variable dr to object self with the result
        self.simplify() # Simplifies values of object self

    def div(self, a, b):
        self.nr = a.nr * b.dr # Adds variable nr to object self with the result
        self.dr = a.dr * b.nr # Adds variable dr to object self with the result
        self.simplify() # Simplifies values of object self

    def simplify(self):
        if self.nr != 0:
            # gcd of values of self
            ans = math.gcd(self.nr, self.dr)
            # Simplifies nr of object self
            self.nr = self.nr // ans
            # Simplifies dr of object self
            self.dr = self.dr // ans

# End of the class
if __name__ == '__main__': # True when prog10a is executed and False when prog10a is imported
    a = rat() # Creates 6 empty rat objects
    b = rat()
    c = rat()
    d = rat()
    e = rat()
    f = rat()

    a.get() # Reads inputs to object 'a'
    b.get() # Reads inputs to object 'b'

    c.add(a, b) # Adds objects 'a' and 'b' and stores results in object 'c'
    d.sub(a, b) # Subtracts objects 'a' and 'b' and stores results in object 'd'
    e.mul(a, b) # Multiplies objects 'a' and 'b' and stores results in object 'e'

    if b.nr != 0:
        f.div(a, b) # Divides objects 'a' and 'b' and stores results in object 'f'

    # __str__() method of rat class returns values of object 'c' in the form of string
    print('Sum : ', c)
    # __str__() method of rat class returns values of object 'd' in the form of string
    print('Difference : ', d)
    # __str__() method of rat class returns values of object 'e' in the form of string
    print('Product : ', e)

    if b.nr != 0:
        # __str__() method of rat class returns values of object 'f' in the form of string
        print('Division : ', f)
    else:
        print('Division is not permitted')