# tupla luk krotka to struktura, która przechowuje więcej niż 1 wartość na raz

zmienna = (1,2,3,4)
print(zmienna)

a = ('ala','ma','kota')
b = ('ala', 'ma', 3.5, 'koty', 5, 6, 7, 8)
c = 0
print(b)
print(len(b))
print(a[0],)

c = 0
while c < len(b):
    print(b[c])
    c += 1
print(b)
print(b[1:3])
print(b[:3])
print(b[3:])
print(b[1:6:2])
print(b[::2])

print(b[:-1])
print(b[-3:])

print(b[1:-1])
print(b[::-1])

print(b[5:2:-1])
print(b[2:5:-1])

#zadanie 1


