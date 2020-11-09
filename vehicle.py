
# Exercise Question 1: Create a Vehicle class with max_speed and 
# mileage instance attributes

class Vehicle:
    """A vehicle."""

    def __init__(self, name, max_speed, mileage):
        """Initializing."""

        self.name = name 
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        """Returns the seating capacity of a vehicle."""

        s = f"The seating capacity of {self.name} is {capacity} passengers."

        return s

    
class Car(Vehicle):
    """A car."""
    pass

class Bus(Vehicle):
    """A bus."""

    def seating_capacity(self, capacity=50):
        """A bus's capacity."""

        return super().seating_capacity(capacity=50)
    


Honda = Vehicle("Ivy", 300, 10000)
print(Honda.max_speed, Honda.mileage)


Robs_car = Car("Carson", 200, 130000)
print("Vehicle Name:", Robs_car.name, "Speed:", Robs_car.max_speed, "Mileage:", Robs_car.mileage)


School_bus = Bus("School Volvo", 180, 12)
print(School_bus.seating_capacity())