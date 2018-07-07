x = 50
y = 50

if 0 < x < 10:
    if y < 10:
        print('lewy górny róg')
    elif y > 90:
        print('lewy dolny róg')
    else:
        print('lewa krawędź')
elif 100 > x > 90:
    if y < 10:
        print('prawy górny róg')
    elif y > 90:
        print('prawy dolny róg')
    else:
        print('prawa krawędź')
elif 10 <= x <= 90:
    if y < 10:
        print('górna krawędź')
    elif y > 90:
        print('dolna krawędź')
    else:
        print('środek')
else:
    print('poza planszą')

#    sposób drugi (po angielsku, żeby nie mieć problemów z odmianą ;)
if x < 10:
    pos_x = 'left'
elif x > 90:
    pos_x = 'right'
else:
    pos_x = ''

if y < 10:
    pos_y = 'top'
elif y > 90:
    pos_y = 'bottom'
else:
    pos_y = ''

# oba wypełnione
if pos_x and pos_y:
    print(pos_y, pos_x,'corner')

# tylko jeden z nich wypełniony
elif pos_x or pos_y:
    print(pos_y, pos_x, 'edge')

# oba puste
else:
    print('center')

