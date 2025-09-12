#find outputs(home work):- 

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

print(num())                                     #200



#find outputs(home work):- 

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
    return 'Hello  World'

print(f1())                                      #<b><i><u>Hello  World</u></i></b>
