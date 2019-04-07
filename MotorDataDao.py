import datetime

class MotorDatum():
    time_format = "%m/%d/%Y, %H:%M:%S"
    def __init__(self):
        self.timestamp = datetime.datetime.now()
        self.current = 0
        self.voltage = 0

    def set_current(self, c):
        self.current = c

    def get_current(self):
        return self.current

    def set_voltage(self, v):
        self.voltage = v

    def get_voltage(self):
        return self.voltage

    def set_timestamp(self, t):
        self.timestamp = datetime.datetime.strptime(t, self.time_format)

    def get_timestamp(self):
        return self.timestamp.strftime(self.time_format)

    def get_postable(self):
        return {'ts': self.get_timestamp(),'current': self.get_current(), 'voltage': self.get_voltage()}

    def read_and_set(self, a, id):
        mr = a[id]
        self.set_timestamp(mr['ts'])
        self.set_voltage(mr['voltage'])
        self.set_current(mr['current'])
        return self.get_postable

    def print(self):
        print("At time %s, current was %s and voltage was %s" % (self.get_timestamp(), str(self.get_voltage()), str(self.get_voltage())))
