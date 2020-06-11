



class Arm_Claw:
    def __init__(self, xLocation, yLocation):
        self.xAxis = 0
        self.yAxis = 0
        self.zAxis= 0
        self.clawMotor = 0
        self.xLocation = xLocation
        self.yLocation = yLocation
    def move_xAxis(self):
        # checks to see if the value of the xAxis is at the xLocation
        # if not it sets it to it. Which would represent it moving to it.
        if(self.xLocation != self.xAxis):
            self.xAxis = self.xLocation
            print("Moving to correct X Axis")
        else:
            print("X Axis is correct.")
    def move_yAxis(self):
        # checks to see if the value of the yAxis is at the yLocation
        # if not it sets it to it. Which would represent it moving to it.
        if(self.yLocation != self.yAxis):
            self.yAxis = self.yLocation
            print("Moving to correct Y Axis")
        else:
            print("Y Axis is correct.")
    def move_zAxis(self):
        # checks to see if all the items are in the correct places then will lower the claw.
        # max z axis is 1
        if(self.zAxis != 1 and self.xAxis == self.xLocation and self.yAxis == self.yLocation): 
            self.zAxis == 1
            print("Moving to correct Z Axis.") 
        else:
            print("Ensure correct position.")    
    def activate_claw(self):
        # Ensuring that the claw is open before closing.
        self.clawMotor = 0
        if(self.zAxis == 1):
            self.clawMotor = 1
            print("closing Claw")
            # Retracting the claw
            self.zAxis = 0
        else:
            print("Please ensure that the height is correct.")    
    def return_to_start(self):
        self.xAxis = 0
        self.yAxis = 0
        self.zAxis= 0
        if(self.xAxis == 0 and self.yAxis == 0 and self.zAxis == 0):
            self.clawMotor = 0
        print("Returning to start. Opening Claw.")
def main():
    claw = Arm_Claw(3,3)
    claw.move_xAxis()
    claw.move_yAxis()
    claw.move_zAxis()
    claw.activate_claw()
    claw.return_to_start()
        
if(__name__ == "__main__"):
    main()
        
       

        
