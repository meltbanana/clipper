
import numpy as np

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


#in apparent wind relative coordinates
def sail_forces_matrix(angle_wind_sail):
    if angle_wind_sail < np.pi/8:
        lift = 0 
        drag = 0
    else:
        drag = angle_wind_sail/np.pi
        lift = np.sin(2*angle_wind_sail)

    return np.array([[drag, -lift],
                    [lift, drag]])


Va = [1,1]

for i in range(1,9):
    print('pi/%i'%i, np.dot(sail_forces_matrix(np.pi/i), Va))
