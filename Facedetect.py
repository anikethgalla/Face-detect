import cv2
import play

image=cv2.imread("astro.jpg")
#import xml file and reading xml file usign cascade classifier
haarcascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
#detecting face(only frontal face)
faced=haarcascade.detectMultiScale(image,1.05,4)
print(faced)

for x,y,w,h in faced:
  #creating a rectangle
  cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imwrite("ouptu.png",image)
