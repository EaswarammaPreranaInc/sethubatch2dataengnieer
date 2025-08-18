n = int(input("How many lines? : "))

for i in range(n):
    # Print spaces
    for j in range(n - i - 1):
        print(" ", end="")

    # Print stars
    for k in range(2 * i + 1):
        print("*", end="")

    # Move to next line
    print()
  
  ##########################################
  *
     ***
    *****
   *******
  *********
 ***********
*************
