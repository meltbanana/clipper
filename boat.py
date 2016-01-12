import numpy as np

class Boat:
    def __init__(self, control):
        self.control = control
        self.location = np.array([1, 2])
        self.speed = np.array([1, 0])
        self.sail = np.pi/2
        self.wheel = 0 
    
    def move(self, env):
        pass

def captain(boat):
    boat.speed += 1
    return True

boat = Boat(captain)
print(boat.location, boat.speed)
boat.move(5)
boat.control(boat)
print(boat.location, boat.speed)
