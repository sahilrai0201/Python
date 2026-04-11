class Car:
    def __init__(self):
        # initializing the state of car components
        self.acc = False     # accelerator is initially OFF
        self.brake = False   # brake is initially OFF
        self.clutch = False  # clutch is initially OFF

    def start(self):
        # abstraction: user only calls start(), internal details are handled here
        self.clutch = True   # clutch is pressed
        self.acc = True      # accelerator is pressed
        print("car started...")  # car starts

car1 = Car()   # creating a Car object → constructor initializes all values
car1.start()   # calling start() method → starts the car without exposing internal logic       