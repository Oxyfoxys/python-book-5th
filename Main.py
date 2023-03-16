import turtle

from stars import orion


def other():
    '''
    2.3 Вывод данных на экран при помощи функции print and 2.4 Комментарии(#)
    '''

    # Programme 2.1 and 2.6.
    print('Кейт Остен')  # Показать полное имя.
    print('123 Фул Серкл Драйв')  # Показать адрес проживания.
    print('Эшвиль, Северная Каролина 28899')  # Показать город и индекс.
    # Programme 2.3(Строковые данные и строковые литералы)
    # выводит строки содержащие апострофы
    print("Из всех рассказов О'Генри")
    print("мне больше нравится 'Вождь краснокожих'.")

    '''
    2.5 Переменные
    '''

    # Programme 2.8
    # Создать две переменные: top_speed  и distance.
    top_speed = 160
    distance = 300

    # Показать значения, на которые ссылаются переменные
    print('Предельная скорость составляет')
    print(top_speed)
    print('Пройденное расстояние составляет')
    print(distance)

    # Programme 2.10
    # Эта программа показывает повторное присвоение значения переменной.
    # Присвоить значение переменной roubles.
    roubles = 2.75
    print('У меня на счете', roubles, 'рублей.')

    # Повторно присвоить значение переменной roubles,
    # чтобы она ссылалась на другое значение.
    roubles = 99.95
    print('А теперь там', roubles, 'рублей!')

    # Programme 2.11
    # Создать переменные, которые ссылаются на два строковых значения.
    first_name = 'Кэтрин'
    last_name = 'Марино'

    # Показать значения, на которые эти переменные ссылаются
    print(first_name, last_name)

    '''
    2.6 Чтение входных данных с клавиатуры
    '''

    # Programme 2.12
    # Получить имя пользователя.
    first_name = input('Введите свое имя: ')

    # Получить фамилию пользователя
    last_name = input('Введите свою фамилию: ')

    # Напечать пользователю приветствие
    print('Привет,', first_name, last_name)

    # Programme 2.13
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

    # Programme 2.14
    # Присвоить значение переменной salary.
    salary = 25000.0

    # Присвоить значение переменной bonus.
    bonus = 12000.0

    # Рассчитать заработную плату до удержаний, сложив  salary
    # и  bonus. Присвоить результат переменной pay.
    pay = salary + bonus

    # Вывести переменную pay.
    print('Ваша заработная плата состовляет', pay)

    # Programme 2.15
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

    # Programme 2.16 (среднее арифметическое значение)
    # average = (a + b + c) / 3.0
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

    # Оператор возведения в степень
    # area = lenght**2

    # Programme 2.17
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

    # Programme 2.18
    # Получить требуемуе будущее значение.
    future_value = float(input('Введите требуемое будущее значение: '))

    # Получить годовую процентную ставку.
    rate = float(input('Введите годовую процентную ставку: '))

    # Получить количество лет хранение денег на счете.
    years = int(input('Введите количество лет хранения денег на счете: '))

    # Рассчитать сумму, необходимую для внесения денег на счет.
    present_value = future_value / (1.0 + rate) ** years

    # Показать сумму, необходимую для внесения на счет.
    print('Вам потребуется внести сумму:', present_value)

    '''
    2.8 (Конкатенация строковых литералов)
    '''

    # Programme 2.19
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

    print('one', 'two', 'three', sep='*')  # sep='~~~';''
    print('One\nTwo\nThree')  # Переводит позицию печати на следующую строку
    print('One\tTwo\tTree')  # Переводит позицию печати на следующую горизонтальную позицию табуляции
    print("Домашнее задание на завтра - прочитать \"Гамлета\".")  # \'  Печатает двойную или одинарную кавычку
    # \\ печатает обратную косую черту

    '''
    2.10 (Вывод на экран форматированного результата с помощью f-строк)
    '''

    # Programme 2.20
    # Эта программа демонстрирует, как отображается число
    # с плавающей точкой без форматирования.
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    print(f'Ежемесячный платеж составляет {monthly_payment}.')

    # Programme 2.21
    # Эта программа демонстрирует округление числа
    # с плавающей точкой.
    amount_due = 5000.0
    monthly_payment = amount_due / 12.0
    print(f'Ежемесячный платеж составляет {monthly_payment:.2f}.')

    # Programme 2.22
    # Эта программа демонстрирует вывод на экран
    # числа с плавающей точкой в качестве валюты.
    monthly_pay = 5000.0
    annual_pay = monthly_pay * 12
    print(f'Ваша годовая зарплата составляет ${annual_pay:,.2f}')

    # Programme 2.23
    # Эта программа выводит на экран следующие ниже числа
    # в двух столбцах.
    num1 = 127.899
    num2 = 3465.148
    num3 = 3.776
    num4 = 264.821
    num5 = 88.081
    num6 = 799.999

    # Каждое число выводится в поле из 10 знаков и
    # округляется до 2 знаков после точки.
    print(f'{num1:10.2f}{num2:10.2f}')
    print(f'{num3:10.2f}{num4:10.2f}')
    print(f'{num5:10.2f}{num6:10.2f}')

    # Programme 2.24
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


