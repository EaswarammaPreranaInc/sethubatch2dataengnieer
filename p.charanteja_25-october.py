from prog7b import number, string

while True:
    c = input("Enter number / string / exit : ")
    if c == "number":
        n1 = input("Enter any number   : ")
        n2 = input("Enter any number   : ")
        num1 = number(n1)
        num2 = number(n2)
        num_sum = num1 + num2
        print("Sum of the numbers : ", num_sum)
    elif c == "string":
        s1 = input("Enter any string   : ")
        s2 = input("Enter any string   : ")
        str1 = string(s1)
        str2 = string(s2)
        str_join = str1 + str2
        print("Join of the two strings : ", str_join)
    elif c == "exit":
        print("Good Bye")
        break
    else:
        print("Invalid input, try again!")
