import requests
import time
from MotorDataDao import MotorDatum
URL = "http://127.0.0.1:5000/MotorData"
while True:

    r = requests.get(url=URL)
    print(r.json())
    if len(r.json()) > 0:
        all_motor_data = r.json().items()
        print(all_motor_data)

    time.sleep(5)