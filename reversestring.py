stri=input("Enter a string: ")
li=list(stri.split())
revli=li[::-1]
print(" ".join(revli))
for word in li:
    print(''.join(reversed(word)),end=" ")
print()
