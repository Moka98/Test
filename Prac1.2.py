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
button_list =[7,13]
GPIO.setup(button_list,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.output(11,GPIO.LOW)

def turnOn(channel):
	GPIO.output(11,GPIO.HIGH)
	print("Turned on")
	

def turnOff(channel):
	GPIO.output(11,GPIO.LOW)
	print("Turned off")
	

GPIO.add_event_detect(7,GPIO.RISING,callback=turnOn,bouncetime=300)
GPIO.add_event_detect(13,GPIO.RISING,callback=turnOff,bouncetime=300)
 
def main():
	print ("Works")
	time.sleep(10)





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
