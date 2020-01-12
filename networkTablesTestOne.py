import threading
from networktables import NetworkTables

cond = threading.Condition()
notified = [False]

def connectionListener(connected, info):
    print(info, '; Connected=%s' % connected)
    with cond:
        notified[0] = True
        cond.notify()

NetworkTables.initialize(server='10.80.29.2')
NetworkTables.addConnectionListener(connectionListener, immediateNotify=True)

with cond:
    print("Waiting")
    if not notified[0]:
        cond.wait()

print('connected')

while(1==1):

	# Insert your processing code here

	table = NetworkTables.getTable('datatable')

	value = table.getNumber('X', 1)

	print(value)
	
	#uncomment the following if you would like to send data to rio rather than recieve

	#table.putNumber('X', 3)
