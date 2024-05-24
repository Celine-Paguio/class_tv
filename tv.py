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
# Set a new channel for the tv
    def set_channel(self, channel):
        if self.on and (1 <= channel <= 120):
            self.channel = channel
# Increases the channel number by 1
# Decreases the channel number by 1
# Returns the channel for the tv
# Set a new volume for the tv
# Increases the volume of the tv by 1
# Decreases the volume of the tv by 1
# Gets the volume level for this tv