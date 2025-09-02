'''
Write  a  program  to  evaluate  expression  like  calculator

Let  input  be  3 + 4 * 5 - 6 / 2 =
What  is  the  output ? --->  14.5

Hint:  Use  while  loop

Iteration             a          op        b               result
---------------------------------------------------------------------
       1              3          +          4           7   --->  'a'

	   2              7          *          5           35   --->  'a'

	   3             35         -          6           29   --->  'a'

	   4             29         /          2           14.5   --->  'a'

	   5            14.5       =          ----
'''

s = input("Enter expression with '=' : ")
s = s.replace(" ", "").rstrip("=")
a = int(s[0])
i = 1  
while i < len(s):
    op = s[i]
    b = int(s[i+1])
    if op == "+":
        a += b
    elif op == "-":
        a -= b
    elif op == "*":
        a *= b
    elif op == "/":
        a /= b
    i += 2
print("Result:", a)


'''
Output:

Enter expression with '=' : 3+4*5-6/2=
Result: 14.5

'''
    
