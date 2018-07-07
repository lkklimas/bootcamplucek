# Napisz program obliczajacy srednia wartosc temperatury w danym
# tygodniu na podstawie temperatur wprowadzonych przez
# uzytkownika.

ile_dni = 7
nr_dnia = 1
suma_temp = 0
while nr_dnia <= ile_dni:
    suma_temp += int(input(f'podaj temp dnia {nr_dnia}: '))
    nr_dnia += 1

srednia_temp = suma_temp / ile_dni
print(f'średnia temp w tym tygodniu wyniosła {srednia_temp}')