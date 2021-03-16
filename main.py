import time

from ac_interface import AssettoCorsaData
from led_interface import LedInterface

ledInterface = LedInterface()
ledInterface.__init__()

assettoReader = AssettoCorsaData()
assettoReader.start()



def xred(rpm):
    return int(((rpm - 5500) * 255) / 1500)

def xgreen(rpm):
    return int(255 - (((rpm - 5500) * 255) / 1500))

while True:
    data = assettoReader.getData()
    if data['rpm']>6000:
        ledInterface.setColour(xred(data['rpm']), xgreen(data['rpm']), 0)
        print("(" + str(xred(data['rpm'])) + ", " + str(xgreen(data['rpm'])) + ")")
    


    """ data = assettoReader.getData()
    if data['rpm'] < 2000:
        start_time = time.time()
        ledInterface.setColour(0, 255, 0)
        print("[*] Green " + str((time.time() - start_time)))

    if data['rpm'] > 3000 and data['rpm'] < 5000:
        start_time = time.time()
        ledInterface.setColour(255, 255, 0)
        print("[*] Yellow " + str((time.time() - start_time)))

    elif data['rpm'] > 3000:
        start_time = time.time()
        ledInterface.setColour(255, 0, 0)
        print("[*] Red " + str((time.time() - start_time)))"""