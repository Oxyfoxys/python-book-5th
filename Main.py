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