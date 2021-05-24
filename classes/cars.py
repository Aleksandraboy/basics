# 03/28/21 Object-oriented Programming concepts

class Car(): # all class names should start with the capital letter(upper case)
    ''' this class describes model of the car'''

    def __init__(self, model, color, brand):
        '''this is the constructor, with required parameters'''
        self.modelofthecar = model
        self.colorofthecar = color
        self.brandofthecar = brand

    def drive(self):
        '''driving action'''# it's not nesessery
        print(f"You are driving the car! isn't it awesame")

    def do_somthing(self):
        print("I want to do somthing....")
        print("Let me drive this car")
        self.drive()
        # motor = Motorcycle()
        # motor.drive()

    def get_description(self):
        ''' '''
        print(f"Model of the car: {self.modelofthecar}")
        print(f"Color of the car: {self.colorofthecar}")
        print(f"Brand of the car: {self.brandofthecar}")

# mycar = Car() # car is the class, mycar is an object, in this line  we are creating instance of the (intanstiation)
mycar = Car("3", "red", "BMW")
yourcar = Car("345", "green", "Acura")

mycar.get_description()
mycar.drive()

yourcar.get_description()
yourcar.drive()

# yourcar.drive()
# yourcar.do_something()
# mycar.drive()
