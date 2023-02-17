class Cat:
    def __init__(self, name, color, age, numYears = 2):
        self.name = name
        self.color = color
        self.age = age
        self.numLives = 9
        self.numYears = numYears
        
    def speak(self):
        print("meow")
        
    def loseLife(self):
        self.numLives -=1
    def __str__(self):
        return "My name is " + self.name + " and I am " + age
        

myCat = Cat('princess', 'gray', 2, 1)
myCat = Cat('daisy', 'red', 2)

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(self.name + " is " + str(self.age) + " years old")

    def roll_over(self):
        print(self.name +" rolled over")

    def sit(self):
        print(self.name + " is sitting")
        
    def chase_ball(self):
        print(self.name + " ran after the ball")


milo = Dog('milo',2)
daisy = Dog('daisy',4)


milo.get_info()
milo.roll_over()
milo.sit()
daisy.get_info()
milo.chase_ball()





