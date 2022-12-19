from spike import PrimeHub, ColorSensor, DistanceSensor, MotorPair
from spike.control import wait_for_seconds
import random

# Initialize the PrimeHub to beep.
hub = PrimeHub()

# I do not know where your motors are plugged in but mine are C and D.
motor_pair = MotorPair('C','D')

# Why not? It's F now.
distance_l = DistanceSensor('E')
#distance_r = DistanceSensor('F')
distance_f = DistanceSensor('A')

# And I guess this one is B.
color_sensor = ColorSensor('B')



motor_pair.set_default_speed(30)


def move(sense_color, range):

    # An array for storing the colors that the robot has encountered
    color_array = []
    # Alternates so it always turns left then right
    turn_left = True
    motor_pair.start(0, 30)
    while True:
        # Sense the current_color
        current_color = color_sensor.get_color()  
        #right_sensor = get_distance(distance_r)
        # If a wall is within x distance, turn
        # The direction turned is based on the turn_left flag, which alternates with each turn
        if(get_distance(distance_l) > range * 2):
            wait_for_seconds(.9)
            rotate_left()
            motor_pair.start(0,30)
            wait_for_seconds(.9)
            #Move forward a bit while still sensing the front but not the back
        elif(get_distance(distance_f) < range):
            rotate_right()
        motor_pair.start(0,30)
        # If the current color is the one we're searching for, we can stop
        if current_color == sense_color:
            hub.speaker.beep(60, 1)
            motor_pair.stop()
            break
        # If the current color is not the one we're looking for but the robot has sensed a color that isn't the posterboard
        # that it's searching on, beep to signal that it is incorrect, store it, and then continue on

        elif current_color != 'white' and current_color != None:
            hub.speaker.beep(44,1)
            color_array.append(current_color)
    previous_colors(color_array)

def backtrack(color_array, range):
    sense_color = color_array[random.randint(0,1)]
    rotate_left()
    rotate_left()
    motor_pair.start(0,30)

    while True:
        current_color = color_sensor.get_color()  

        if get_distance(distance_f) < range:
            rotate_left()
            motor_pair.start(0,30)

        elif get_distance(distance_r) > range:
            rotate_right()
            motor_pair.start(0,30)
            distance_r.wait_for_distance_closer_than(range, unit='cm', short_range=True)

        if sense_color == current_color:
            hub.speaker.beep(60, 1)
            motor_pair.stop()
            break


        
        
       

def previous_colors(color_array):
    for color in color_array:
        if color == 'red':
            hub.speaker.beep(100,1)
        elif color == 'green':
            hub.speaker.beep(90,1)
        elif color == 'blue':
            hub.speaker.beep(80,1)
        else:
            hub.speaker.beep(70,1)

def get_distance(sensor):
    cm = sensor.get_distance_cm()
    if isinstance(cm, int):
        return cm
    return 99999999

def rotate_to_yaw(yaw, speed):

    while yaw != hub.motion_sensor.get_yaw_angle():
        motor_pair.start_tank(speed, -speed)
    motor_pair.stop()
    return

def rotate_right():
    hub.motion_sensor.reset_yaw_angle()
    rotate_to_yaw(90, 15)
    return

def rotate_left():
    hub.motion_sensor.reset_yaw_angle()
    rotate_to_yaw(-90, -15)
    return


move('green', 10)
