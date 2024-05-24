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
# Increase channel number by 1
    # tv_1.channel_up()
# Decrease the channel number by 1
    # tv_1.channel_down()
# Set volume for tv 1
# Set channel for tv 2
    tv_2.set_channel(3)
# Increase channel number by 1
    # tv_2.channel_up()
# Decrease the channel number by 1
    # tv_2.channel_down()
# Set volume for tv 2
# Print the output
    print("tv1's channel is" ,tv_1.get_channel())
    print("tv2's channel is" ,tv_2.get_channel())
# Call the test_tv function to produce the output
test_tv()