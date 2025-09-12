# Question 1: Find outputs (Home work)
def square(fun):
    def inner1():
        x = fun()
        return x * x
    return inner1

def double(fun):
    def inner2():
        y = fun()
        return 2 * y
    return inner2

@double
@square
def num():
    return 10
# end of the function

print(num())

# Answer 1:
# Step 1: num() → square(num) → returns 10 * 10 = 100
# Step 2: double(inner1) → 2 * 100 = 200
# Output: 200


# Question 2: Find outputs (Home work)
def bold(fun):
    def inner1():
        return '<b>' + fun() + '</b>'
    return inner1

def italic(fun):
    def inner2():
        return '<i>' + fun() + '</i>'
    return inner2

def underline(fun):
    def inner3():
        return '<u>' + fun() + '</u>'
    return inner3

@bold
@italic
@underline
def f1():
    return 'Hello World'
# End of the function

print(f1())

# Answer 2:
# Step 1: f1() → underline(f1) → '<u>Hello World</u>'
# Step 2: italic(inner3) → '<i><u>Hello World</u></i>'
# Step 3: bold(inner2) → '<b><i><u>Hello World</u></i></b>'
# Output: <b><i><u>Hello World</u></i></b>
