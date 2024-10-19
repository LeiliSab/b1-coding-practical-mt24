class PDController:
    #initialising the pd controller with Kp and Kd
    def _init_(self,Kp = 0.15,Kd = 0.6):
        self.Kp = Kp
        self.Kd = Kd
        self.prev_error = 0
        