if __name__ == '__main__':
    print(orion.__doc__)
    orion()


'''
simulator chapter 2
'''
 #1
height = int(input('Введите свой рост: '))

#2
color = input('Введите свой любимый цвет: ')

#3
'''
b = a + 2
a = b * 4
b = a / 3.14
a = b - 8
'''

#4
w = 5
x = 4
y = 8
z = 2

result1 = x+y
result2 = z*2
result3 = y/x
result4 = y-z
result5 = w//z
print(result1, result2, result3, result4, result5)

#5
total = 10 + 14

#6
#due = total - down_payment

#7
#total = subtotal * 0.15

#8
a = 5
b = 2
c = 3
result = a + b * c
print(result)

#9
num = 99
num = 5
print(num)

#10
#print(format(sales, '.2f))

#11
number = 1234567.456
print(format(number, ',.1f'))

#12
print('Джордж', 'Джон', 'Пол', 'Ринго', sep='@')

#13
#turtle.circle(75)

#14
'''
import turtle
turtle.hideturtle()
turtle.fillcolor('blue')
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()
'''
#15
'''
import turtle
turtle.hideturtle()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(30)
turtle.setheading(0)
turtle.pendown()
turtle.fillcolor('red')
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()
'''

'''
exercise
'''
#1
print('Aleks lutic')
print('Эшвиль, Северная Каролина 28899')
print('89234657823')
print('профильная')

#2
total_amount =float(input('Введите сумму общего объема продаж:'))
pta = 0.23 #процент от общей суммы
sn = total_amount / 100 * pta
print(sn)

#3
total_number = float(input('Введите общее количество квадратных метров:'))
ackr = 4046.86
na = total_number / 4047 * ackr
print(na)

#4
product1 = float(input('Введите цену товара 1: '))

product2 = float(input('Введите цену товара 2: '))

product3 = float(input('Введите цену товара 3: '))

product4 = float(input('Введите цену товара 4: '))

product5 = float(input('Введите цену товара 5: '))

subTotal = (product1 + product2 + product3 + product4 + product5)

salesTax = subTotal * 0.07

total = subTotal + salesTax

print('sub total: ',format(subTotal , ',.2f'))
print('sales tax: ',format(salesTax , ',.2f'))

#5
speed = 70
distance = speed * 6
distance2 = speed * 10
distance3 = speed * 15
print(distance, distance2, distance3)

#6
amount = float(input("Введите общую сумму покупки: "))

federal_tax = amount * 0.05
regional_tax = amount * 0.025

totalSale = ( amount + federal_tax + regional_tax )

print('Сумма покупки :',format(amount, ',.2f'))
print('Сумма федерального налога с продажи: ',format(federal_tax , ',.2f'))
print('Сумма регионального налога с продажи: ',format(regional_tax , ',.2f'))
print('Итоговая сумма :',format(totalSale,',.2f'))

#7
#расход = пройденные километры / расход бензина в литрах
# kilometers_per_litre = kilometers / litres
kilometers = float(input('Введите пройденные километры: '))

litres = float(input('Введите литры потребленного топлива: '))

kilometers_per_litre = kilometers / litres

print('Вы использовали', format(kilometers_per_litre, '.2f'), 'литров на километр')

#8
TAX_RATE = 0.07  #налоговая ставка
TIP_RATE = 0.18  #ставка чаевых

food = float(input('Введите стоимость еды: '))

tip = food * TIP_RATE

tax = food * TAX_RATE

total = food + tip + tax  #итоговая сумма

print('Чаевые: $', format(tip, '.2f'))
print('Налог: $', format(tax, '.2f'))
print('Итоговая сумма: $', format(total, '.2f'))

#9
celsius = float(input('Введите температуру по шкале Цельсия: '))

fahrenheit = (9 / 5) * celsius + 32

