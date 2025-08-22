s = input("Enter string: ")
rev = ""
for i in range(len(s) - 1, -1, -1):
    rev = rev + s[i]
print(rev)

s = input("Enter string: ")
words = s.split()  # split string into words

for word in words:
    rev = ""
    for ch in word:
        rev = ch + rev  # build reversed word
    print(rev, end=" ")

s = input("Enter string: ")
chars = list(s)

for i in range(len(chars)):
    for j in range(len(chars) - i - 1):
        if chars[j] > chars[j + 1]:
            chars[j], chars[j + 1] = chars[j + 1], chars[j]

result = "".join(chars)
print(result)

