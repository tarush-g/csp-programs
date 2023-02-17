from graphics import *
import time
import random
HEIGHT = 720
WIDTH = 1270
score = [0,0]
negatives = [1, -1]
# instantiate window
win = GraphWin("window", WIDTH, HEIGHT)
win.setBackground('lightblue')


# instantiate a point with (x, y) coordinates of (160, 120)
center = Point(WIDTH//2, HEIGHT//2)
p1point1 = Point(1240, (HEIGHT//2)-75)
p1point2 = Point(1260, (HEIGHT//2)+75)
p2point1 = Point(10, (HEIGHT//2)-75)
p2point2 = Point(30, (HEIGHT//2)+75)
textpoint = Point(WIDTH//2, HEIGHT-50)
radius = 20


# instantiate ball with center at (160, 120)
ball = Circle(center, radius)
paddle1 = Rectangle(p1point1, p1point2)
paddle2 = Rectangle(p2point1, p2point2)
score_text = Text(textpoint, f"Score: {score[1]}-{score[0]}")


# fill the circle with black
ball.setFill("BLACK")
paddle1.setFill("BLACK")
paddle2.setFill("BLACK")
score_text.setFill("BLACK")
score_text.setSize(15)

# draw the circle to the window
ball.draw(win)
paddle1.draw(win)
paddle2.draw(win)
score_text.draw(win)


xvelocity = round(random.uniform(0.1, 0.2), 2)*random.choice(negatives)
yvelocity = round(random.uniform(0.1, 0.2), 2)*random.choice(negatives)


def paddleMove(paddle1, paddle2):
    user_event = win.checkKey()
    if user_event == "w":
        paddle1.move(0, -20)
    if user_event == "s":
        paddle1.move(0, 20)
    if user_event == "Up":
        paddle2.move(0, -20)
    if user_event == "Down":
        paddle2.move(0, 20)
    

while True:
    paddleMove(paddle2, paddle1)
    # move ball along x-axis
    ball.move(xvelocity, yvelocity)

    # get x-coordinate of circle
    #TODO get the ball to bounce off the right and then left edge of the window
    #HINT - the xBall is the value you need to be using to make a decision
    centerBall = ball.getCenter()
    xBall = centerBall.getX()
    yBall = centerBall.getY()

    '''
    if xBall + radius >= WIDTH or xBall - radius <= 0:
        xvelocity = -xvelocity
    '''
    if yBall + radius >= HEIGHT or yBall - radius <= 0:
        yvelocity = -yvelocity
    
    if xBall-radius<=30 and paddle2.p1.y<=yBall-radius and yBall+radius<=paddle2.p2.y:
        xvelocity = -xvelocity
    if xBall+radius>=1240 and paddle1.p1.y<=yBall-radius and yBall+radius<=paddle1.p2.y:
        xvelocity = -xvelocity
    if xBall+radius >= WIDTH:
        score[1]+=1
        score_text.setText(f"Score: {score[1]}-{score[0]}")
        ball.move((center.x)-xBall, (center.y)-yBall)
        xvelocity = round(random.uniform(0.1, 0.2), 2)*random.choice(negatives)
        yvelocity = round(random.uniform(0.1, 0.2), 2)*random.choice(negatives)
        time.sleep(0.5)
    if xBall-radius <= 0:
        score[0]+=1
        score_text.setText(f"Score: {score[1]}-{score[0]}")
        ball.move((center.x)-xBall, (center.y)-yBall)
        xvelocity = round(random.uniform(0.1, 0.2), 2)*random.choice(negatives)
        yvelocity = round(random.uniform(0.1, 0.2), 2)*random.choice(negatives)


        time.sleep(0.5)



    # if there is a mouse click on window, close the window
    if win.checkMouse():
        win.close()
        break


exit(0)
