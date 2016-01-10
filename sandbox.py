
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

#need update here!
# 1. function f(angle) -> matrix
# 2. matrix*Va = total_force
# 3. projection(total_force, Vb) ~ boat acceleration

def get_total_force(angle_wind_sail, Va):
    drag = Va
    lift = rotate(Va, np.pi/2)
    if angle_wind_sail < np.pi/8:
        lift *= 0 
        drag *= 0
    else:
        drag *= angle_wind_sail
        lift *= np.sin(2*angle_wind_sail)

    return lift + drag


print(get_total_force(np.pi/3, np.array([1,0])))

    
    
