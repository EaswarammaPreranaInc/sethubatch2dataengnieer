
# equilateral triangle with odd number of stars with natural numbers of stars
n=int(input("Enter number of lines: "))
for i in range(n):
   for _ in range(i+1):
      print(" "*(n-i-1), end='')
      print('* '*(i+1))
      break
      