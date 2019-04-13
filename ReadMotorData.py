import requests
import time
from MotorDataDao import MotorDatum
URL = "http://127.0.0.1:5000/MotorData"
while True:

    r = requests.get(url=URL)
    print(r.json())
    if len(r.json()) > 0:
        all_motor_data = r.json()
        p = []
        if all_motor_data:
            for k, v in all_motor_data.items():
                p.append(float(v['current'])*float(v['voltage']))
        print(all_motor_data)
        print(p)
    time.sleep(5)