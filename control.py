class PDController:
    #initialising the pd controller with Kp and Kd
    def _init_(self,Kp = 0.15,Kd = 0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0

    def compute_control(self, reference, output):
        """
        Compute the control action u[t] based on the PD controller formula:
        u[t] = KP * e[t] + KD * (e[t] - e[t-1])
        
        :param reference: The desired reference value r[t]
        :param output: The current output value y[t]
        :return: The control action u[t] 
        """
        error = reference - output
        proportional = self.Kp * error
        derivative = self.Kd*(error - self.prev_error)
        self.prev_error = error
        controller_action = proportional + derivative
        return controller_action 
