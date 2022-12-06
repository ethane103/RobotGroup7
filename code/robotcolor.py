from spike import PrimeHub, ColorSensor, DistanceSensor, MotorPair

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
        else:
            motor_pair.start(0, 30)
        if color_sensor.get_color() == sense_color:
            hub.speaker.beep(60, 1)
            motor_pair.stop()
            break

def get_distance():
    cm = distance_sensor.get_distance_cm()
    if isinstance(cm, int):
        return cm
    return 99999999

move('blue')