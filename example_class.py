# Define a class
class Car:
    def __init__(self, color, speed=0):
        self.color = color      # attribute: color of the car
        self.speed = speed      # attribute: current speed

    def accelerate(self):
        self.speed += 10        # method: increase speed
        print(f"Current speed: {self.speed}km/h")

    def brake(self):
        self.speed -= 10        # method: decrease speed
        print(f"Current speed: {self.speed}km/h")

# Create an object (instance of the Car class)
my_car = Car("red")
my_car.accelerate()   # Output: Current speed: 10km/h
my_car.brake()        # Output: Current speed: 0km/h

# Create another object
your_car = Car("blue", 30)
your_car.accelerate() # Output: Current speed: 40km/h