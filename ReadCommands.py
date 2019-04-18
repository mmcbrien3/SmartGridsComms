import requests, time
from CommandsDao import Commands
speed_level = 0

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
URL = "http://192.168.43.225:5000/Commands"
while True:
    r = requests.get(url=URL)
    print(r.json())
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
    time.sleep(0.01)