#lista jest podobna do tupli, ale można ją modyfikować

lista = [1,2,3,4,5,6,7,12]

print(len(lista))
print(lista[0])
print(lista[-1])
print(lista[::2])

#APPEND DODAJE NA KONIEC LISTY
lista.append('ala')
print(lista)

#INSERT DODAJE GDZIEKOLWIEK
lista.insert(3,'kot')
print(lista)
lista.insert(len(lista),'tu byłem')
print(lista)

lista.reverse()
print(lista)
lista.reverse()
print(lista)

lista[3] = 'tu był element 4'
print(lista)

lista[3:7] = []
print(lista)

lista[3:7] = [0,0,0,0,0,0,0,0]

print(lista)