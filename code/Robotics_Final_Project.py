
from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

#Slots the devices should be in
hub = PrimeHub()
distance = DistanceSensor('A')
motorL = Motor('C')
motorR = Motor('D')
motor_pair = MotorPair('C', 'D')
color1 = ColorSensor('B')


#If object is closer than range, move backwards. If no objects are in range, move forward. This method lasts for "duraction" seconds
def search(range, duration):
    hub.speaker.beep(60, 0.5)
    sense_color = 'blue'
    motor_pair.start(0, 30)
    timer = Timer()
    timer.reset()
    #Alternates so it always turns left then right
    turn_left = True
    while(timer.now() < duration):
        if(get_distance_cm_num() < range):
            if turn_left:
                rotate_degrees(-90, 30)
                turn_left = False
            else:
                rotate_degrees(90,30)
                turn_left = True
        else:
            motor_pair.start(0, 30)
        wait_for_seconds(.1)
        if color1.get_color() == sense_color:
            motor_pair.stop()
            hub.speaker.beep(60, 0.5)
            break
    motor_pair.stop()
    return

def get_distance_cm_num():
    cm = distance.get_distance_cm()
    if type(cm) != int:
        return 999999
    return cm

def rotate_to_yaw(yaw, speed):
    
    while yaw != hub.motion_sensor.get_yaw_angle():
        motor_pair.start_tank(speed, -speed)
    motor_pair.stop()
    return

def rotate_degrees(degrees, speed):
    hub.motion_sensor.reset_yaw_angle()
    rotate_to_yaw(degrees, speed)
    return

search(10, 60)

