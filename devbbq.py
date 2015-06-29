#!/usr/bin/python
 
import spidev
import time
import os

spi = spidev.SpiDev()
spi.open(0,0)

# Sets the delay period
delay = 1

def read_spi(channel):
    os.system('clear')
    spidata = spi.xfer2([1,(8+channel)<<4,0])
    print("Raw ADC:      {}".format(spidata))
    print("-----------------")
    data = ((spidata[1] & 3) << 8) + spidata[2]
    return data
 
try:
    while True:
        channeldata1 = read_spi(0)
        voltage1 = round(((channeldata1 * 3300) / 1023),0)
        temperaturek1 = ((voltage1) / 10)
        temperaturec1 = ((temperaturek1) - 273.15)
        temperaturef1 = ((((temperaturek1) - 273.15) * 9/5) +32)
        channeldata2 = read_spi(1)
        voltage2 = round(((channeldata2 * 3300) / 1023),0)
        temperaturek2 = ((voltage2) / 10)
        temperaturec2 = ((temperaturek2) - 273.15)
        temperaturef2 = ((((temperaturek2) - 273.15) * 9/5) +32)
        avgtempk = (((temperaturek1) + (temperaturek2)) / 2)
	avgtempc = (((temperaturec1) + (temperaturec2)) / 2)
        avgtempf = (((temperaturef1) + (temperaturef2)) / 2)
        print("Data (dec)     {}".format(channeldata1))
        print("Data (bin)     {}".format(('{0:010b}'.format(channeldata1))))
        print("Voltage (mV):  {}".format(voltage1))
        print("Temperature-1: {} Kelvin".format(temperaturek1))
        print("Temperature-1: {} Celsius".format(temperaturec1))
        print("Temperature-1: {} Fahrenheit".format(temperaturef1))
        print("-----------------")
        print("Data (dec)     {}".format(channeldata2))
        print("Data (bin)     {}".format(('{0:010b}'.format(channeldata2))))
        print("Voltage (mV):  {}".format(voltage2))
        print("Temperature-2: {} Kelvin".format(temperaturek2))
        print("Temperature-2: {} Celsius".format(temperaturec2))
        print("Temperature-2: {} Fahrenheit".format(temperaturef2))
        print("-----------------")
        print("Avg Temperature:")
	print("{} Kelvin".format(avgtempk))
        print("{} Celsius".format(avgtempc))
        print("{} Fahrenheit".format(avgtempf))
	time.sleep(delay)
 
except KeyboardInterrupt:
	spi.close()
