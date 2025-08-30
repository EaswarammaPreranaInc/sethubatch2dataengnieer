Write  a  program  to  print  distinct  vowels  of  the  string  by  using  set
s = "RamA Rao"
vowels = set("aeiou")
found = {ch.lower() for ch in s if ch.lower() in vowels}
result = ""
for ch in s:
    if ch.lower() in found and ch.upper() not in result:
        result += ch.upper()
print(result)
