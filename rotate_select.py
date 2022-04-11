import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def button_callback(channel, number):
    #will add comunication to game later.
    if(number == 1):
        #RED (Normal)
        GPIO.ouput(22, 1)
    if(number == 2):
        #PURPLE(Tilt)
        GPIO.output(24, 1)
    if(number == 3):
        #BLUE (Voice)
        GPIO.output(22, 0)
    if(number == 4):
        #GREEN (Auto)
        GPIO.output(26, 1)
        GPIO.output(22,0)
    
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(22, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(24, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(26, GPIO.OUT, pull_up_down=GPIO.PUD_DOWN) 
num = 0
GPIO.add_event_detect(10,GPIO.RISING,callback=lambda *a: button_callback(10,num+1)) #Button is on pin 10 for now
message = input("Press enter to quit\n\n") 
GPIO.cleanup() # Clean up