'''
2.3 Вывод данных на экран при помощи функции print and 2.4 Комментарии(#)
'''

#Programme 2.1 and 2.6.
print('Кейт Остен')     #Показать полное имя.
print('123 Фул Серкл Драйв')     #Показать адрес проживания.
print('Эшвиль, Северная Каролина 28899')     #Показать город и индекс.
#Programme 2.3(Строковые данные и строковые литералы)
#выводит строки содержащие апострофы
print("Из всех рассказов О'Генри")
print("мне больше нравится 'Вождь краснокожих'.")

'''
2.5 Переменные
'''

#Programme 2.8
# Создать две переменные: top_speed  и distance.
top_speed = 160
distance = 300

# Показать значения, на которые ссылаются переменные
print('Предельная скорость составляет')
print(top_speed)
print('Пройденное расстояние составляет')
print(distance)

#Programme 2.10
# Эта программа показывает повторное присвоение значения переменной.
# Присвоить значение переменной roubles.
roubles = 2.75
print('У меня на счете',roubles,'рублей.')

# Повторно присвоить значение переменной roubles,
# чтобы она ссылалась на другое значение.
roubles = 99.95
print('А теперь там',roubles,'рублей!')

#Programme 2.11
# Создать переменные, которые ссылаются на два строковых значения.
first_name = 'Кэтрин'
last_name = 'Марино'

# Показать значения, на которые эти переменные ссылаются
print(first_name, last_name)

'''
2.6 Чтение входных данных с клавиатуры
'''

#Programme 2.12
# Получить имя пользователя.
first_name = input('Введите свое имя: ')

# Получить фамилию пользователя
last_name = input('Введите свою фамилию: ')

# Напечать пользователю приветствие
print('Привет,', first_name, last_name)

#Programme 2.13
# Получить имя, возраст и доход пользователя
name = input('Как вас зовут?')
age = int(input('Сколько вам лет?'))
income = float(input('Какой у вас доход?'))

# Вывод данных на экран
print('Вот данные, которые Вы ввели:')
print('Имя:', name)
print('Возраст:', age)
print('Доход:', income)

'''
2.7 Выполнение расчетов
'''

#Programme 2.14
# Присвоить значение переменной salary.
salary = 25000.0

# Присвоить значение переменной bonus.
bonus = 12000.0

# Рассчитать заработную плату до удержаний, сложив  salary
# и  bonus. Присвоить результат переменной pay.
pay = salary + bonus

# Вывести переменную pay.
print('Ваша заработная плата состовляет', pay)

#Programme 2.15
# Эта программа получают исходную цену товара
# и вычисляет отпускную цену с 20%-й скидкой.

# Получить исходную цену товара.
original_price = float(input("Введите исходную цену товара: "))

# Вычислить сумму скидки
discount = original_price * 0.2

# Вычислить отпускную  цену.
sale_price = original_price - discount

# Показать отпускную цену
print('Отпускная цена составляет', sale_price)

#Programme 2.16 (среднее арифметическое значение)
#average = (a + b + c) / 3.0
# Получить три оценки и присвоить их переменным
# test1, test2 and test3.
test1 = float(input('Введите первую оценку: '))
test2 = float(input('Введите вторую оценку: '))
test3 = float(input('Введите третью оценку: '))

# Вычислить средний балл из трех оценок
# и присвоить результат переменной average.
average = (test1 + test2 + test3) / 3.0

# Показать переменную average.
print('Средний балл составляет', average)

#Оператор возведения в степень
#area = lenght**2

#Programme 2.17
# Получить от пользователя количество секунд.
total_seconds = float(input('Введите количество секунд: '))

# Получить количество часов.
hours = total_seconds // 3600

