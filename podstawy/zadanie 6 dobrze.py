liczby = [5,2,1,4,3]

print(liczby)

index_min = None
index_max = None

for index in range(len(liczby)):
    if index == 0:
        index_max = index
        index_min = index
        print(index_max,index_min)
    else:
        if liczby[index] > liczby[index_max]:
            index_max = index
        if liczby [index < liczby[index_min]]:
            index_min = index
print(index_min, index_max)

min = liczby [index_min]
max = liczby[index_max]

liczby[index_max] = min
liczby[index_min] = max

print(liczby)