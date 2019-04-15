from time import sleep
from ina219 import INA219

ina = INA219(shunt_ohms=0.1,max_expected_amps=1,address=0x40)

ina.configure(voltage_range=ina.RANGE_16V,
                gain=ina.GAIN_AUTO,
                bus_adc=ina.ADC_128SAMP,
                shunt_adc=ina.ADC_128SAMP)
delay = 3
try:
	while True:
		#READ IN VALUES
		v = ina.voltage()
		i = ina.voltage()/1000.0
		#POST NEW DATA
		if v and i:
			URL = "http://127.0.0.1:5000/MotorData"
			command = MotorDatum()
			command.set_current(i)
			command.set_voltage(v)
			r = requests.post(URL, command.get_postable())
			print("Successfully posted data of v: %v and i: %i" %(v, i))

		sleep(delay)
except:
	print("Something went wrong reading from the ina219")
