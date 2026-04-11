class Car:
    def __init__(self):
        # encapsulation: data (variables) and methods are bundled inside the class
        self.acc = False     # accelerator state (data)
        self.brake = False   # brake state (data)
        self.clutch = False  # clutch state (data)

    def start(self):
        # encapsulation: method controls how internal data is modified
        self.clutch = True   # modifying internal state
        self.acc = True      # modifying internal state
        print("car started...")  # behavior of the object

car1 = Car()   # object created → data is encapsulated inside car1
car1.start()   # accessing behavior through method, not directly changing variables
