expr = "123+45+6+789"
numbers = expr.split("+")
total = sum(int(n) for n in numbers)
print("Sum:", total)   # 963
