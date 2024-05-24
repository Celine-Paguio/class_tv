# This program is the test driver that will produce the output from the class tv

# Import tv
from tv import tv
def test_tv():
# Create instances of the class
    tv_1 = tv()
    tv_2 = tv()
# Turn on the tv 1 
    tv_1.turn_on()
# Turn on tv 2
    tv_2.turn_on()
# Set channel for tv 1
    tv_1.set_channel(30)
# Increase channel number of tv 1 by 1
    # tv_1.channel_up()
# Decrease the channel number of tv 1 by 1
    # tv_1.channel_down()
# Set volume for tv 1
    tv_1.set_volume(3)
# Increase the volume of tv 1 by 1
    # tv_1.volume_up()
# Decrease the volume of tv 1 by 1
    # tv_1.volume_down()
# Set channel for tv 2 
    tv_2.set_channel(3)
# Increase channel number of tv 2 by 1
    # tv_2.channel_up()
# Decrease the channel number of tv 2 by 1
    # tv_2.channel_down()
# Set volume for tv 2
    tv_2.set_volume(2)
# Increase the volume of tv 2 by 1 
    # tv_2.volume_up()
# Decrease the volume of tv 2 by 1
    # tv_2.volume_down()
# Print the output
    print("tv1's channel is", tv_1.get_channel(), "and the volume level is", tv_1.get_volume())
    print("tv2's channel is", tv_2.get_channel(), "and the volume level is", tv_2.get_volume())
# Call the test_tv function to produce the output
test_tv()

# End of program