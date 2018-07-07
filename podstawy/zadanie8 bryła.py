a = int(input('podaj szerokość: '))
b = int(input('podaj wysokość: '))
c = int(input('podaj długość: '))

v = a*b*c
print(f'bryła o wymiarach {a}x{b}x{c} mieści 1 litr: {v >= 1000}')
print(v)

bryła = input('''podaj rodzaj bryly:
[p]rostopadloscian
[b]utelka
[s]tożek:''')
if bryła == 'p':
    pass
elif bryła == 'b':
    pass
elif bryła == 's':
    pass
else:
    print('nie znam takiej bryły')