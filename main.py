import time

from ac_interface import AssettoCorsaData
from led_interface import LedInterface

ledInterface = LedInterface()
ledInterface.__init__()

assettoReader = AssettoCorsaData()
assettoReader.start()

state = None

#def xred(rpm):
 #   return int(((rpm - 5500) * 255) / 1500)
#def xgreen(rpm):
 #   return int(255 - (((rpm - 5500) * 255) / 1500))
#     ledInterface.setColour(xred(data['rpm']), xgreen(data['rpm']), 0)
  #      print("(" + str(xred(data['rpm'])) + ", " + str(xgreen(data['rpm'])) + ")")
    
#THIS SENT CALL TOO QUICKLY TO THE LED CONTROLLER, MAKING IT CRASH
#NOW I ONLY CALL THE .changeColor WHEN THE COLOR NEEDS TO CHANGE


while True:
    data = assettoReader.getData()
    print(str(data['rpm']))
    
    if data['rpm']<6000 and state != 0:
        ledInterface.setColour(0, 255, 0)
        state = 0

    elif data['rpm']>=6000 and data['rpm']<6300 and state != 1:
        ledInterface.setColour(140, 255, 0)
        state = 1
        
    elif data['rpm']>=6300 and data['rpm']<6400 and state != 2:
        ledInterface.setColour(200, 255, 0)
        state = 2

    elif data['rpm']>=6400 and data['rpm']<6600 and state != 3:
        ledInterface.setColour(255, 255, 0)
        state = 3

    elif data['rpm']>=6600 and data['rpm']<7000 and state != 4:
        ledInterface.setColour(255, 0, 0)
        state = 4

    elif data['rpm']>=7000 and state != 5:
        ledInterface.setColour(128, 0, 128)
        state = 5
    
    time.sleep(0.02)

