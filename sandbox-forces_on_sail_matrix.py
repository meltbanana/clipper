import numpy as np
import matplotlib.pyplot as plt
import vectors as v

def draw_vectors(xy_src):
    lst = [[0, 0, x, y] for x,y in xy_src]    
    soa =np.array(lst) 
    X,Y,U,V = zip(*soa)
    plt.figure()
    ax = plt.gca()
    qv = ax.quiver(X,Y,U,V,angles='xy',scale_units='xy',scale=1)
    ax.set_xlim([-2,2])
    ax.set_ylim([-2,2])
    plt.draw()
    plt.show()
    return True
    

#draw_vectors([np.array([1,5]), (2, 3)])

def force_on_sails_matrix(wind, sail):         
    
    #get angle between wind and sail
    orientation = np.sign(np.cross(wind, sail))    
    angle = v.angle(wind, sail)
    if np.pi/2 < angle <= np.pi:
       angle = abs(np.pi - angle)
       orientation *= -1
       
    #get forces on sail (for 0 <= angle <= pi/2)
    drag = np.exp(abs(angle)/2) - 1
    lift = -orientation * np.exp(-20*(angle - 0.6)**2)

    return np.array([[drag, -lift], [lift, drag]])

wind_apparent = np.array([1, 0])  
speed = np.array([1, 0.5])
sail_angle = np.pi/180 * (110)

total_matrix = force_on_sails_matrix(wind_apparent, v.rotate(speed, sail_angle))
total = np.dot(total_matrix, wind)

print('wind=', wind)
draw_vectors([wind, speed, total])
