"""
Names: Mopeli Moka
Student Number: MPLMOK001
Prac: Prac 1
Date:29/07/2019 
"""

#Import Libraries
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
 
def main():
	GPIO.output(11,GPIO.HIGH)
	print("ON")
	time.sleep(2)
	GPIO.output(11,GPIO.LOW)
	print("OFF")
	time.sleep(2)

if __name__ == "__main__":
	try:
	   while True:
	        main()
	except KeyboardInterrupt:
	      print("Exeting gracefully")
	      GPIO.cleanup()
	except Exception as e:
	     GPIO.cleanup()
	     print("Some other error occurred")
	     print(e.message)