print('Она равна', format(fahrenheit, '.2f'), 'градусам по Фаренгейту')

#10
COOKIES_RECIPE = 48
SUGAR_RECIPE = 1.5
BUTTER_RECIPE = 1
FLOUR_RECIPE = 2.75

cookies = float(input("Введите количество булочек: "))   #количество булочек

sugar = (cookies * SUGAR_RECIPE) / COOKIES_RECIPE  #стаканы воды

butter = (cookies * BUTTER_RECIPE) / COOKIES_RECIPE  #стаканы масла

flour = (cookies * FLOUR_RECIPE) / COOKIES_RECIPE  #стаканы муки

print("Чтобы изготовить", cookies, "булочек, вам понадобятся:")
print(format(sugar, '.2f'), "стаканов сахара")
print(format(butter, '.2f'), "стаканов масла")
print(format(flour, '.2f'), "стаканов муки")

#11
men = int(input('Введите количество учащихся мужского пола: '))
women = int(input('Введите количество учащихся женского пола: '))

total = men + women

percentMen = men / total

percentWomen = women / total

print('Юноши: ', format(percentMen, '.2f'), '%')
print('Девушки: ', format(percentWomen, '.2f'), '%')

#12
COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

amountPaidForStock = 0.0  # Сумма, выплаченная за акции
purchaseCommission = 0.0  # Комиссия, уплаченная за покупку акций
totalPaid = 0.0           # Итоговая уплаченная сумма
stockSoldFor = 0.0        # Сумма, за которую акции были проданы
sellingCommission = 0.0   # Комиссия, уплаченная за продажу акций
totalReceived = 0.0       # Итоговая полученная сумма
profitOrLoss = 0.0        # Сумма дохода или убытка

amountPaidForStock = NUM_SHARES * PURCHASE_PRICE   # Вычислить сумму, которую Джо уплатил за акции, не включая комиссию.

purchaseCommission = COMMISSION_RATE * amountPaidForStock  # Вычислить сумму комиссию, которую Джо уплатил брокеру при покупке акций.

totalPaid = amountPaidForStock + purchaseCommission  # Вычислить общую сумму, которую Джо уплатил

stockSoldFor = NUM_SHARES * SELLING_PRICE   # Вычислить сумму, за которую Джо продал акции.

sellingCommission = COMMISSION_RATE * stockSoldFor  # Вычислить сумму комиссии, которую Джо уплатил брокеру

totalReceived = stockSoldFor - sellingCommission  # Вычислить сумму денег, оставшихся после того, как Джо заплатил брокеру

profitOrLoss = totalReceived - totalPaid   # Вычислить сумму дохода или убытка

print('Сумма, уплаченная за акции: $', format(amountPaidForStock, '.2f'))
print('Комиссия, уплаченная при покупке: $', format(purchaseCommission, '.2f'))
print('Сумма, вырученная от продажи акций: $', format(stockSoldFor, '.2f'))
print('Комиссия, уплаченная при продаже: $', format(sellingCommission, '.2f'))
print('Доход (или убыток, если число отрицательное): $', format(profitOrLoss, '.2f'))

#13
print('Введите длину гряды в метрах: ', end='')
R = float(input())

print('Введите объем пространства в метрах, используемого под трельяжные концевые опоры: ', end='')
E = float(input())

print('Введите расстояние в метрах между каждой лозой: ', end='')
S = float(input())

V = (R - 2 * E) / S

print('У вас достаточно места для', V, 'виноградных лоз.')

#14
print('Введите начальный остаток основного счета: ', end='')
P = float(input())

print('Введите годовую ставку процента: ', end='')
r = float(input())

print('Сколько раз в году начисляется сложный процентный доход? ', end='')
n = int(input())

print('Сколько лет этот счет будет получать процентные начисления? ', end='')
t = int(input())

r = r / 100

A = P * (1 + float(r) / n) ** (n * t)

print('В конце периода из', t, 'лет у вас будет $', format(a, ',.2f'))

#15
#1
'''
import turtle

turtle.hideturtle()

turtle.fillcolor('red')
# romb1
turtle.begin_fill()
turtle.left(135)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()
# romb2
turtle.begin_fill()
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.end_fill()
'''

