
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
def get_total_force(angle_sail, Va):
    if angle_sail < np.pi/8:
        lift, drag = 0, 0
    else:
        drag = angle_sail
        lift = sin(2*angle_sail)

    return = (lift + drag) * Va


