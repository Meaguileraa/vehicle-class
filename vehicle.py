
# Exercise Question 1: Create a Vehicle class with max_speed and 
# mileage instance attributes

class Vehicle:
    """A vehicle."""

    def __init__(self, max_speed, mileage):
        """Initializing."""

        self.max_speed = max_speed
        self.mileage = mileage

Honda = Vehicle(300, 10000)
print(Honda.max_speed, Honda.mileage)