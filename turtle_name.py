import turtle
import string
from P2Alpha import *

tim = turtle.Turtle()
tim.speed(10)
tim.width(3)

def print_word(trtl, x, y, word):
    coord = x
    for letter in word.upper():
        globals()[letter](trtl, coord, y)
        coord +=100

