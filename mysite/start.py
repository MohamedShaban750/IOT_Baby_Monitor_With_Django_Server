# Threading Imports
import threading
from time import sleep
import time
from .motor import motor
from .fan import fan
from .statusLcd import *
from .play import music
from .singlethread import singlethread

# Creating the single thread
singlethread = threading.Thread(target=singlethread, daemon=True)
singlethread.start()

# Creating the status thread
lcdStatusThread = threading.Thread(target=lcdTest, daemon=True)
lcdStatusThread.start()
#

