# Napisz program wyswietlajacy minimalna oraz maksymalna liczbe z
# wszystkich liczb wprowadzonych przez uzytkownika. Daj
# uzytkownikowi mozliwosc zakonczenia wprowadzania liczb
# odpowiednia komenda. Zadbaj o obsłuzenie przypadku gdy
# uzytkownik nie wprowadzi zadnej liczby.

komunikat = 'podaj kolejną liczbę lub wpisz [koniec]: '
res = input(komunikat)
min = res
max = res

while res != 'koniec':
    # tu coś robimy z res
    liczba = int(res)
    if liczba > int(max) :
        max = liczba
    if liczba < int(min) :
        min = liczba

    res = input(komunikat)

if min != 'koniec':
    print(f'najwieksza z podanych liczb to {max}')
    print(f'najmniejsza z podanych liczb to {min}')
else:
    print('nie podałeś żadnych liczb')