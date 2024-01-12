import cv2
import numpy as np

color1 = np.zeros((600,600,3),dtype=np.uint8)
#img1[150:450,150:450] = [255,255,255]

color1[0:300,0:200] = (190,190,190)
color1[0:300,200:400] = (0,0,255)
color1[0:300,400:] = (178,255,102)
color1[300:,0:200] = (0,0,0)
color1[300:,200:400] = (255,0,0)
color1[300:,400:] = (255,0,255)

msk = np.zeros((600,600,3),dtype=np.uint8)
msk[:,200:400] = (255,255,255)
msk = cv2.cvtColor(msk,cv2.COLOR_BGR2GRAY)
ret,msk = cv2.threshold(msk,125,255,cv2.THRESH_BINARY)
'''
Bitwise AND:-
In Mask the pixel value of the image is displayed when the corresponding pixel in nmask is non-zero,
else it will output 0 
'''
btA = cv2.bitwise_and(color1,color1,mask=msk)


btO = cv2.bitwise_or(color1,color1,mask=msk)


btN = cv2.bitwise_not(color1,mask=msk)


btX = cv2.bitwise_xor(color1,color1,mask=msk)


cv2.imshow("Image1",color1)
cv2.imshow("Mask",msk)
cv2.imshow("Bitwise",btN)
cv2.waitKey(0)
cv2.destroyAllWindows()