#2
'''
import turtle

OUTER_TOP_X = 0
OUTER_TOP_Y = 200
INNER_TOP_X = OUTER_TOP_X
INNER_TOP_Y = OUTER_TOP_Y / 2
BASE_LEFT_X = -100
BASE_LEFT_Y = 0
BASE_RIGHT_X = 100
BASE_RIGHT_Y = 0

turtle.hideturtle()
turtle.penup()

turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)

turtle.fillcolor('red')
turtle.pendown()

#внешний треугольник.
turtle.goto(OUTER_TOP_X, OUTER_TOP_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)

#внутренний треугольник
turtle.begin_fill()
turtle.goto(INNER_TOP_X, INNER_TOP_Y)
turtle.goto(BASE_LEFT_X, BASE_LEFT_Y)
turtle.goto(BASE_RIGHT_X, BASE_RIGHT_Y)
turtle.end_fill()
'''

'''
#3
import turtle

TOP_SQUARE_TOP_LEFT_X = -100
TOP_SQUARE_TOP_LEFT_Y = 100
TOP_SQUARE_TOP_RIGHT_X = 0
TOP_SQUARE_TOP_RIGHT_Y = 100
TOP_SQUARE_BOTTOM_LEFT_X = -100
TOP_SQUARE_BOTTOM_LEFT_Y = 0
TOP_SQUARE_BOTTOM_RIGHT_X = 0
TOP_SQUARE_BOTTOM_RIGHT_Y = 0

BOTTOM_SQUARE_TOP_LEFT_X = 0
BOTTOM_SQUARE_TOP_LEFT_Y = 0
BOTTOM_SQUARE_TOP_RIGHT_X = 100
BOTTOM_SQUARE_TOP_RIGHT_Y = 0
BOTTOM_SQUARE_BOTTOM_RIGHT_X = 100
BOTTOM_SQUARE_BOTTOM_RIGHT_Y = -100
BOTTOM_SQUARE_BOTTOM_LEFT_X = 0
BOTTOM_SQUARE_BOTTOM_LEFT_Y = -100

turtle.hideturtle()
turtle.penup()

# Начертить самый верхний квадрат
turtle.goto(TOP_SQUARE_BOTTOM_RIGHT_X, TOP_SQUARE_BOTTOM_RIGHT_Y)
turtle.pendown()
turtle.goto(TOP_SQUARE_TOP_RIGHT_X, TOP_SQUARE_TOP_RIGHT_Y)
turtle.goto(TOP_SQUARE_TOP_LEFT_X, TOP_SQUARE_TOP_LEFT_Y)
turtle.goto(TOP_SQUARE_BOTTOM_LEFT_X, TOP_SQUARE_BOTTOM_LEFT_Y)
turtle.goto(TOP_SQUARE_BOTTOM_RIGHT_X, TOP_SQUARE_BOTTOM_RIGHT_Y)
turtle.penup()

# Начертить нижний квадрат
turtle.goto(BOTTOM_SQUARE_BOTTOM_RIGHT_X, BOTTOM_SQUARE_BOTTOM_RIGHT_Y)
turtle.pendown()
turtle.goto(BOTTOM_SQUARE_TOP_RIGHT_X, BOTTOM_SQUARE_TOP_RIGHT_Y)
turtle.goto(BOTTOM_SQUARE_TOP_LEFT_X, BOTTOM_SQUARE_TOP_LEFT_Y)
turtle.goto(BOTTOM_SQUARE_BOTTOM_LEFT_X, BOTTOM_SQUARE_BOTTOM_LEFT_Y)
turtle.goto(BOTTOM_SQUARE_BOTTOM_RIGHT_X, BOTTOM_SQUARE_BOTTOM_RIGHT_Y)
turtle.penup()

# Соединить углы
turtle.goto(BOTTOM_SQUARE_BOTTOM_RIGHT_X, BOTTOM_SQUARE_BOTTOM_RIGHT_Y)
turtle.pendown()
turtle.goto(TOP_SQUARE_TOP_LEFT_X, TOP_SQUARE_TOP_LEFT_Y)
turtle.penup()
turtle.goto(BOTTOM_SQUARE_TOP_RIGHT_X, BOTTOM_SQUARE_TOP_RIGHT_Y)
turtle.pendown()
turtle.goto(TOP_SQUARE_TOP_RIGHT_X, TOP_SQUARE_TOP_RIGHT_Y)
turtle.penup()
turtle.goto(BOTTOM_SQUARE_BOTTOM_LEFT_X, BOTTOM_SQUARE_BOTTOM_LEFT_Y)
turtle.pendown()
turtle.goto(TOP_SQUARE_BOTTOM_LEFT_X, TOP_SQUARE_BOTTOM_LEFT_Y)
'''