# Получить количество оставшихся минут.
minutes = (total_seconds // 60) % 60

# Получить количество оставшихся секунд.
seconds = total_seconds % 60

# Показать результаты.
print('Вот время в часах, минутах и секундах:')
print('Часы:', hours)
print('Минуты:', minutes)
print('Секунды:', seconds)

#Programme 2.18
# Получить требуемуе будущее значение.
future_value = float(input('Введите требуемое будущее значение: '))

# Получить годовую процентную ставку.
rate = float(input('Введите годовую процентную ставку: '))

# Получить количество лет хранение денег на счете.
years = int(input('Введите количество лет хранения денег на счете: '))

# Рассчитать сумму, необходимую для внесения денег на счет.
present_value = future_value / (1.0 + rate)**years

# Показать сумму, необходимую для внесения на счет.
print('Вам потребуется внести сумму:', present_value)

'''
2.8 (Конкатенация строковых литералов)
'''

#Programme 2.19
# Эта программа демонстрирует конкантенацию строковых литералов.
first_name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')

# Объединить имена с пробелом между ними.
full_name = first_name + ' ' + last_name

# Вывести на экран полное имя пользователя.
print('Ваше полное имя: ' + full_name)

'''
2.9 (Подробнее об инструкции print)
'''

print('one','two','three', sep='*')  #sep='~~~';''
print('One\nTwo\nThree')  # Переводит позицию печати на следующую строку
print('One\tTwo\tTree')  # Переводит позицию печати на следующую горизонтальную позицию табуляции
print("Домашнее задание на завтра - прочитать \"Гамлета\".")  # \'  Печатает двойную или одинарную кавычку
# \\ печатает обратную косую черту

'''
2.10 (Вывод на экран форматированного результата с помощью f-строк)
'''

#Programme 2.20
# Эта программа демонстрирует, как отображается число
# с плавающей точкой без форматирования.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'Ежемесячный платеж составляет {monthly_payment}.')

#Programme 2.21
# Эта программа демонстрирует округление числа
# с плавающей точкой.
amount_due = 5000.0
monthly_payment = amount_due / 12.0
print(f'Ежемесячный платеж составляет {monthly_payment:.2f}.')

#Programme 2.22
# Эта программа демонстрирует вывод на экран
# числа с плавающей точкой в качестве валюты.
monthly_pay = 5000.0
annual_pay = monthly_pay * 12
print(f'Ваша годовая зарплата составляет ${annual_pay:,.2f}')

#Programme 2.23
# Эта программа выводит на экран следующие ниже числа
# в двух столбцах.
num1 = 127.899
num2 = 3465.148
num3 = 3.776
num4 = 264.821
num5 = 88.081
num6 = 799.999

#Каждое число выводится в поле из 10 знаков и
# округляется до 2 знаков после точки.
print(f'{num1:10.2f}{num2:10.2f}')
print(f'{num3:10.2f}{num4:10.2f}')
print(f'{num5:10.2f}{num6:10.2f}')

#Programme 2.24
# Эта программа демонстрирует выравнивание строковых литералов по центу
name1 = 'Гордон'
name2 = 'Смит'
name3 = 'Вашингтон'
name4 = 'Альварадо'
name5 = 'Ливингстон'
name6 = 'Джонс'

# Вывод имен на экран
print(f'***{name1:^20}***')
print(f'***{name2:^20}***')
print(f'***{name3:^20}***')
print(f'***{name4:^20}***')
print(f'***{name5:^20}***')
print(f'***{name6:^20}***')

'''
2.12
'''

#Programme 2.25
# Эта программа наносит звезды созвездия Ориона,
# названия звезд и линии созвездия.
import turtle

# Задать размер окна.
turtle.setup(500, 600)

# Установить черепаху.
turtle.penup()
turtle.hideturtle()

# Создать именованные константы для звездных координат.
LEFT_SHOULDER_X = -70
LEFT_SHOULDER_Y = 200

RIGHT_SHOULDER_X = 80
RIGHT_SHOULDER_Y = 180

LEFT_BELTSTAR_X = -40
LEFT_BELTSTAR_Y = -20

MIDDLE_BELTSTAR_X = 0
MIDDLE_BELTSTAR_Y = 0

RIGHT_BELTSTAR_X = 40
RIGHT_BELTSTAR_Y = 20

LEFT_KNEE_X = -90
LEFT_KNEE_Y = -180

RIGHT_KNEE_X = 120
RIGHT_KNEE_Y = -140

# Нанести звезды.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)  # Левое плечо
turtle.dot()
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)  # Правое плечо
turtle.dot()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)  # Левая звезда в поясе
turtle.dot()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)  # Средняя звезда
turtle.dot()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)  # Правая звезда
turtle.dot()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)  # Левое колено
turtle.dot()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)  # Правое колено
turtle.dot()

# Вывести названия звезд.
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.write('Бетельгейзе')
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.write('Хатиса')
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.write('Альнитак')
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.write('Альнилам')
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.write('Минтака')
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.write('Саиф')
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)
turtle.write('Ригель')

# Нанести линию из левого плеча в левую звезду пояса
turtle.goto(LEFT_SHOULDER_X, LEFT_SHOULDER_Y)
turtle.pendown()
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из правого плеча в правую звезду пояса
turtle.goto(RIGHT_SHOULDER_X, RIGHT_SHOULDER_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из левой звезды пояса в среднюю звезду пояса
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.penup()

# Нанести линию из средней звезды пояса в правую звезду пояса
turtle.goto(MIDDLE_BELTSTAR_X, MIDDLE_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.penup()

# Нанести линию из левой звезды пояса в левое колено
turtle.goto(LEFT_BELTSTAR_X, LEFT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(LEFT_KNEE_X, LEFT_KNEE_Y)
turtle.penup()

# Нанести линию из правой звезды пояса в правое колено
turtle.goto(RIGHT_BELTSTAR_X, RIGHT_BELTSTAR_Y)
turtle.pendown()
turtle.goto(RIGHT_KNEE_X, RIGHT_KNEE_Y)

# Оставить окно открытым
turtle.done()