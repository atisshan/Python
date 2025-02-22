class Vehicle:
    def __init__(self, make, label):

       self.make=make
       self.label=label

       def start(self):
           return NotImplementedError("Not implemented")
       def stop(self):
           return NotImplementedError("Not implemented")
       
class Car(Vehicle):
           def start(self):

            return f"{self.make}, {self.label}"
           def stop(self):
              return f"{self.make}, {self.label}"
car = Car("Toyota", "Toyota")

print(car.start())
print(car.stop)