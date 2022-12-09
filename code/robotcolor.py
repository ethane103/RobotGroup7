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

def move(sense_color):

    while True:
        if get_distance() < 30:
            motor_pair.stop()
            motor_pair.move(19, 'cm', steering=100)
            print("1")
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

move('blue')