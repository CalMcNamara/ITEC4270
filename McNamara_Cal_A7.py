import time  # Import the Time library
from gpiozero import DistanceSensor  # Import the GPIO Zero Library
from gpiozero import CamJamKitRobot
time.sleep(5)
class Rover:
    def __init__(self):
        # defining pin for the sensor's parts. 
        self.pinTrigger = 17
        self.pinEcho = 18
        self.pinLinefollower = 25
        # distance conunter
        self.total_distance = 0
        # distance measurment, starting at 
        self.distance_away = 1
        # motor speed
        self.motor_speed = .3
        self.motorforward = (self.motor_speed, self.motor_speed)
        self.motorbackward = (-self.motor_speed, -self.motor_speed)
        self.motorleft = (self.motor_speed, 0)
        self.motorright = (0, self.motor_speed)
        
        self.sensor = DistanceSensor(echo = self.pinEcho, trigger = self.pinTrigger)
        self.rover = CamJamKitRobot()
        
    def get_distance(self):
        self.distance_away = self.sensor.distance * 100
        print(self.distance_away)
    def move_forward(self):
        self.rover.value = self.motorforward
        time.sleep(.5)
        self.rover.stop()
        print("Moving Forward")
    def move_back(self):
        self.rover.value = self.motorbackward
        time.sleep(1)
        self.rover.stop()
        print("Moving Back")
    def move_left(self):
        self.rover.value = self.motorright
        # the diffrence between the bots time to move left and right are due to issues of the rovers wheels not touch the ground evenly
        time.sleep(3)
        self.rover.stop()
        print("Moving to the left")
    def move_right(self):
        self.rover.value = self.motorleft
        time.sleep(.5)
        self.rover.stop()
        print("Moving to the Right")
    def navigate(self):
        while(self.total_distance <= 10):
            print(self.total_distance)
            self.get_distance()
            # checking to see if there is an object infront of the rover.
            if(self.distance_away < 20):
                print(self.distance_away)
                self.get_distance()
                print("getting close to an obstacle")
                self.move_left()
                self.move_forward()
                self.move_right()
            else:
                self.move_forward()
                time.sleep(1)
                self.total_distance += 1
            time.sleep(1) 
                
                    
rover = Rover()
rover.get_distance()
rover.navigate()

# video demonstration https://www.youtube.com/watch?v=VXVAxkbMF70
