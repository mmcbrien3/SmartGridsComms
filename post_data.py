from time import sleep
from ina219 import INA219
from MotorDataDao import MotorDatum
import requests
ina = INA219(shunt_ohms=0.1,max_expected_amps=1,address=0x40)

ina.configure(voltage_range=ina.RANGE_16V,
                gain=ina.GAIN_AUTO,
                bus_adc=ina.ADC_128SAMP,
                shunt_adc=ina.ADC_128SAMP)
delay = .5
try:
	while True:
		#READ IN VALUES
		v = ina.voltage()
		print(v)
		i = ina.current()/1000.0
		print(i)
		#POST NEW DATA
		if v is not None and i is not None:
			URL = "http://192.168.43.225:5000/MotorData"
			command = MotorDatum()
			command.set_current(i)
			command.set_voltage(v)
			r = requests.post(URL, command.get_postable())
			print("Successfully posted data of v: %f and i: %f" %(v, i))

		sleep(delay)
except Exception as e:
	print("Something went wrong reading from the ina219")
	print(e)
