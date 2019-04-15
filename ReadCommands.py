import requests
import time
from CommandsDao import Commands
URL = "http://192.168.43.225:5000/Commands"
while True:
    r = requests.get(url=URL)
    print(type(r.json()))
    if len(r.json()) > 0:
        c = Commands()
        c.read_and_set(r.json())
        c.print()

    time.sleep(5)
