class PDController:
    #initialising the pd controller with Kp and Kd
    def __init__(self, Kp = 0.15, Kd = 0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0

    def compute_control(self, reference, output):
        
        error = reference - output
        proportional = self.Kp * error
        derivative = self.Kd*(error - self.prev_error)
        self.prev_error = error
        controller_action = proportional + derivative
        return controller_action 
