import random

# model 1 
class Robot_GPS:
    def __init__(self):
    # setting the robot start position to (0,0)
        self.robot_x = 0
        self.robot_y = 0
    # move methods 
    def robot_movex_pos(self):
        self.robot_x = self.robot_x + 1
        print("Moving Robot 1 unit forward on the X axis Current position: " + str(self.robot_x))
    def robot_movex_neg(self):
        self.robot_x = self.robot_x - 1
        print("Moving Robot 1 unit back on the X axis Current Position: " + str(self.robot_x))
    def robot_movey_pos(self):
        self.robot_y = self.robot_y + 1
        print("Moving Robot 1 unit forward on the y axis Current position: " + str(self.robot_y))
    def robot_movey_neg(self):
        self.robot_y = self.robot_y - 1
        print("Moving Robot 1 unit back on the y axis Current Position: " + str(self.robot_y))
    # move logic method 
    def move_robot(self,destx,desty,obstaclex, obstacley):
        # first it will move forward and will check to see if there is an infront of it. If there is one along that axis it will move around that point. 
        while(self.robot_y < desty):
            if(self.robot_y + 1 == obstacley):
                if(self.robot_x + 1 == obstaclex):
                    self.robot_movex_neg()
                    self.robot_movey_pos()
                    self.robot_movey_pos()
                else:
                    self.robot_movex_pos()
                    self.robot_movey_pos()
                    self.robot_movey_pos()
            else:
                self.robot_movey_pos()
        while(self.robot_x < destx):
            if(self.robot_x + 1 == obstaclex):
                if(self.robot_y - 1 == obstacley):
                    self.robot_movey_pos()
                    self.robot_movex_pos()
                    self.robot_movex_pos()
                    self.robot_movey_neg()
                else:    
                    self.robot_movey_neg()
                    self.robot_movex_pos()
                    self.robot_movex_pos()
                    self.robot_movey_pos()
            else:
                self.robot_movex_pos()
        print(self.robot_x,self.robot_y,destx,desty)

                


    class Destination:
            # creating a random goal
            destx = random.randint(12,15)
            desty = random.randint(12,15)
            goal = "Red Line"
       
    class Obstacle:
        obstaclex = random.randint(1,13)
        obstacley = random.randint(1,13)
        obstacletype = "Pillar"
        print(obstaclex,obstacley)



robot = Robot_GPS()
robot.move_robot(robot.Destination.destx,robot.Destination.desty,robot.Obstacle.obstaclex,robot.Obstacle.obstacley)