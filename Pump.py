import RPi.GPIO as GPIO
class Pump:
    #Connect to arduino?
    def __init__(self,pinNum):
        self.pin = pinNum
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pinNum, GPIO.OUT)
    def runPump(self):
        GPIO.output(self.pin,GPIO.HIGH)
    def stopPump(self):
        GPIO.output(self.pin,GPIO.LOW)

