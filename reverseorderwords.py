s = input("Enter a sentence: ")
words = s.split()
rev_sentence = ''
for i in range(1, len(words)+1):
    rev_sentence += words[-i] + ' '
print("Reversed Words:", rev_sentence.strip())
