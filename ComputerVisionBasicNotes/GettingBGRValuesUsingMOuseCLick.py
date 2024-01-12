import cv2
import numpy as np

img = np.zeros((600,600,3))

#Giving White Color
img[0:300,0:200] = [255,255,255]
#Giving Red Color
img[0:300,200:400] = [0,0,255]
#Giving Green Color
img[0:300,400:] = [0,255,0]
#Giving Blue Color
img[300:,200:400] = [255,0,0]
#Giving Yellow Color
img[300:,400:] = [255,255,0]

#we used y,x to get BGR value bcoz in array its hieght,width,colorchannel and x=width,y=height
def callback(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        b = img[y,x,0]
        g = img[y,x,1]
        r = img[y,x,2]
        print(f"BGR:-({b},{g},{r}")

cv2.imshow("image",img)
cv2.setMouseCallback("image",callback)
cv2.waitKey(0)
cv2.destroyAllWindows()