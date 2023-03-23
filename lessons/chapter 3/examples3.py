'''
3.1 Инструкция if
'''

'''
if balance == 0:
 # Инструкции будут исполнены,
 # только если переменная balance равна 0.

if choice != 5:
 # Инструкции будут исполнены,
 # только если переменная choice не равна 5.
'''

'''
 Programme 3.1
 Эта программа получает три оценки за контрольные работы
 и показывает их средний балл. Она поздравляет пользователя,
 если средний балл высокий.
'''
# Именованная константа HIGH_SCORE содержит значение, которое
# считается высоким баллом.

HIGH_SCORE = 95

# Получить три оценки за контрольные работы
test1 = int(input('Введите оценку 1: '))
test2 = int(input('Введите оценку 2: '))
test3 = int(input('Введите оценку 3: '))

# Расчитать средний балл
average = (test1 + test2 + test3) / 3

# Напечатать средний балл
print('Средний балл составляет: ', average)

# Если средний балл высокий, то
# поздравить пользователя.
if average >= HIGH_SCORE:
    print('Поздравляем!')
    print('Отличный средний балл!')

    '''
    3.2 Инструкция if-esle
    '''
    #Programme 3.2
    # Именованные константы представляют базовые часы
    # и коэффициент сверхурочного времени.
    BASE_HOURS = 40  # Базовые часы в неделю
    OT_MULTIPLIER = 1.5  # Коэффициент сверхурочного времени

    # Получить отработанные часы и почасовую ставку оплаты труда.
    hours = float(input('Введите количество отработанных часов: '))
    pay_rate = float(input('Введите почасовую ставку оплаты труда: '))

    # Рассчитать и показать заработную плату до удержаний.
    if hours > BASE_HOURS:
        # Рассчитать заработную плату до удержаний без сверхурочных.
        # Сначала получить количество отработанных сверхурочных часов.
        overtime_hours = hours - BASE_HOURS

        # Рассчитать оплату за работу в сверхурочное время.
        overtime_pay = overtime_hours * pay_rate * OT_MULTIPLIER

        # Рассчитать заработную плату до удержаний.
        gross_pay = BASE_HOURS * pay_rate + overtime_pay
    else:
        # Рассчитать заработную плату до удержаний.
        gross_pay = hours * pay_rate

    # Показать заработную плату до удержаний.
    print(f'Заработная плата до удержаний составляет: ${gross_pay:,.2f}.')

    '''
    3.3 Сравнение строковых значений
    '''

    '''
     Programme 3.3
     Эта программа сравнивает два строковых значения.
    '''
    # Получить от пользователя пароль.
    password = input('Введите пароль: ')

    # Определить, был ли введен правильный
    # пароль.
    if password == 'prospero':
        print('Пароль принят.')
    else:
        print('Извините, этот пароль неверный.')

    '''
    Programme 3.4
    Эта программа сравнивает строковые значения оператором <.
    '''
    # Получить от пользователя два имени
    name1 = input('Введите фамилию и имя: ')
    name2 = input('Введите еще одну фамилию и имя: ')

    # Показать имена в алфавитном порядке.
    print('Вот имена, ранжированные по алфавиту:')

    if name1 < name2:
        print(name1)
        print(name2)
    else:
        print(name2)
        print(name1)

'''
3.4 Вложенные структуры принятия решения и инструкция if-elif-else
'''

'''
Programme 3.5
Эта программа определяет, удовлетворяет ли
клиент требованиям банка на получение ссуды.
'''

MIN_SALARY = 30000.0  #Минимально допустимая годовая зарплата
MIN_YEARS = 2    #Минимально допустимый стаж на текущем месте работы

# Получить размер годовой заработной платы клиента.
salary = float(input('Введите свой годовой доход: '))

# Получить количество лет на текущем месте работы.
years_on_job = int(input('Введите количество лет ' +
                         'рабочего стажа: '))

