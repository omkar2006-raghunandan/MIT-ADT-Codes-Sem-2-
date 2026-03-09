class vehicle:
    def move(self):
        print("vehicle is moving")

class car(vehicle):
    def move(self):
        print("driving on the road")

class bicycle(vehicle):
    def move(self):
        print("Pedal on the metal")

v0 = vehicle()
v1 = car()
v2 = bicycle()

v1.move()
v2.move()