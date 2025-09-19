s = input("Enter mixed case string : ")
s = s.upper()
vowels = set("AEIOU")
res = set(s) & vowels
out = "".join(sorted(res, reverse=True))
print("Distinct vowels :", out)

'''
Output:
Enter mixed case string : RamA raO
Distinct vowels : OA
'''
