# NetworkTablesViaJetsonFRC
Quick tutorial for setting up NetworkTables on the Jetson TX2 for use in FRC

I think Jetson comes with python

pip3 install pynetworktables

Connect Jetson to Robot Radio over ethernet

Then upload code from the respective files onto Rio and Jetson

The Rio program will change the value of X in the network table to a certain value once a button on a controller is pressed.

The program on the Jetson starts by listening for connections, then connects, then simply prints out the data inside the specified section from the network table
