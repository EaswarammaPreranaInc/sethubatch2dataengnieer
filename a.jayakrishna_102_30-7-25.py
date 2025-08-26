# Write  a  program  to  print  full  pyramid
a = int(input("How many lines ? : "))
for i in range(a):
    print(" " * (a - i - 1), end="")
    print("*" * (2 * i + 1))

"""o/p:
How many lines ? : 7
      *
     ***
    *****
   *******
  *********
 ***********
*************
"""