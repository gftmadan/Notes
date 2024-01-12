import cv2
import numpy as np


color1 = np.zeros((600,600,3),dtype=np.uint8)
color2 = np.zeros((600,600,3),dtype=np.uint8)

color1[0:300,0:200] = (190,190,190)
color1[0:300,200:400] = (0,0,255)
color1[0:300,400:] = (178,255,102)
color1[300:,0:200] = (0,0,0)
color1[300:,200:400] = (255,0,0)
color1[300:,400:] = (255,0,255)

color2[0:300,0:200] = (0,0,255)
color2[0:300,200:400] = (255,0,0)
color2[0:300,400:] = (0,0,0)
color2[300:,0:200] = (0,255,0)
color2[300:,200:400] = (255,255,255)
color2[300:,400:] = (0,255,255)

msk = np.zeros((600,600,3),dtype=np.uint8)
msk[:,200:400] = (255,255,255)
msk = cv2.cvtColor(msk,cv2.COLOR_BGR2GRAY)
ret,msk = cv2.threshold(msk,125,255,cv2.THRESH_BINARY)

#color1[0:600,0:600] = (11,215,102)
#color2[0:600,0:600] = (204,153,255)


btA = cv2.bitwise_and(color1,color1)
btO = cv2.bitwise_or(color1,color1)
btN = cv2.bitwise_not(color1)
btX = cv2.bitwise_xor(color1,color1)

mbtA = cv2.bitwise_and(color1,color1,mask=msk)
mbtO = cv2.bitwise_or(color1,color1,mask=msk)
mbtN = cv2.bitwise_not(color1,mask=msk)
mbtX = cv2.bitwise_xor(color1,color1,mask=msk)


cv2.imshow("Image",color1)
#cv2.imshow("Image1",color2)
cv2.imshow("BitwiseAnd",btA)
cv2.imshow("BitwiseOR",btO)
cv2.imshow("BitwiseNot",btN)
cv2.imshow("BitwiseXor",btX)


cv2.imshow("MaskedBitwiseAnd",mbtA)
cv2.imshow("MaskedBitwiseOR",mbtO)
cv2.imshow("MaskedBitwiseNot",mbtN)
cv2.imshow("MaskedBitwiseXor",mbtX)


cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Normall Working of BITWISE FUnctions in opencv is:-

1)Perform THe respective BITWISE Operation between the two source images and store in output
2)if Mask is not applied:(mask should be a binary image)
        then display the output image as it is.
  if Mask is applied:
        then display only those pixels(as it is) who corresponding pixel in mask is non-zero
        else display zero    
'''