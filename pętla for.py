#

lista = [1,2,3,4,5,6,7,8,]

for el in lista:
    print(el)
print("----------------------")

tupla = ('ala','ma',3, 'koty','które','ją','nienawidzą')

for el in tupla:
    print(el)
print("----------------------")

for nr, zmienna in enumerate(tupla, start=1):
    print(nr, zmienna)
print("----------------------")

for i in range(len(tupla)):
    print(i, tupla[i])

print("----------------------")

for i in range(1,len(tupla),2):
    print(i, tupla[i])