# Определить, удовлетворяет ли клиент требованиям.
if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('Ваша ссуда одобрена.')
    else:
        print(f'Вы должны отработать',
              f'не менее {MIN_YEARS}',
              f'лет, чтобы получить одобрение.')
else:
    print(f'Вы должны зарабатывать не менее $',
          f'не менее {MIN_SALARY:,.2f}',
          f'в год, что бы получить одобрение.')

'''
Programme 3.6
 Эта программа получает от пользователя количество баллов
и показывает соответствующий буквенный уровень.
'''

# Именованные константы, представляющие пороги уровней.
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Получить от пользователя баллы за контрольную работу.
score = int(input('Введите свои баллы:'))

# Определить буквенный уровень
if score >= A_SCORE:
    print('Ваш уровень - A.')
else:
    if score >= B_SCORE:
        print('Ваш уровень - B.')
    else:
        if score >= C_SCORE:
            print('Ваш уровень - C.')
        else:
            if score >= D_SCORE:
                print('Ваш уровень - D.')
            else:
                print('Ваш уровень - F.')

'''
3.5 Логические операторы
'''

'''
Programme 3.7
Эта программа определяет, удовлетворяет ли
клиент требованием банка на получение ссуды
'''

MIN_SALARY = 30000.0
MIN_YEARS = 2

#Получить размер годового дохода клиента
salary = float(input('Введите свой годовой доход: '))

#Получить количество лет на текущем месте работы
years_on_job = int(input('Введите количество лет' + 'рабочего стажа: '))

#Определить, удовлетворяет ли клиент требованиям
if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('Ваша ссуда одобрена')
else:
    print('Ваша ссуда не одобрена')

'''
Programme 3.8
Эта программа определяет, удовлетворяет ли
клиент требованием банка на получение ссуды
'''

MIN_SALARY = 30000.0
MIN_YEARS = 2

#Получить размер годового дохода клиента
salary = float(input('Введите свой годовой доход: '))

#Получить количество лет на текущем месте работы
years_on_job = int(input('Введите количество лет' + 'рабочего стажа: '))

#Определить, удовлетворяет ли клиент требованиям
if salary >= MIN_SALARY or years_on_job >= MIN_YEARS:
    print('Ваша ссуда одобрена')
else:
    print('Ваша ссуда не одобрена')

'''
3.7 Черепашья графика: определение состояния черепахи
'''

'''
Programme 3.9
Игра "Порази цель"
'''
import turtle

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
TARGET_LLEFT_X = 100
TARGET_LLEFT_Y = 250
TARGET_WIDTH = 25
FORCE_FACTOR = 30
PROJECTILE_SPEED = 1
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

turtle.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

turtle.hideturtle()
turtle.speed(0)
turtle.penup()
turtle.goto(TARGET_LLEFT_X, TARGET_LLEFT_Y)
turtle.pendown()
turtle.setheading(EAST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(NORTH)
turtle.forward(TARGET_WIDTH)
turtle.setheading(WEST)
turtle.forward(TARGET_WIDTH)
turtle.setheading(SOUTH)
turtle.forward(TARGET_WIDTH)
turtle.penup()

turtle.goto(0, 0)
turtle.setheading(EAST)
turtle.showturtle()
turtle.speed(PROJECTILE_SPEED)

angle = float(input("Введите угол выстрела снаряда: "))
force = float(input("Введите пусковую(1-10): "))

distance = force * FORCE_FACTOR

turtle.setheading(angle)

turtle.pendown()
turtle.forward(distance)

if (turtle.xcor() >= TARGET_LLEFT_X and
    turtle.xcor() <= (TARGET_LLEFT_X + TARGET_WIDTH) and
    turtle.ycor() >= TARGET_LLEFT_Y and
    turtle.ycor() <= (TARGET_LLEFT_Y + TARGET_WIDTH)):
        print('Цель поражена!')
else:
        print('Вы промахнулись')




