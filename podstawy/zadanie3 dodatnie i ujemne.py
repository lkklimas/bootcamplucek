# Napisz program zliczajacy wystapienia liczb dodatnich i ujemnych w
# zadanej liscie liczb całkowitych.'


lista = [-1, 0, 20, 0, -5, -7, -100, 300]

dod = 0
ujm = 0
zera = 0

for el in lista:
    if el > 0:
        dod += 1
    elif el < 0:
        ujm += 1
    else:
        zera += 1

print(f'dodatnich: {dod}, ujemnych: {ujm}, zer: {zera}')