def pyramid(length):
    length+=1
    for i in range(length):
        print((' '*(length-(i+1)))+('#'*i)+' '+('#'*i))

pyramid(int(input('what length for pyramid? ')))
