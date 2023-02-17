import turtle

tim = turtle.Turtle()
def A(trt1, x,y):
    trt1.pu()
    trt1.goto(x,y)
    trt1.pd()
    trt1.goto(x+0,y+120)
    trt1.goto(x+60,y+120)
    trt1.goto(x+60,y+80)
    trt1.goto(x+0,y+80)
    trt1.goto(x+60,y+80)
    trt1.goto(x+60,y+0)

def J(trtl, x,y):
    trtl.pu()
    trtl.goto(x,y)
    trtl.pd()
    trtl.goto(x+0,y+20)
    trtl.goto(x,y)
    trtl.goto(x+30,y+0)
    trtl.goto(x+30,y+120)
    trtl.goto(x+0,y+120)
    trtl.goto(x+60,y+120)


J(tim, 0,0)

def X(trt1, x,y):
    trt1.pu()
    trt1.goto(x,y)
    trt1.pd()
    trt1.goto(x+60,y+120)
    trt1.goto(x+30,y+60)
    trt1.goto(x+60,y+0)
    trt1.goto(x+0,y+120)
    
X(tim, 0,150)

    
