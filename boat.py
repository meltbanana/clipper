import numpy as np
from vectors import angle, rotate, projection

class Boat:
    def __init__(self):    
        self.location = np.array([0, 0]) 
        self.speed = np.array([0, 0]) 
        self.sail = np.pi/4 
        self.wheel = 0
    
    def move(self, env):      
        

        #physics of forces on sail here
        #src:https://en.wikipedia.org/wiki/Forces_on_sails#Effect_of_coefficients_of_lift_and_drag_on_forces
        #f: (angle between wind and sail) -> (total force on sail)
        # function returns matrix: Matrix * Wind = Total Force
        def force_on_sails_matrix(angle_wind_sail):         
            if angle_wind_sail < np.pi/8:
                lift = 0 
                drag = 0
            else:
                #every ship has different parameters
                #so this is just game model boat 
                #to test control self-education ability
                drag = angle_wind_sail - 0.3
                lift = np.sin(2*angle_wind_sail)

            return np.array([[drag, -lift],
                             [lift, drag]])
            
        #1. rotate
        k_rotate = 0.1 #wheel -> rotate coefficient
        self.speed = rotate(self.speed, (-1) * self.wheel * k_rotate)

        #2. friction
        k_friction = 0.05
        self.speed = self.speed * (1 - k_friction)
        
        #3. acceleration = forces on sails -> projection on boat direction
        k_acceleration = 0.01
        wind_apparent = env.wind - self.speed
        angle_wind_sail = angle(wind_apparent, self.speed) + self.sail
        
        force_on_sail = np.dot(force_on_sails_matrix(angle_wind_sail), wind_apparent)
        self.speed += k_acceleration * projection(force_on_sail, self.speed)
        
        #4. move
        self.location += self.speed
       
