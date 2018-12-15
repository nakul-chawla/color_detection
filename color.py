# coding: utf-8
# In[22]:
import cv2
import numpy as np
cam=cv2.VideoCapture(0)
fname='C://home//MachineLearn//Python//OpenCV//Output//Outputname.avi'
codec=cv2.VideoWriter_fourcc('X','V','I','D')
fps=35
res=(640,480)
VideoOut=cv2.VideoWriter(fname,codec,fps,res)
while (1):
_,im=cam.read()
hsv=cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
green_light=np.array([65, 50, 50],np.uint8)
green_dark=np.array([77,255,255],np.uint8)
blue_light=np.array([85,150,150],np.uint8)
blue_dark=np.array([110,255,255],np.uint8)
red_light=np.array([165,87,111],np.uint8)
red_dark=np.array([180,255,255],np.uint8)
red=cv2.inRange(hsv,red_light,red_dark)
blue=cv2.inRange(hsv,blue_light,blue_dark)
yellow=cv2.inRange(hsv,yellow_light,yellow_dark)
green=cv2.inRange(hsv,green_light,green_dark)
kernel=np.ones((15,15),"uint8")
red=cv2.dilate(red,kernel)
res_red = cv2.bitwise_and(im,im, mask=red)
blue=cv2.dilate(blue,kernel)
res_blue = cv2.bitwise_and(im,im, mask=blue)
green=cv2.dilate(green,kernel)
res_green = cv2.bitwise_and(im,im, mask=green)
(_,contours,hierarchy)=cv2.findContours(green,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for _,contour in enumerate(contours):
area=cv2.contourArea(contour)
if area>300:
x,y,w,h=cv2.boundingRect(contour)
cnt=contours[len(contours)-1]
cv2.drawContours(im,cnt,-1,(0,255,0),5)
cv2.putText(im,"Green",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0))(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for _,contour in enumerate(contours):
area=cv2.contourArea(contour)
if area>300:
x,y,w,h=cv2.boundingRect(contour)
cnt=contours[len(contours)-1]
cv2.drawContours(im,cnt,-1,(0,0,255),5)
cv2.putText(im,"Red",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,255))
(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
for _,contour in enumerate(contours):
area=cv2.contourArea(contour)
if area>300:
x,y,_,_=cv2.boundingRect(contour)
cnt=contours[len(contours)-1]
cv2.drawContours(im,cnt,-1,(255,0,0),5)
cv2.putText(im,"Blue",(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0))
VideoOut.write(im)
cv2.imshow("Tracker",im)
if 0xFF!= ord('q') or 0xFF!=ord('Q'):
break
VideoOut.release()
cam.release()
cv2.destroyAllWindows()
