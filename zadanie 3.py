lista = [-4,-3,-2,-1,0,1,2,3,4]

zero = 0
ujm = 0
dod = 0

for i in lista:
    if i > 0:
        dod += 1
    elif i < 0:
        ujm += 1
    else:
        zero += 1

print(f'dodatnich: {dod}, ujemnych: {ujm}, zer: {zero}')