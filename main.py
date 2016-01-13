#main simulation file
import numpy as np
from boat import Boat


class env:
    pass
env.wind = np.array([1, 0])

def control(boat):
    boat.speed += 1
    return True


boat = Boat()

for t in range(10):
    control(boat)
    boat.move(env)
    print(boat.speed)
