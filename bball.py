from graphics import *
import random
HEIGHT = 720
WIDTH = 1270
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'black', 'pink', 'white']
velocities = [-1, 1, -2, 2, -3, 3, -4, 4]
sizes = [ 10,20,30,40]

class BBall(Circle):
    def __init__(self, center, radius, dx, dy, color='black'):
        self.dx=dx
        self.dy=dy
        Circle.__init__(self, center, radius)
        self.setFill(color)

    def transform(self, WIDTH, HEIGHT):
        self.move(self.dx, self.dy)
        center = self.getCenter()
        x = center.getX()
        y = center.getY()

        if x + self.radius >= WIDTH:
            self.dx = -self.dx
        if x - self.radius <= 0:
            self.dx = -self.dx
        if y + self.radius >= HEIGHT:
            self.dy = -self.dy
        if y - self.radius <= 0:
            self.dy = -self.dy
win = GraphWin("window", WIDTH, HEIGHT)
win.setBackground('lightblue')


ballArr = []
for i in range(4):
    x = random.randint(45,WIDTH-45)
    y = random.randint(45,HEIGHT-45)

    center = Point(x, y)

    ballArr.append(BBall(center, random.choice(sizes), random.choice(velocities), random.choice(velocities), random.choice(colors)))

for ball in ballArr:
    ball.draw(win)
    
while True:
   for ball in ballArr:
       ball.transform(WIDTH, HEIGHT)



