ch = input("Enter any character: ")

if ch.isspace():
    print("White space")
elif ch.isalnum():
    print("Alpha Numeric Character")
    if ch.isalpha():
        print("Alphabet Character")
        if ch.isupper():
            print("Upper case Alphabet")
        else:
            print("lower case Alphabet")
    else:
        print("Digit character")
else:
    print("Special character")
