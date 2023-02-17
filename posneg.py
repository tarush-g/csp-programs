num1 = int(input('please enter an integer: '))
num2 = int(input('please enter an integer: '))
boolean = int(input('enter 0 for false and 1 for true: '))
if num1*num2<0 and boolean == 0:
    print("happy")  
elif boolean == 1 and num1<0 and num2<0:
    print("happy")
