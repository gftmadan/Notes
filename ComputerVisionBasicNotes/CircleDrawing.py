import cv2

img1 = cv2.imread("E:\ComputerVision\Working Data\Input Data\graf1.png")

'''
cv2.circle Link:-https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html#gaf10604b069374903dbd0f0488cb43670
'''

'''cv2.circle(img1,(350,350),50,(0,0,0),3)
cv2.imshow("Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

cv2.circle(img1,(350,350),50,(0,0,0),-11)
cv2.imshow("Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
#ANy negetive value will fill the circle