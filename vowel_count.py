inp = input("Enter the string").strip()
vowels="AEIOUaeiou"
count=0
num=0
for i in inp:
    if i.isalpha() and i in vowels:
        count+=1
    elif i.isdigit():
        num+=1
print(f"{count}\n{num}")