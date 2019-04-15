from time import sleep
from ina219 import INA219

ina = INA219(shunt_ohms=0.1,max_expected_amps=1,address=0x40)

ina.configure(voltage_range=ina.RANGE_16V,
		gain=ina.GAIN_AUTO,
		bus_adc=ina.ADC_128SAMP,
		shunt_adc=ina.ADC_128SAMP)

try:
	while True:
		v=ina.voltage()
		i=ina.current()/1000.0
		p=ina.power()/1000.0
		print("Voltage: %f, Current: %f, Power: %f" % (v, i , p))
		sleep(2)
except:
	print("Something went wrong")
