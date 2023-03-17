import turtle
# test
from stars import orion


def other():



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

#2

#3

#4

#5

#6

#7

#8

#9

#10


#11


#12


#13


#14


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