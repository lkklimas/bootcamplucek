liczba1 = float(input('podaj pierwszą liczbę: '))
liczba2 = float(input('podaj drugą liczbę: '))
operacja = input('podaj operację [+-*/]: ')

if operacja == '+':
    wynik = liczba1 + liczba2
elif operacja == '-':
    wynik = liczba1 - liczba2
elif operacja == '*':
    wynik = liczba1 * liczba2
elif operacja == '/':
    if liczba2 == 0:
        exit('nie wolno dzielić przez 0')
    wynik = liczba1 / liczba2
else:
    exit('nieznana operacja')

print(f'wynikiem działania jest {wynik}')