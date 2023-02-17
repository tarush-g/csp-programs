def pyramid(length):
    for i in range(length):
        for j in range((2*length+1)):
            if (j<((length-i)-1)) or (j>(length+1+i)) or (j==length):
                print(' ',end='')
            else:
                print('#', end='')
        print('\n')
        

pyramid(int(input('what length for pyramid? ')))
