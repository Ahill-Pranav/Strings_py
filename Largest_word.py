inp = input("Enter string:").strip()
words=inp.split()
largest=""
maxi=0
for word in words:
    if len(word)>maxi:
        largest=word
        maxi=len(word)
print(largest)