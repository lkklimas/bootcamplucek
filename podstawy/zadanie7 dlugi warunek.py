liczba = int(input('podaj liczbę: '))

# tak można podzielić na linie zbyt długi warunek
sprawdz = liczba % 2 == 0 and liczba % 3 == 0 and liczba
sprawdz = sprawdz or liczba == 7

print(f'liczba spełnia dlugi warunek: '
      f'{liczba % 2 == 0 and liczba % 3 == 0 and liczba > 10 or liczba == 7}')

# leniwy python
a = 1
if a == 1:
    print('super, piewrwszy warunek spełniony')
elif a < 4:
    print('drugi warunek spełniony')
else:
    print('nie spełnia')

# jeśli z pierwszego warunku wiem jaki będzie ostateczny wynik to nie musze liczyć drugiego
#  dla a = 1 działa
#  dla a = 2 wywala błąd składniowy
a= 2
if a == 1 or a > '2':
    print('drugi warunek nigdy nie sprawdzony')
else:
    print('buu')