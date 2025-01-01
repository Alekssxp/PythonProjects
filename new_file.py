def triangle (*size, symb):
    for i in size:
        i += i + 1
        print (symb * i)
size = int(input ('Введите размер треугольника:'))
symb = input ('Введите символ:')
triangle (size, symb)