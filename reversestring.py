s = input("Enter any string: ")
rev = ''
for i in range(1, len(s)+1):
    rev += s[-i]
print("Reverse String:", rev)
