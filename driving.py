notvalidinput=True
while notvalidinput == True:
    try:
        x=int(input('x coordinate: '))
        y=int(input('y coordinate: '))
        notvalidinput=False
    except:
        print('not valid. enter integer')

if x>0 and y>0:
    print('quadrant 1')
elif x<0 and y>0:
    print('quadrant 2')
elif x<0 and y<0:
    print('quadrant 3')
elif x>0 and y<0:
    print('quadrant 4')
elif x==0 and y==0:
    print('origin')
