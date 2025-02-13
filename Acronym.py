inp = input("Enter the input:")
acronym=""
words = inp.split()
for word in words:
    acronym+=word[0].upper()

print(acronym)