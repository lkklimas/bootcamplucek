lista = (1,2,3,4,5,6,7,8,9)
a = -1
b = 0


for x in lista:
    c = int(lista[b])
    d = int(lista[a])
    lista.insert(x,d)
    b = b + 1
    a = b - 1
print(lista)

