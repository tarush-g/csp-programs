import turtle

tim = turtle.Turtle()
tim.speed(10)
tim.color('red')
tim.width(3)
def square(length):
    for i in range(4):
        tim.forward(length)
        tim.left(90)

x=30
for i in range(200):
    tim.left(3)
    square(x)
    x+=3

