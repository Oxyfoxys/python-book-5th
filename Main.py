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

#3

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