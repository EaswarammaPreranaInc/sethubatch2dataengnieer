#name: Tarun Banala.      06-08-2025

1) Program with Walrus Operator (combine Lines 7 & 8 a single line).

Ans:-

try:
    sum = ctr = 0
    while (x := eval(input('Enter input (ctrl + z to stop) : '))) is not None:
        sum += x
        ctr += 1
except EOFError:
    try:
        print(F'Average : {sum / ctr}')
    except ZeroDivisionError:
        print('Enter at least one input')
except (NameError, TypeError):
    print('Input can not be string')
