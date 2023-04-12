#1
# Получить число для дня недели.
day = int(input('Введите число (1-7) для дня недели: '))

# Определить название дня недели и показать его.
if day == 1:
    print('Понедельник')
elif day == 2:
    print('Вторник')
elif day == 3:
    print('Среда')
elif day == 4:
    print ('Четверг')
elif day == 5:
    print ('Пятница')
elif day == 6:
    print ('Суббота')
elif day == 7:
    print ('Воскресенье')
else:
    print ('Ошибка: пожалуйста, введите число в диапазоне между 1 и 7.')


#2
# Локальные переменные
lengthA = 0.0
widthA = 0.0
areaA = 0.0
lengthB = 0.0
widthB = 0.0
areaB = 0.0

# Получить длину A
lengthA = float(input('Введите длину A: '))

# Получить ширину A
widthA = float(input('Введите ширину A: '))

# Получить длину B
lengthB = float(input('Введите длину B: '))

# Получить ширину B
widthB = float(input('Введите ширину B: '))

# Вычислить площадь A
areaA = lengthA * widthA

# Вычислить площадь B
areaB = lengthB * widthB

# Напечатать сравнение площадей
print ('Площадь A:', format(areaA, '.2f'))
print ('Площадь B:', format(areaB, '.2f'))
if  areaA > areaB:
    print ('Площадь A больше площади B.')
elif  areaA < areaB:
    print ('Площадь B больше площади A.')
else:
    print ('Площадь A равна площади B.')