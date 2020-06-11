
class Robot:
    def __init__(self):
        self.controller = self.Controller()
        self.sensor = self.Sensor()
        self.claw = self.Claw()
        self.motor = self.Motor()
    
    def activate_controller(self):
        self.controller()
    
    def print_sensor(self):
        print(self.sensor.sensor_value)
    # Class def for actualtors for the motor
    class Motor:
        actualtor_type = "motor"
        actualtor_end_effector = "Claw"

        def activate_motor(self, force):
            print("Applying " + force + " to the Claw")


    # Class def for end_effectors for the claw
    class Claw:
        end_effector_type = "Claw"
        # claw stances should be close , open , closing , opening.
        claw_stance = "Open"

        def claw_work(self,rw_obj):
            print(self.end_effector_type +" " + self.claw_stance + " on " + rw_obj )

    # Class def for Sensor for the distance sensor
    class Sensor:
        # This sensor measure's the distance from it to a give object. 
        sensor_type = "Distance"
        # Sensor values Max 10 min 0 in inches.
        sensor_value = 10.0

        def return_sensordata(self):
            return(self.sensor_value)


    # class def for Controller

    class Controller:
        controller_type = "microprocessor"

        def read_sensor(self,sensorclass):
            sensor_value = sensorclass.sensor_value
            print(sensorclass.sensor_value)
        def control_actuator(self,actualtor_funtion):
            print("Controller " + str(self.controller_type) + " Sending Order to "+ str(actualtor_funtion))
            print("Claw Status : " + Robot.Claw.claw_stance)
            
            while(Robot.Sensor.sensor_value > 0):
                if(Robot.Sensor.sensor_value <= 10):
                    #Change Claw's stnace to closing. 
                    Robot.Claw.claw_stance = "Closing"
                    Robot.Sensor.sensor_value -= 1
                    print("Controller " + str(self.controller_type) + " Sending Order to "+ str(actualtor_funtion) + " to close")
                    print("Distnace Unitl close " + str(Robot.Sensor.sensor_value))
                    print("Claw Status : " + Robot.Claw.claw_stance)

                if(Robot.Sensor.sensor_value == 0):
                    Robot.Claw.claw_stance = "Closed"
                    print("Controller " + str(self.controller_type) + " Sending Order to "+ str(actualtor_funtion) + " complete")
                    print("Claw Status : " + Robot.Claw.claw_stance)
                    Robot.Claw.claw_work(Robot.Claw,"Box")
            

clawbot = Robot()

clawbot.print_sensor()
clawbot.Controller.control_actuator(Robot.Controller,Robot.Claw.end_effector_type)


