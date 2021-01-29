import RPi.GPIO as GPIO
from time import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(14,GPIO.OUT) ##blue
GPIO.setup(15,GPIO.OUT) ##red
GPIO.setup(18,GPIO.OUT) ##green
GPIO.setup(10,GPIO.IN, pull_up_down=GPIO.PUD_DOWN) ##switch

GPIO.setup(12,GPIO.OUT) ##G
GPIO.setup(16,GPIO.OUT) ##F
GPIO.setup(20,GPIO.OUT) ##A
GPIO.setup(21,GPIO.OUT) ##B
GPIO.setup(26,GPIO.OUT) ##E
GPIO.setup(19,GPIO.OUT) ##D
GPIO.setup(13,GPIO.OUT) ##C

GPIO.setup(23,GPIO.OUT) ##Red
GPIO.setup(24,GPIO.OUT) ##Green
GPIO.setup(25,GPIO.OUT) ##Blue

def ledOFF():
    GPIO.output(15,0)
    GPIO.output(18,0)
    GPIO.output(14,0)
def ledOFF2():
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,0)
def red():
    GPIO.output(15,0)
    GPIO.output(18,1)
    GPIO.output(14,0)


def blue():
    GPIO.output(15,0)
    GPIO.output(18,0)
    GPIO.output(14,1)


def green():
    GPIO.output(15,1)
    GPIO.output(18,0)
    GPIO.output(14,0)

def red2():
    GPIO.output(24,0)
    GPIO.output(23,1)
    GPIO.output(25,0)


def blue2():
    GPIO.output(23,0)
    GPIO.output(24,0)
    GPIO.output(25,1)


def green2():
    GPIO.output(24,1)
    GPIO.output(23,0)
    GPIO.output(25,0)

def blinking():
    blue()
    sleep(0.5)
    ledOFF()
    sleep(0.5)
    blue()
    sleep(0.5)
    ledOFF()
    sleep(0.5)
    blue()
    sleep(0.5)
    ledOFF()
    sleep(0.5)

def none():
    GPIO.output(21,0)
    GPIO.output(13,0)
    GPIO.output(19,0)
    GPIO.output(12,0)
    GPIO.output(16,0)
    GPIO.output(20,0)
    GPIO.output(26,0)   
def one():
    GPIO.output(21,1)
    GPIO.output(13,1)
    GPIO.output(19,0)
    GPIO.output(12,0)
    GPIO.output(16,0)
    GPIO.output(20,0)
    GPIO.output(26,0)
    
def two():
    GPIO.output(21,1)
    GPIO.output(13,0)
    GPIO.output(19,1)
    GPIO.output(12,1)
    GPIO.output(16,0)
    GPIO.output(20,1)
    GPIO.output(26,1)
    
def three():
    GPIO.output(21,1)
    GPIO.output(13,1)
    GPIO.output(19,1)
    GPIO.output(12,1)
    GPIO.output(16,0)
    GPIO.output(20,1)
    GPIO.output(26,0)
    
def four():
    GPIO.output(21,1)
    GPIO.output(13,1)
    GPIO.output(19,0)
    GPIO.output(12,1)
    GPIO.output(16,1)
    GPIO.output(20,0)
    GPIO.output(26,0)
    
def five():
    GPIO.output(21,0)
    GPIO.output(13,1)
    GPIO.output(19,1)
    GPIO.output(12,1)
    GPIO.output(16,1)
    GPIO.output(20,1)
    GPIO.output(26,0)
    
def six():
    GPIO.output(21,0)
    GPIO.output(13,1)
    GPIO.output(19,1)
    GPIO.output(12,1)
    GPIO.output(16,1)
    GPIO.output(20,0)
    GPIO.output(26,1)
    
def seven():
    GPIO.output(21,1)
    GPIO.output(13,1)
    GPIO.output(19,0)
    GPIO.output(12,0)
    GPIO.output(16,0)
    GPIO.output(20,1)
    GPIO.output(26,0)
    
def eight():
    GPIO.output(21,1)
    GPIO.output(13,1)
    GPIO.output(19,1)
    GPIO.output(12,1)
    GPIO.output(16,1)
    GPIO.output(20,1)
    GPIO.output(26,1)

def nine():
    GPIO.output(21,1)
    GPIO.output(13,1)
    GPIO.output(19,0)
    GPIO.output(12,1)
    GPIO.output(16,1)
    GPIO.output(20,1)
    GPIO.output(26,0)

def zero():
    GPIO.output(21,1)
    GPIO.output(13,1)
    GPIO.output(19,1)
    GPIO.output(12,0)
    GPIO.output(16,1)
    GPIO.output(20,1)
    GPIO.output(26,1)
# GPIO.setup(12,GPIO.OUT) ##G
# GPIO.setup(16,GPIO.OUT) ##F
# GPIO.setup(20,GPIO.OUT) ##A
# GPIO.setup(21,GPIO.OUT) ##B
# GPIO.setup(26,GPIO.OUT) ##E
# GPIO.setup(19,GPIO.OUT) ##D
# GPIO.setup(13,GPIO.OUT) ##C

def countdown():
    green2()
    nine()
    sleep(1)
    eight()
    sleep(1)
    seven()
    sleep(1)
    six()
    sleep(1)
    five()
    sleep(1)
    four()
    blue2()
    sleep(1)
    three()
    ledOFF2()
    sleep(1)
    two()
    blue2()
    sleep(1)
    one()
    ledOFF2()
    sleep(1)
    zero()
    green()
    red2()
    sleep(1)
    
def coolDown():
    for i in range(0,9):
        sleep(1)

while True:
    none()
    red2()
    if GPIO.input(10) == GPIO.HIGH:
        #cat = false
        #cool
        print("Signal Detected")
        blinking()
        red()
        countdown()
        none()
        coolDown()
    else:
        green()
        




