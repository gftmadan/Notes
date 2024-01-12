import cv2

'''
cv2.subtract Link:-https://docs.opencv.org/3.4/d2/de8/group__core__array.html#gaa0f00d98b4b5edeaeb7b8333b2de353b
We can see that the order ofg imaages subtracted matters
'''
img1 = cv2.imread("E:\ComputerVision\Working Data\Input Data\\aloeL.jpg")
img1 = cv2.resize(img1,(600,600))

img2 = cv2.imread("E:\ComputerVision\Working Data\Input Data\graf1.png")
img2 = cv2.resize(img2,(600,600))

sub1 = cv2.subtract(img1,img2)
sub2 = cv2.subtract(img2,img1)

cv2.imshow("Image",img1)
cv2.imshow("Image",img2)
cv2.imshow("Subtraction1",sub1)
cv2.imshow("Subtrcation2",sub2)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Image Subtracting can be used for  Background Removal