import RPi.GPIO as GPIO
import time, datetime
now = datetime.datetime.now()
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
 #GPIO ports for the 7segment pins
segment8 =  (26,19,13,6,5,11,9,10)
 
for segment in segment8:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 1)
 
    #Digit 1
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7, 0) #Off initially
    #Digit 2
    GPIO.setup(8, GPIO.OUT)
    GPIO.output(8, 0) #Off initially
    #Digit 3
    GPIO.setup(25, GPIO.OUT)
    GPIO.output(25, 0) #Off initially
    #Digit 4
    GPIO.setup(24, GPIO.OUT)
    GPIO.output(24, 0) #Off initially
null = [1,1,1,1,1,1,1]
zero = [0,0,0,0,0,0,1]
one = [1,0,0,1,1,1,1]
two = [0,0,1,0,0,1,0]
three = [0,0,0,0,1,1,0]
four = [1,0,0,1,1,0,0]
five = [0,1,0,0,1,0,0]
six = [0,1,0,0,0,0,0]
seven = [0,0,0,1,1,1,1]
eight = [0,0,0,0,0,0,0]
nine = [0,0,0,0,1,0,0]
def print_segment(charector):
    if charector == 1:
        for i in range(7):
            GPIO.output(segment8[i], one[i])
    if charector == 2:
        for i in range(7):
            GPIO.output(segment8[i], two[i])
    if charector == 3:
        for i in range(7):
            GPIO.output(segment8[i], three[i])
    if charector == 4:
        for i in range(7):
            GPIO.output(segment8[i], four[i])
    if charector == 5:
        for i in range(7):
            GPIO.output(segment8[i], five[i])
    if charector == 6:
        for i in range(7):
            GPIO.output(segment8[i], six[i])
    if charector == 7:
        for i in range(7):
            GPIO.output(segment8[i], seven[i])
    if charector == 8:
        for i in range(7):
            GPIO.output(segment8[i], eight[i])
    if charector == 9:
        for i in range(7):
            GPIO.output(segment8[i], nine[i])
    if charector == 0:
        for i in range(7):
            GPIO.output(segment8[i], zero[i])        
            
    return;
while 1:
    for i in range(61):
        i1=i/10
        i2=i%10
  
        delay_time = 0.1 #delay to create virtual effect
    
    
        GPIO.output(7, 1) #Turn on Digit One
        print_segment (int(i1)) #Print i1 on segment
        time.sleep(delay_time)
        GPIO.output(7, 0) #Turn off Digit One
        GPIO.output(8, 1) #Turn on Digit two
        print_segment (int(i2)) #Print i2 on segment
        #Display point Off
        time.sleep(delay_time)
        GPIO.output(8, 0) #Turn off Digit two
  
    
