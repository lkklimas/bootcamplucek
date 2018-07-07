print('Witaj świecie!')

# int - liczba całkowita
a = 3
b = 4

asdfghj_kl234 = 8
ala_ma_kota = 90
iopo = 0

# float - liczba ułamkowa
ulamek = 4.5
inne_opcje = .3
test = 3.

# błędy zaokrągleń
print(0.1 + 0.2)

# str - napisy
napis1 = "ala ma kota"
napis2 = 'ala ma kota'

print(napis1)
print(napis2)
print(napis1 == napis2)

# bool - wartości logiczne
prawda = True
fałsz = False

a = ''
if a:
    print('a zinterpretowane jako prawda')
else:
    print('a zinterpretowane jako fałsz')

# OGOLNA UWAGA: nie róbcie literówek ;)
ine_opcje = 9
print(inne_opcje + 4)


# operator dodawania - +
# operator odejmowania - -
# operator mnozenia - *
# operator dzielenia - /
# operator dzielenia całkowitoliczbowego - //
# operator modulo (reszta z dzielenia) - %
# operator potegi - **

# pole trójkata o podstawie 10 i wysokosci 5
# pole koła o promieniu 7
# pole trapezu o długosci podstaw 3 i 9 oraz wysokosci 6.5
# objetosc kuli o promieniu 7/8
a = 10
h = 5
pole_trojkata = a * h / 2
print(pole_trojkata)
pi = 3.14
r = 7
pole_kola = pi * r ** 2
print(pole_kola)
a = 3
b = 9
h = 6.5
pole_trapezu = (a+b) * h / 2
print(pole_trapezu)
r = 7/8
objetosc_kuli = 4/3 * pi * r ** 3
print(objetosc_kuli)

print(a)
print('a ma wartość: ',a,sep='', end=' ' )
print(f'a ma wartość: {a}\ndruga linia z wyliczeniem: {2+2}')
print(f'''ala ma kota
    druga linia
    trzecia linia i warotść zmiannej {a}''')

# <10 wyrównaj do lewej
# ^10 wyrównaj do środka
# >10 wyrównaj do prawej
cena = 10.0
waga = 2.5
print(f'{"Cena:":<8} {cena:>5.2f} pln\n'
      f'{"Waga:":<8} {waga:>5.2f} kg\n'
      f'{"Koszt:tralala":<8} {cena * waga:>5.2f} pln')

print("I'm the boss")

# dygresja : to jest xor na bitach
print(7^9)


