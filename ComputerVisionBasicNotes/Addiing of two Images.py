import cv2
import numpy as np
'''
cv2.add Link:-https://docs.opencv.org/4.x/d2/de8/group__core__array.html#ga10ac1bfb180e2cfda1701d06c24fdbd6
'''
'''img1 = cv2.imread("E:\ComputerVision\Working Data\Input Data\messi5.jpg")
img1 = cv2.resize(img1,(600,600))
img2 = cv2.imread("E:\ComputerVision\Working Data\Input Data\opencv-logo-white.png")
img2 = cv2.resize(img2,(600,600))
print(img1.shape)
print(img2.shape)
add1 = cv2.add(img1,img2)
add2 = cv2.add(img2,img1)



cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.imshow("Addition1",add1)
cv2.imshow("Addition2",add2)
cv2.waitKey(0)
cv2.destroyAllWindows()'''



'''
#Its add the two pixel values and then it saturates it .....
Saturation means - if any pixel value increases 255 then it clips back to 255
                   else it remains the pixels values unchanged  
WE CAN SEE IT IN THE BELOW EXAMPLE
'''
'''
img1 = np.zeros((600,600,3),dtype=np.uint8)
img2 = np.zeros((600,600,3),dtype=np.uint8)

img1[:,:] = (111,222,25)
img2[:,:] = (111,32,255)

img3 = cv2.add(img1,img2)
print(img3)
cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("image",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()'''


'''
Masking effects the same as it did in BITWISE OPeration
(First adding then saturating and displaying only those pixels tht have corresponding non-zero pixels values in the mask 
'''
img1 = cv2.imread("E:\ComputerVision\Working Data\Input Data\messi5.jpg")
img1 = cv2.resize(img1,(600,600))
img2 = cv2.imread("E:\ComputerVision\Working Data\Input Data\opencv-logo-white.png")
img2 = cv2.resize(img2,(600,600))

msk = np.zeros((600,600,3),dtype=np.uint8)
msk[:,200:400] = (255,255,255)
msk = cv2.cvtColor(msk,cv2.COLOR_BGR2GRAY)
ret,msk = cv2.threshold(msk,125,255,cv2.THRESH_BINARY)

img3 = cv2.add(img1,img2,mask=msk)

cv2.imshow("Image1",img1)
cv2.imshow("Image2",img2)
cv2.imshow("MaskedAddition",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()