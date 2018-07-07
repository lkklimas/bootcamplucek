import random

print('''
Szukasz skarbu na planszy 10x10
Podaj w którą stronę idziesz:
[l]ewo
[p]rawo
[g]óra
[d]ół
wyjdziesz poza planszę to zginiesz!
''')

gracz_x = random.randrange(1,11)
gracz_y = random.randrange(1,11)

# resetuj planszę
skarb_x = random.randrange(1,11)
skarb_y = random.randrange(1,11)
a=0
odl_przed = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
min_liczba_krokow = odl_przed + 6

while True:
    # continue przerywa bieżący obrót pętli i wraca do nagłówka while
    # break wychodzi całkowicie z pętli
    print(f'twoja pozycja to {gracz_x},{gracz_y}')

    if skarb_x == gracz_x and skarb_y == gracz_y:
        print('Brawo! Skarb jest twój!')
        break

    if gracz_x < 1 or gracz_x > 10 or gracz_y < 1 or gracz_y > 10:
        print('Jesteś trupem')
        break

    if a >= min_liczba_krokow:
        # tu też resetuj planszę
        skarb_x = random.randrange(1, 11)
        skarb_y = random.randrange(1, 11)
        print('Spóźniłeś się. Smok zmienił siedzibę')
        odl_przed = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        a = 0
        min_liczba_krokow = odl_przed + 6

    krok = input()
    if krok == 'l':
        gracz_x -= 1
    elif krok == 'p':
        gracz_x += 1
    elif krok == 'g':
        gracz_y -= 1
    elif krok == 'd':
        gracz_y += 1
    else:
        continue

    a += 1
    zamglenie = random.randrange(1,6)
    if zamglenie > 1:
        odl_po = abs(gracz_x - skarb_x) + abs(gracz_y - skarb_y)
        if odl_przed > odl_po:
            print('ciepło')
        else:
            print('zimno')
        odl_przed = odl_po

print('koniec gry')