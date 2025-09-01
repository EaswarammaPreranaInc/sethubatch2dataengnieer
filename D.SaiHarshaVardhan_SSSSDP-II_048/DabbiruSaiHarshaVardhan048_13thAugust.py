st = input("Enter the input: ")
vowels = "AEIOU"
printed = ""
st = st.upper()   

for ch in st:
    if ch in vowels and ch not in printed:
        printed += ch
        print(ch, end="")
