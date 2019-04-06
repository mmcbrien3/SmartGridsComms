import requests, time
from CommandsDao import Commands

URL = "http://127.0.0.1:5000/Commands"

d = 'inCreaSe'
command = Commands()
command.set_command(d)
r = requests.post(URL, command.get_postable())
pastebin_url = r.text
print("The pastebin URL is:%s"%pastebin_url)