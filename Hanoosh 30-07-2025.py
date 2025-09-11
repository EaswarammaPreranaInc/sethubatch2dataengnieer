'''
Write  a  program  to  print  full  pyramid
	 *
   ***
  *****
 *******
*********
Input  is  number  of  lines
'''
a = int(input("How many number of lines : "))
i = 1

while i <= n:
    spaces = n - i
    stars = 2 * i - 1

    j = 1

    while j <= spaces:
        print(" ", end="")
        j += 1

    k = 1
    while k <= stars:
        print("*", end="")
        k += 1

    print()

    i += 1