import turtle
bob = turtle.Turtle()

number1 = 90
number2 = 90
number3 = 5

def drawSquare(num1, num2):
    bob.fd(num1)
    bob.lt(90)
    bob.fd(num2)
    bob.lt(90)
    bob.fd(num1)
    bob.lt(90)
    bob.fd(num2)
    bob.lt(90)

#drawSquare(number1,number2)


def drawPolygon(num1, num2, num3):

    num3 = 360 / num3
    bob.fd(num1)
    bob.lt(num3)
    bob.fd(num2)

    bob.fd(num1)
    bob.lt(num3)
    bob.fd(num2)

    bob.fd(num1)
    bob.lt(num3)
    bob.fd(num2)

    bob.fd(num1)
    bob.lt(num3)
    bob.fd(num2)

    bob.fd(num1)
    bob.lt(num3)
    bob.fd(num2)


drawPolygon(number1, number2, number3)

turtle.mainloop()
