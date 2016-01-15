import numpy as np
import vectors as v

class Boat:
    def __init__(self):    
        self.location = np.array([0, 0]) 
        self.speed = np.array([0.1, 0]) 
        self.sail = np.pi/2 
        self.wheel = 0
    
    def __str__(self):
        p = 3
        np.set_printoptions(precision=p, suppress=True)     
        return 'location='+str(self.location)+', '+\
                'speed='+str(self.speed)+', '+\
                'sail='+str(round(self.sail, p))+', '+\
                'wheel='+str(round(self.wheel, p))
    
    def move(self, env):      

        #physics of forces on sail here
        #src:https://en.wikipedia.org/wiki/Forces_on_sails#Effect_of_coefficients_of_lift_and_drag_on_forces
        #f: (angle between wind and sail) -> (total force on sail)
        # function returns matrix: Matrix * Wind = Total Force
        def force_on_sails_matrix(wind, sail):         
            #1. get angle between wind and sail
            orientation = np.sign(np.cross(wind, sail))    
            angle = v.angle(wind, sail)
            if np.pi/2 < angle <= np.pi:
               angle = abs(np.pi - angle)
               orientation *= -1
               
            #2. get forces on sail (for 0 <= angle <= pi/2)
            #every ship has different parameters
            #so this is just game model boat 
            #to test control self-education ability
            drag = np.exp(abs(angle)/2) - 1
            lift = -orientation * np.exp(-20*(angle - 0.6)**2)
        
            return np.array([[drag, -lift], [lift, drag]])

            
        #1. rotation
        k_rotate = 0.05 * v.length(self.speed) #wheel -> rotate coefficient
        self.speed = v.rotate(self.speed, (-1) * self.wheel * k_rotate)

        #2. friction
        k_friction = 0.05
        self.speed = self.speed * (1 - k_friction)
        
        #3. acceleration = forces on sails -> projection on boat direction
        k_acceleration = 0.1
        wind_apparent = env.wind - self.speed
        total_force_matrix = force_on_sails_matrix(wind_apparent, v.rotate(self.speed, self.sail))
        total_force = np.dot(total_force_matrix, wind_apparent)
        self.speed += k_acceleration * v.projection(total_force, self.speed)
      
        #4. move
        self.location += self.speed
       
