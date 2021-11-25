#import RPi.GPIO as GPIO
import time
class Pump:
    #Connect to arduino?
    def __init__(self,pinNum):
        self.pin = pinNum
    def setUp(self):
        #GPIO.setmode(GPIO.BOARD)
        #GPIO.setup(self.pin, GPIO.OUT)
        pass
    def runPump(self,delay):
        #GPIO.output(self.pin,GPIO.HIGH)
        #time.sleep(delay)
        #GPIO.output(self.pin, GPIO.LOW)
        pass
