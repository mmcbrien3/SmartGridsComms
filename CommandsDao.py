import time

class Commands():
    time_format = "%m/%d/%Y, %H:%M:%S"
    def __init__(self):
        self.timestamp = time.time()
        self.increase = False

    def set_command(self, c):
        if c.lower() == "increase":
            self.increase = True
        elif c.lower() == "decrease":
            self.increase = False
        else:
            raise Exception("Invalid argument for set_command")

    def get_command(self):
        if self.increase:
            return "increase"
        else:
            return "decrease"

    def set_timestamp(self, t):
        self.timestamp = t

    def get_timestamp(self):
        return self.timestamp

    def get_postable(self):
        return {'ts': self.get_timestamp(),'command': self.get_command()}

    def read_and_set(self, c):
        mr = sorted(c.items(), key=lambda kv: int(kv[0]))[-1][1]
        self.set_timestamp(mr['ts'])
        self.set_command(mr['command'])
        return self.get_postable

    def print(self):
        print("At time %s, a %s command was posted" % (self.get_timestamp(), self.get_command()))
