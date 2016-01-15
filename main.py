#main simulation file
import numpy as np
from boat import Boat

class env:
    pass
env.wind = np.array([10, 0])

def control(boat):
 
    print(boat)
    
    sail = input('set sail, captain:')
    try:
        boat.sail = int(sail) * np.pi/ 180   
    except:
        if sail == 'exit':
            print('\n\033[31m' + 'game over' + '\033[30m')
            exit()
    
    wheel = input('set wheel, captain:')
    try:
        boat.wheel = int(wheel) * np.pi/ 180   
    except:
        pass
    
    return True


boat = Boat()

for t in range(1000):
    if t%10 == 0: 
        print('\n\033[31m' + '--- control session --- (print exit to exit)---'+'\033[30m')
        print('wind = ', env.wind, ', apparent wind =', env.wind - boat.speed)
        control(boat)
    boat.move(env)
