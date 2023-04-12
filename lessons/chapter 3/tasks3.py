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

#3

# Получить возвраст человека.
age = int(input('Введите возраст: '))

# Определить, является ли этот человек младенцем, ребенком,
# подростком или взрослым, и показать результат.
if age <= 1:
    print('Младенец')
elif age > 1 and age < 13:
    print('Ребенок')
elif age > 13 and age < 20:
    print('Подросток')
else:
    print ('Взрослый')

#4

# Получить число
number = int(input('Введите целое число между 1 и 10: '))

# Напечатать римскую цифру
if number == 1:
    print ('I')
elif number == 2:
    print ('II')
elif number == 3:
    print ('III')
elif number == 4:
    print ('IV')
elif number == 5:
    print ('V')
elif number == 6:
    print ('VI')
elif number == 7:
    print ('VII')
elif number == 8:
    print ('VIII')
elif number == 9:
    print ('IX')
elif number == 10:
    print ('X')
else:
    print ('Ошибка: недопустимое число')

#5

# Глобальные константы
MASS_MULTIPLIER = 9.8
TOO_HEAVY = 500.0
TOO_LIGHT = 100.0

# Локальные переменные
weight = 0.0
mass = 0.0

# Получить массу
mass = float(input("Введите массу тела в килограммах: "))

# Вычислить вес
weight = mass * MASS_MULTIPLIER

# Показать расчет веса
print ('Вес объекта: ', format(weight, '.2f'))
if weight > TOO_HEAVY:
    print ('Объект слишком тяжелый. Он весит более',
           TOO_HEAVY, 'ньютонов.')
elif  weight < TOO_LIGHT:
    print ('Объект слишком легкий. Он весит менее',
           TOO_LIGHT, 'ньютонов.')

#6

# Получить день
day = int(input('Введите день месяца: '))

# Получить месяц
month = int(input('Введите месяц в числовой форме: '))

# Получить год
year = int(input('Введите год в числовой форме: '))

# Проверить, введен ли допустимый день
if day > 31 or day < 1:
    print('Ошибка: введен недопустимый день')

# Проверить, введен ли допустимый месяц
elif month > 12 or month < 1:
    print('Ошибка: введен недопустимый месяц')

# Проверить, введен ли допустимый год
elif year > 99 or year < 0:
    print('Ошибка: введен недопустимый год')

# Введенные данные допустимы
else:
    # Показать расчет магической даты
    print('Введена дата ', day, '/', month, '/', year)
    if (day * month) == year:
        print('Это магическая дата.')
    else:
        print('Это не магическая дата.')