def task_1():
    '''
    Пример ввода текста
    '''
    print('Aleks lutic')
    print('Эшвиль, Северная Каролина 28899')
    print('89234657823')
    print('профильная')


def task_2():
    total_amount = float(input('Введите сумму общего объема продаж:'))
    pta = 0.23  # процент от общей суммы
    sn = total_amount / 100 * pta
    print(sn)


def task_3():
    total_number = float(input('Введите общее количество квадратных метров:'))
    ackr = 4046.86
    na = total_number / 4047 * ackr
    print(na)



def task_4():
    product1 = float(input('Введите цену товара 1: '))

    product2 = float(input('Введите цену товара 2: '))

    product3 = float(input('Введите цену товара 3: '))

    product4 = float(input('Введите цену товара 4: '))

    product5 = float(input('Введите цену товара 5: '))

    subTotal = (product1 + product2 + product3 + product4 + product5)

    salesTax = subTotal * 0.07

    total = subTotal + salesTax

    print('sub total: ', format(subTotal, ',.2f'))
    print('sales tax: ', format(salesTax, ',.2f'))



def task_5():
    speed = 70
    distance = speed * 6
    distance2 = speed * 10
    distance3 = speed * 15
    print(distance, distance2, distance3)



def task_6():
    amount = float(input("Введите общую сумму покупки: "))

    federal_tax = amount * 0.05
    regional_tax = amount * 0.025

    totalSale = (amount + federal_tax + regional_tax)

    print('Сумма покупки :', format(amount, ',.2f'))
    print('Сумма федерального налога с продажи: ', format(federal_tax, ',.2f'))
    print('Сумма регионального налога с продажи: ', format(regional_tax, ',.2f'))
    print('Итоговая сумма :', format(totalSale, ',.2f'))



def task_7():
    # расход = пройденные километры / расход бензина в литрах
    # kilometers_per_litre = kilometers / litres
    kilometers = float(input('Введите пройденные километры: '))

    litres = float(input('Введите литры потребленного топлива: '))

    kilometers_per_litre = kilometers / litres

    print('Вы использовали', format(kilometers_per_litre, '.2f'), 'литров на километр')


def task_8():
    TAX_RATE = 0.07  # налоговая ставка
    TIP_RATE = 0.18  # ставка чаевых

    food = float(input('Введите стоимость еды: '))

    tip = food * TIP_RATE

    tax = food * TAX_RATE

    total = food + tip + tax  # итоговая сумма

    print('Чаевые: $', format(tip, '.2f'))
    print('Налог: $', format(tax, '.2f'))
    print('Итоговая сумма: $', format(total, '.2f'))



def task_9():
    celsius = float(input('Введите температуру по шкале Цельсия: '))

    fahrenheit = (9 / 5) * celsius + 32

    print('Она равна', format(fahrenheit, '.2f'), 'градусам по Фаренгейту')


def task_10():
    COOKIES_RECIPE = 48
    SUGAR_RECIPE = 1.5
    BUTTER_RECIPE = 1
    FLOUR_RECIPE = 2.75

    cookies = float(input("Введите количество булочек: "))  # количество булочек

    sugar = (cookies * SUGAR_RECIPE) / COOKIES_RECIPE  # стаканы воды

    butter = (cookies * BUTTER_RECIPE) / COOKIES_RECIPE  # стаканы масла

    flour = (cookies * FLOUR_RECIPE) / COOKIES_RECIPE  # стаканы муки

    print("Чтобы изготовить", cookies, "булочек, вам понадобятся:")
    print(format(sugar, '.2f'), "стаканов сахара")
    print(format(butter, '.2f'), "стаканов масла")
    print(format(flour, '.2f'), "стаканов муки")

def task_11():
    men = int(input('Введите количество учащихся мужского пола: '))
    women = int(input('Введите количество учащихся женского пола: '))

    total = men + women

    percentMen = men / total

    percentWomen = women / total

    print('Юноши: ', format(percentMen, '.2f'), '%')
    print('Девушки: ', format(percentWomen, '.2f'), '%')


def task_12():
    COMMISSION_RATE = 0.03
    NUM_SHARES = 2000
    PURCHASE_PRICE = 40.0
    SELLING_PRICE = 42.75

    amountPaidForStock = 0.0  # Сумма, выплаченная за акции
    purchaseCommission = 0.0  # Комиссия, уплаченная за покупку акций
    totalPaid = 0.0  # Итоговая уплаченная сумма
    stockSoldFor = 0.0  # Сумма, за которую акции были проданы
    sellingCommission = 0.0  # Комиссия, уплаченная за продажу акций
    totalReceived = 0.0  # Итоговая полученная сумма
    profitOrLoss = 0.0  # Сумма дохода или убытка

    amountPaidForStock = NUM_SHARES * PURCHASE_PRICE  # Вычислить сумму, которую Джо уплатил за акции, не включая комиссию.

    purchaseCommission = COMMISSION_RATE * amountPaidForStock  # Вычислить сумму комиссию, которую Джо уплатил брокеру при покупке акций.

    totalPaid = amountPaidForStock + purchaseCommission  # Вычислить общую сумму, которую Джо уплатил

    stockSoldFor = NUM_SHARES * SELLING_PRICE  # Вычислить сумму, за которую Джо продал акции.

    sellingCommission = COMMISSION_RATE * stockSoldFor  # Вычислить сумму комиссии, которую Джо уплатил брокеру

    totalReceived = stockSoldFor - sellingCommission  # Вычислить сумму денег, оставшихся после того, как Джо заплатил брокеру

    profitOrLoss = totalReceived - totalPaid  # Вычислить сумму дохода или убытка

    print('Сумма, уплаченная за акции: $', format(amountPaidForStock, '.2f'))
    print('Комиссия, уплаченная при покупке: $', format(purchaseCommission, '.2f'))
    print('Сумма, вырученная от продажи акций: $', format(stockSoldFor, '.2f'))
    print('Комиссия, уплаченная при продаже: $', format(sellingCommission, '.2f'))
    print('Доход (или убыток, если число отрицательное): $', format(profitOrLoss, '.2f'))


def task_13():
    print('Введите длину гряды в метрах: ', end='')
    R = float(input())

    print('Введите объем пространства в метрах, используемого под трельяжные концевые опоры: ', end='')
    E = float(input())

    print('Введите расстояние в метрах между каждой лозой: ', end='')
    S = float(input())

    V = (R - 2 * E) / S

    print('У вас достаточно места для', V, 'виноградных лоз.')


def task_14():
    print('Введите начальный остаток основного счета: ', end='')
    p = float(input())

    print('Введите годовую ставку процента: ', end='')
    r = float(input())

    print('Сколько раз в году начисляется сложный процентный доход? ', end='')
    n = int(input())

    print('Сколько лет этот счет будет получать процентные начисления? ', end='')
    t = int(input())

    r = r / 100

    a = p * (1 + float(r) / n) ** (n * t)

    print('В конце периода из', t, 'лет у вас будет $', format(a, ',.2f'))


if __name__ == '__main__':
    print(task_1.__doc__)
    task_1()
    # task_2()
    # task_3()
    # task_4()
    # task_5()
    # task_6()
    # task_7()
    # task_8()
    # task_9()
    # task_10()
    # task_11()
    # task_12()
    # task_13()
    # task_14()
