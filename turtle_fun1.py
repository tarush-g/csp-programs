from turtle import Turtle
import random
from P2Alpha import *
import string

tim = Turtle()
tim.speed(5)
tim.width(4)

def print_word(trtl, x, y, word):
    coord = x
    for letter in word.upper():
        if letter == ' ':
            coord+=100
            continue
        if letter == '/':
            coord=x
            y-= 140
            continue
        globals()[letter](trtl, coord, y)
        coord +=100

tim.penup()
tim.goto(-150, -150)
tim.pendown()
tim.circle(20)
tim.right(90)
tim.fd(10)

tim.left(30)
tim.fd(60)
tim.right(180)
tim.fd(60)
tim.left(120)
tim.fd(60)
tim.right(180)
tim.fd(60)
tim.right(150)

tim.fd(70)
tim.left(30)
tim.fd(60)
tim.right(180)
tim.fd(60)
tim.left(120)
tim.fd(60)
tim.right(180)
tim.fd(60)
tim.right(150)

tim.pu()
tim.goto(-520, 200)
tim.pd()
tim.right(180)
tim.fd(130)
tim.circle(-10, extent=90)
tim.fd(710)
tim.circle(-10, extent=90)
tim.fd(280)
tim.circle(-10, extent=90)
tim.fd(200)
tim.left(50)
tim.fd(175)
tim.right(160)
tim.fd(142.66)
tim.left(110)
tim.fd(446.30)
tim.circle(-10, extent=90)
tim.goto(-520, 200)




words = input('what do you want to say? ')
color = input('what color do you want? ')
tim.pencolor(color)
print_word(tim, -500, 200, words)


