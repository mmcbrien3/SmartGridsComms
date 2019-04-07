import requests, time
from MotorDataDao import MotorDatum

URL = "http://127.0.0.1:5000/MotorData"

d = 'inCreaSe'
command = MotorDatum()
command.set_current(5)
command.set_voltage(10)
r = requests.post(URL, command.get_postable())
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)