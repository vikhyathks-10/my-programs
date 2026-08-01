class Car:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print(self.brand, self.model, "Started")

    def stop(self):
        print(self.brand, self.model, "Stopped")


car = Car("Toyota", "Fortuner", 2024)

car.start()
car.stop()