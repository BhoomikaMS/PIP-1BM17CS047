p = open("happyNum.txt", 'r')
h = open("primeNum.txt", 'r')

pl = p.read()
plist = pl.split(', ')
hl = h.read()
hlist = hl.split(', ')

prime = set(plist)
happy = set(hlist)
print(" ".join(map(str, prime.intersection(happy))))

p.close()
h.close()
