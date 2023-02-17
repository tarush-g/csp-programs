from graphics import *
HEIGHT = 720
WIDTH = 1270


# instantiate window
win = GraphWin("window", WIDTH, HEIGHT)
win.setBackground('lightblue')


# instantiate a point with (x, y) coordinates of (160, 120)
center = Point(WIDTH//2, HEIGHT//2)
radius = 20


# instantiate ball with center at (160, 120)
ball = Circle(center, radius)



# fill the circle with black
ball.setFill("BLACK")

# draw the circle to the window
ball.draw(win)




xvelocity = 0.1
yvelocity = 0.05

    


while True:
    # move ball along x-axis
    ball.move(xvelocity, yvelocity)

    # get x-coordinate of circle
    #TODO get the ball to bounce off the right and then left edge of the window
    #HINT - the xBall is the value you need to be using to make a decision
    centerBall = ball.getCenter()
    xBall = centerBall.getX()
    yBall = centerBall.getY()

    
    if xBall + radius >= WIDTH or xBall - radius <= 0:
        xvelocity = -xvelocity
    if yBall + radius >= HEIGHT or yBall - radius <= 0:
        yvelocity = -yvelocity

        
    
 




    # if there is a mouse click on window, close the window
    if win.checkMouse():
        win.close()
        break


exit(0)
