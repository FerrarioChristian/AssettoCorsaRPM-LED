import tinytuya
import time

device = tinytuya.BulbDevice('bf80b3b54b9856bf57brh4', '192.168.0.3', '1bb14822386d6d5a', 'device22')
device.set_dpsUsed({"24": None})
device.set_version(3.3)
choose = str(input("[?] Insert a color name: "))

if choose == "red":
    device.set_colour(255,0,0)

if choose == "green":
    device.set_colour(0,255,0)
    
if choose == "blue":
    device.set_colour(0,0,255)

# THIS MUST BE CALLED OTHERWISE IT WILL NOT WORK!!!
device.status()

while True:
    device.set_colour(255,0,0)
    device.status()
    time.sleep(0.1)
    device.set_colour(0,255,0)
    device.status()
    time.sleep(0.1)
    device.set_colour(0,0,255)
    device.status()
    time.sleep(0.1)