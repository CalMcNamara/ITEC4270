#model 2 

import random
class Robot_Sensor:
    def __init__(self):
        # setting starting posistions for the robot and the end goal. 
        self.robot_x = 0
        self.robot_y = 0
        self.rotation = 0
        self.distance_x = random.randint(10,15)//2
        self.distance_y = random.randint(10,15)//2
    
    # move functions updates the distance it is from the object. 
    def robot_movex_pos(self):
        self.robot_x = self.robot_x + 1
        print("Moving Robot 1 unit forward on the X axis Current position: " + str(self.robot_x))
        self.update_distance(1,0)
        
    
    def robot_movex_neg(self):
        self.robot_x = self.robot_x - 1
        print("Moving Robot 1 unit back on the X axis Current Position: " + str(self.robot_x))
        self.update_distance(-1,0)
        

    def robot_movey_pos(self):
        self.robot_y = self.robot_y + 1
        print("Moving Robot 1 unit forward on the y axis Current position: " + str(self.robot_y))
        self.update_distance(0,1)
         

    def robot_movey_neg(self):
        self.robot_y = self.robot_y - 1
        print("Moving Robot 1 unit back on the y axis Current Position: " + str(self.robot_y))
        self.update_distance(0,-1)
         
    # rotate function take in the angle in which the robot should rotate to. 
    def rotate(self, rotate ):
        self.rotation = rotate
        print("Current Rotation is: " + str(rotate))
    
    def update_distance(self, distance_x, distance_y):
        self.distance_x = self.distance_x - distance_x
        self.distance_y = self.distance_y - distance_y
        print("Distance X Updated to: " + str(self.robot_x))
        print("Distance Y Updated to: " + str(self.robot_y)) 
    
    def distance_between(self):
        return(self.distance_x,self.distance_y)

    # navigation logic 
    def navigate(self, distance_x , distance_y):
        
        if(distance_x < self.distance_x):
            while(distance_x < self.distance_x):
                self.rotate(90)
                self.robot_movex_pos()
                self.rotate(0)
                print("Moving")
                print(self.distance_between()) 

        if(distance_x > self.distance_x):
            while(distance_x > self.distance_x):
                self.rotate(270)
                self.robot_movex_neg()
                self.rotate(0)
                print("Moving")
                print(self.distance_between()) 

        if(distance_y < self.distance_y):
            while(distance_y < self.distance_y):
                self.rotate(0)
                self.robot_movey_pos()
                print("Moving")
                print(self.distance_between()) 

        if(distance_y > self.distance_y):
            while(distance_y > self.distance_y):
                self.rotate(180)
                self.robot_movey_pos()
                print("Moving")
                self.rotate(0)
                print(self.distance_between()) 

robot_sens = Robot_Sensor()
robot_sens.navigate(robot_sens.robot_x,robot_sens.robot_y)