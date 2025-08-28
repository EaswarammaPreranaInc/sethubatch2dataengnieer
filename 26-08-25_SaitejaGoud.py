s=input("enter the string: ")
s= s.upper()
a= set(s)
vowels= "AEIOU"
b= ''
for x in a:
	if x in vowels:
		b+=x
print(b)

