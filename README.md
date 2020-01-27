# NetworkTablesViaJetsonFRC
Quick tutorial for setting up NetworkTables on the Jetson TX2 for use in FRC

pip install pynetworktables
https://github.com/BraedenCullenCodes/NetworkTablesViaJetsonFRC

Connect Jetson to Robot Radio over ethernet

Then upload code from the respective files onto Rio and Jetson

The Rio program will change the value of X in the network table to a certain value once a button on a controller is pressed.

The program on the Jetson starts by listening for connections, then connects, then simply prints out the data inside the specified seciton of the network table
