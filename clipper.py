#0. project clipper
import numpy as np

#1. useful functions

def length(vector):
    return np.sqrt(vector.dot(vector))

def angle(Vx, Vy):
    return np.arccos(np.dot(Vx, Vy)/(length(Vx)*length(Vy)))

def rotate(vector, angle):
    rotation_matrix = np.array([[np.cos(angle), - np.sin(angle)],
                               [np.sin(angle), np.cos(angle)]])
    return np.dot(rotation_matrix, vector)

def projection(Vx, Vy):
    return Vx * cos(angle(Vx, Vy))

#2. data structure

#environment
env = {
    'wind': np.array([0, 1]) #absolute coordinates
    }

#boat state
state = {
    'location': np.array([0, 0]), #absolute coordinates
    'speed': np.array([-1, -1]), #absolute coordinates. also =boat direction 
    'sail': np.pi/4, #angle in relative boat coordinates: back = 0
    'wheel': 0 #angle in relative boat coordinates: back = 0
    }

#3. adaptive control machine

def control(env, state):
    print(env, state)
    angle_gradus = input('set new sail, captain (None = keep course):')
    if not angle_gradus == '':
        angle_gradus = float(angle_gradus)
        state['sail'] = np.pi * angle_gradus/180

    angle_gradus = input('set new wheel, captain (None = keep course):')
    if not angle_gradus == '':
        angle_gradus = float(angle_gradus)
        state['wheel'] = np.pi * angle_gradus/180
    return state

#4. physics of imitation

def move(env, state):

    def drive_boat(Vb, Vw, alpha):
        kForce = 0.1 #wind -> acceleration coefficient mass of boat + all physics     
        friction = 0.01 # V' ~ friction * V
        return -friction*Vb

    def rotate_boat(Vb, angle_wheel):
        kRotate = 0.1 #wheel -> rotate coefficient
        return rotate(Vb, -angle_wheel * kRotate)

       
    state['speed'] = drive_boat(state['speed'], env['wind'], state['sail'])
    state['speed'] = rotate_boat(state['speed'], state['wheel'])
    
    state['location'] = state['location'] + state['speed']

    return state

#5. simultation

for t in range(0, 10**6):
    if t%10==0:
        state = control(env, state)

    state = move(env, state)

