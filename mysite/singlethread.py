from .motor import motor
from .fan import fan
from .play import music
from .sound import *
def singlethread():
    # While server is running
    i = 0
    while(True):
        motor()
        fan()
        music()
        sound()
    # Once server is closed    
    GPIO.cleanup()        

