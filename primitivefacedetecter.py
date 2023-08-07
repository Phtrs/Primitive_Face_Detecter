import cv2
import numpy as np

img=cv2.VideoCapture(0)

def getContours(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0

    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500:
            #cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 2)
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)

            x, y, w, h = cv2.boundingRect(approx)
    return x , y , x+w , y+h




color=[0,46,86,183,98,133]
lower= np.array(color[0:3])
upper=np.array(color[3:6])

while True:
    succes, normal = img.read()
    #imgHSV=FaceFinder(img)
    imgHSV = cv2.cvtColor(normal, cv2.COLOR_BGR2HSV)
    mask=cv2.inRange(imgHSV, lower, upper)
    x,y,w,h=getContours(mask)
    cv2.rectangle(normal,(x,y),(w,h),(11,0,101),3)
    cv2.imshow("video", normal)
    #cv2.imshow("hsvVideo", imgHSV)
    #cv2.imshow("maskVideo",mask)
    if  cv2.waitKey(1) & 0xFF==ord("q"):
        break