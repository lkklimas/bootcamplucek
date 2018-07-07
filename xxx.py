liczba = int(input('podaj liczbę:'))
lista = [1,2,3,4,5,6,7,8,9,10]

for x in lista:
    if x%2 == False:
        print(f'liczby podzielne przez 2:{x}')
for x in lista:
        if x%3 == False:
            print(f'liczby podzielne przez 3:{x}')

