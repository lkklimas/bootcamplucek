import datetime
data = datetime.date.today()
print(data.year)

bieżący_rok = data.year
bieżący_rok = 2018

rok = int(input('podaj rok urodzenia: '))
wiek = bieżący_rok - rok

if wiek >= 18:
    print('jestes pełnoletni')
else:
    print('jestes dzieckiem')