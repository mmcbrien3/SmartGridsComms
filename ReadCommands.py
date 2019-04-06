import requests
import time
from CommandsDao import Commands
URL = "http://127.0.0.1:5000/Commands"
while True:
    r = requests.get(url=URL)
    print(type(r.json()))
    if len(r.json()) > 0:
        c = Commands()
        c.read_and_set(r.json())
        c.print()

    time.sleep(5)