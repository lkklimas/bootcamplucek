miasto_a = input('Miasto A: ')
miasto_b = input('Miasto B: ')
dystans = float(input(f'Dystans pomiędzy {miasto_a}-{miasto_b}: '))
cena = float(input('cena paliwa: '))
spalanie = float(input('spalanie na 100km: '))

print(f'Koszt przejazdu {miasto_a}-{miasto_b} wynosi {round(dystans*cena*spalanie/100,2)} PLN')
print(f'Koszt przejazdu {miasto_a}-{miasto_b} wynosi {dystans*cena*spalanie/100:.2f} PLN')


