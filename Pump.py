import RPi.GPIO as GPIO
class Pump:
    #Connect to arduino?
    def __init__(self,pinNum):
        self.pin = pinNum
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pinNum, GPIO.OUT)
    def runPump(self):
        print(f"Starting pump {self.pin}")
        GPIO.setup(self.pin, GPIO.OUT)  # GPIO Assign mode
        GPIO.output(self.pin, GPIO.LOW)
        #GPIO.output(self.pin,GPIO.LOW)
    def stopPump(self):
        print(f"Stopping pump {self.pin}")
        GPIO.output(self.pin,GPIO.HIGH)




