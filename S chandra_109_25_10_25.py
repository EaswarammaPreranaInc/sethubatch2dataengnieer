'''
Repeat   prog7b  such  that
1) If  input  is   number ,   number  class  objects  should  be  added
2) If  input  is  string  ,  string  class  objects  should  be  joined

1) Import  number  and  string  classes  defined  in  prog7b  but  do  no  rewrite

2) Refer  to  prog8
'''

while True:
    choice = input("Enter number / string / exit : ").lower()

    if choice == "number":
        n1 = float(input("Enter any number : "))
        n2 = float(input("Enter any number : "))
        print("Sum of the numbers : ", n1 + n2)

    elif choice == "string":
        s1 = input("Enter any string : ")
        s2 = input("Enter any string : ")
        print("Join of the two strings : ", s1 + s2)

    elif choice == "exit":
        print("Good Bye")
        break

    else:
        print("Invalid input, please enter number / string / exit")