#4
'''
import turtle

RADIUS = 100
STARTING_POINT_X = -250
STARTING_POINT_Y = 0
HSHIFT = 125
VSHIFT = 100

# Начертить круг #1
x = STARTING_POINT_X
y = STARTING_POINT_Y
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Начертить круг #2
x += HSHIFT
y -= VSHIFT
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Начертить круг #3
x += HSHIFT
y = 0
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Начертить круг #4
x += HSHIFT
y -= VSHIFT
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Начертить круг #5
x += HSHIFT
y = 0
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)
'''

#5
'''
import turtle

CENTER_X = 0
CENTER_Y = 0
X_AXIS_LENGTH = 200
Y_AXIS_LENGTH = 200
RADIUS = 25
SOUTH = 270
EAST = 0

# Спрятать черепаху и задать скорость анимации.
turtle.hideturtle()
turtle.speed(0)

# Начертить ось X
x = CENTER_X - (X_AXIS_LENGTH / 2)
y = CENTER_Y
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.forward(X_AXIS_LENGTH)

# Начертить ось Y
x = CENTER_X
y = CENTER_Y + (Y_AXIS_LENGTH / 2)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.setheading(SOUTH)
turtle.forward(X_AXIS_LENGTH)

# Начертить центральный круг
x = CENTER_X
y = CENTER_Y - RADIUS
turtle.penup()
turtle.setheading(EAST)
turtle.goto(x, y)
turtle.pendown()
turtle.circle(RADIUS)

# Написать "Север"
x = CENTER_X - 10
y = CENTER_Y + (Y_AXIS_LENGTH / 2)
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("Север")

# Написать "Юг"
x = CENTER_X - 10
y = CENTER_Y - (Y_AXIS_LENGTH / 2) - 10
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("Юг")

# Написать "Запад"
x = CENTER_X - (X_AXIS_LENGTH / 2) - 25
y = CENTER_Y - 7
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("Запад")

# Написать "Восток"
x = CENTER_X + (X_AXIS_LENGTH / 2) + 2
y = CENTER_Y - 7
turtle.penup()
turtle.goto(x, y)
turtle.pendown()
turtle.write("Восток")
'''

#6
'''
import turtle

UPPER_LEFT_X = -100
UPPER_LEFT_Y = 100
UPPER_RIGHT_X = 100
UPPER_RIGHT_Y = 100
LOWER_LEFT_X = -100
LOWER_LEFT_Y = -100
LOWER_RIGHT_X = 100
LOWER_RIGHT_Y = -100
CENTER_X = 0
CENTER_Y = 0
GAP = 20

# Спрятать черепаху и задать скорость анимации.
turtle.hideturtle()
turtle.speed(0)

# Начертить сплошные линии.
turtle.penup()
turtle.goto(UPPER_LEFT_X, UPPER_LEFT_Y)
turtle.pendown()
turtle.goto(LOWER_RIGHT_X, LOWER_RIGHT_Y)
turtle.penup()
turtle.goto(UPPER_RIGHT_X, UPPER_RIGHT_Y)
turtle.pendown()
turtle.goto(LOWER_LEFT_X, LOWER_LEFT_Y)
turtle.penup()
turtle.goto(UPPER_LEFT_X, UPPER_LEFT_Y)
turtle.pendown()
turtle.goto(LOWER_LEFT_X, LOWER_LEFT_Y)
turtle.penup()
turtle.goto(UPPER_RIGHT_X, UPPER_RIGHT_Y)
turtle.pendown()
turtle.goto(LOWER_RIGHT_X, LOWER_RIGHT_Y)

# Начертить вершнюю пунктирную линию.
turtle.penup()
turtle.goto(UPPER_LEFT_X, UPPER_LEFT_Y)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)

# Начертить нижнюю пунктирную линию.
turtle.penup()
turtle.goto(LOWER_LEFT_X, LOWER_LEFT_Y)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)
turtle.pendown()
turtle.forward(GAP)
turtle.penup()
turtle.forward(GAP)

# Начертить точки.
turtle.penup()
turtle.goto(UPPER_LEFT_X, UPPER_LEFT_Y)
turtle.dot()
turtle.goto(UPPER_RIGHT_X, UPPER_RIGHT_Y)
turtle.dot()
turtle.goto(LOWER_LEFT_X, LOWER_LEFT_Y)
turtle.dot()
turtle.goto(LOWER_RIGHT_X, LOWER_RIGHT_Y)
turtle.dot()
turtle.goto(CENTER_X, CENTER_Y)
turtle.dot()
'''