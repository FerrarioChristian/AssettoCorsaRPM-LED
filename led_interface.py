import tinytuya

class LedInterface():

    def __init__(self):
        self.device = tinytuya.BulbDevice('bf80b3b54b9856bf57brh4', '192.168.0.3', '1bb14822386d6d5a', 'device22')
        self.device.set_dpsUsed({"24": None})
        self.device.set_version(3.3)

    def setColour(self, red, green, blue):
        self.device.set_colour(red, green, blue)