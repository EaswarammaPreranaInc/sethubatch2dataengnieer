from stack import stack

expe = input('Enter Parenthesis expression : ')

a = stack()
for ch in expe:
    if ch == '(':
        a.push(ch)
    elif ch == ')':
        x = a.pop()
        if x == None:
            print('Invalid')
            exit()

if a.isempty():
    print('Valid')
else:
    print('Invalid')