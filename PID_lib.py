import time
import random

class PID():
    def __init__(self,KP,KI,KD,iteration_time):
        self.error_prior = 0
        self.integral = 0
        self.KP = KP
        self.KI = KI
        self.KD = KD
        self.iteration_time = iteration_time
        
        
    def pid_calc(self,desired_value,actual_value):        
        error = desired_value - actual_value
        self.integral = self.integral + (error*self.iteration_time)
        derivative = (error - self.error_prior)/self.iteration_time
        output = self.KP*error + self.KI*self.integral + self.KD*derivative
        self.error_prior = error
        time.sleep(self.iteration_time)   
        return output

if __name__ == '__main__':
    test_pid = PID(1,0.5,0.2,0.1)
    
    
