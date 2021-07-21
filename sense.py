from sense_hat import SenseHat
## The above code imports the required sensor (SenseHat) module from sense_hat library...
sense = SenseHat()
sense.clear()
## The above code  abbreviates the SenseHat module as sense, and clears all the processes on the SenseHat
tempa = sense.get_temperature() 
tempb = sense.get_temperature_from_pressure()
avgtemp = (tempa + tempb) / 2
pressure = sense.get_pressure()
humidity = sense.get_humidity()
## The above code assigns humidity, pressure, temperature from either the pressure/humidity sensor and the average of the two to their respective variables, and puts the following code in a loop for real-time data.
print("x={0}, y={1}, z={2}".format(x, y, z))
print(tempa)
print(tempb)
print(avgtemp)
print(pressure)
print(humidity)
## The above code prints the sensed data!
