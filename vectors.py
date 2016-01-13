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
    return Vx * np.cos(angle(Vx, Vy))
