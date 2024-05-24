# This program creates a class named tv and a test driver named test_tv that will create two objects from class tv

# Define the tv class
class tv:
# Use constructor
    def __init__(self):
# Set the initial state of the tv
        self.on = False
# Turns on the tv
    def turn_on(self):
        self.on = True
# Turns off the tv
    def turn_off(self):
        self.on = False
# Get if the tv is on or off
    def get_on_or_off(self):
        return self.on
# Set a channel for the tv
    def set_channel(self, channel):
        if self.on and (1 <= channel <= 120):
            self.channel = channel
# Increases the channel number by 1
    def channel_up(self):
        if self.channel < 120:
            self.channel += 1
# Decreases the channel number by 1
    def channel_down(self):
        if self.channel > 0:
            self.channel -= 1
# Returns the channel for the tv
    def get_channel(self):
        return self.channel
# Set a volume for the tv
    def set_volume(self, volume):
        if self.on and (1 <= volume <= 7):
            self.volume = volume
# Increases the volume of the tv by 1
# Decreases the volume of the tv by 1
# Gets the volume level for this tv
    def get_volume(self):
        return self.volume