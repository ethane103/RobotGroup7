from spike import PrimeHub, ColorSensor, DistanceSensor, MotorPair
from spike.control import wait_for_seconds

# Initialize the PrimeHub to beep.
hub = PrimeHub()

# I do not know where your motors are plugged in but mine are C and D.
motor_pair = MotorPair('D','C')

# Why not? It's F now.
distance_sensor = DistanceSensor('F')

# And I guess this one is B.
color_sensor = ColorSensor('B')

motor_pair.set_default_speed(30)

def move(sense_color, range):

    #Alternates so it always turns left then right
    turn_left = True
    motor_pair.start(0, 30)
    while True:
        #If a wall is withen x distance, turn
        #The direction turned is based on the turn_left flag, which alternates with each turn
        if(get_distance() < range):
            if turn_left:
                rotate_degrees(-90, 30)
                turn_left = False
            else:
                rotate_degrees(90,30)
                turn_left = True
        else:
            motor_pair.start(0, 30)
        if color_sensor.get_color() == sense_color:
            hub.speaker.beep(60, 1)
            motor_pair.stop()
            print("3")
            break
        else:
            motor_pair.stop()
            hub.speaker.beep(44,1)
            wait_for_seconds(1)
            motor_pair.start(0,-30)
            wait_for_seconds(3)
            print("4")

def get_distance():
    cm = distance_sensor.get_distance_cm()
    if isinstance(cm, int):
        return cm
    return 99999999

def rotate_to_yaw(yaw, speed):
    
    while yaw != hub.motion_sensor.get_yaw_angle():
        motor_pair.start_tank(speed, -speed)
    motor_pair.stop()
    return

def rotate_degrees(degrees, speed):
    hub.motion_sensor.reset_yaw_angle()
    rotate_to_yaw(degrees, speed)
    return


move('blue', 5)
