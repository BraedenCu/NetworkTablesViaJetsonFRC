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
 
import cv2
import numpy as np

lowerBound=np.array([33,80,40])
upperBound=np.array([102,255,255])
red = (255,0,0)
distance = 1
xcenter = 1
center = 0
cam = cv2.VideoCapture(1)

kernelOpen=np.ones((5,5))
kernelClose=np.ones((20,20))


while True:
    
    table = NetworkTables.getTable('8029data')
    #prev frame not image
    ret, image = cam.read()
    ret, img = cam.read()
    #added resize function
    frame = cv2.resize(image, (250, 250))
    
    #convert BGR to HSV
    imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    # create the Mask
    mask=cv2.inRange(imgHSV,lowerBound,upperBound)
    #morphology
    maskOpen=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernelOpen)
    maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,kernelClose)

    maskFinal=maskClose
    _, conts, _= cv2.findContours(maskFinal.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for i in range(len(conts)):
        #cool center stuff (for big brains only)        
        c =  max(conts,key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        if radius > 50:
             x,y,w,h=cv2.boundingRect(conts[i])
             cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255), 2)
             print(center)
             xcenter = (int(M["m10"] / M["m00"]))
             distance = int(xcenter - 125)
             table.putNumber('x', xcenter)
        else:
             table.putNumber('x', 125)
    #cv2.imshow("maskClose",maskClose)
    #cv2.imshow("maskOpen",maskOpen)
    #cv2.imshow("mask",mask)
    cv2.imshow("cam",frame)
    cv2.waitKey(10)
