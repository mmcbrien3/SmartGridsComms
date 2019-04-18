import requests
import time
from CommandsDao import Commands
URL = "http://192.168.43.225:5000/Commands"
import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

# set up GPIO pins
GPIO.setup(7, GPIO.OUT) # Connected to PWMA
GPIO.setup(11, GPIO.OUT) # Connected to AIN2
GPIO.setup(12, GPIO.OUT) # Connected to AIN1
GPIO.setup(13, GPIO.OUT) # Connected to STBY

# Drive the motor clockwise
GPIO.output(12, GPIO.HIGH) # Set AIN1
GPIO.output(11, GPIO.LOW) # Set AIN2

# Set the motor speed
speed_level = 50
pwm = GPIO.PWM(7, 100)
pwm.start(speed_level)
# Disable STBY (standby)
GPIO.output(13, GPIO.HIGH)

def increase_speed_level(sl):
    sl += 5
    if sl > 100:
        sl = 100
    return sl

def decrease_speed_level(sl):
    sl -=5
    if sl < 0:
        sl = 0
    return sl
last_time_stamp = None
while True:
    r = requests.get(url=URL)
    print(type(r.json()))
    if len(r.json()) > 0:
        c = Commands()
        c.read_and_set(r.json())
        c.print()
        if c.get_command() == "increase" and not last_time_stamp == c.get_timestamp():
            speed_level = increase_speed_level(speed_level)
            pwm.start(speed_level)
            last_time_stamp = c.get_timestamp()
        elif c.get_command() == "decrease":
            speed_level = decrease_speed_level(speed_level)
            pwm.start(speed_level)
            last_time_stamp = c.get_timestamp()
    time.sleep(5)
