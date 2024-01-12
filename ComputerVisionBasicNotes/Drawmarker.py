import cv2

img1 = cv2.imread(r"E:\ComputerVision\Working Data\Input Data\graf1.png")
imgh = img1.shape[0]
imgw = img1.shape[1]
'''
cv2.drawMarker Link:-https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html#ga644c4a170d4799a56b29f864ce984b7e
'''

'''cv2.drawMarker(img1,(imgw//2,imgh//2),(0,0,255),thickness=3)
cv2.imshow("Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

'''cv2.drawMarker(img1,(imgw//2,imgh//2),(0,0,255),markerSize=50,thickness=3)
cv2.imshow("Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#MARKER Flags:-https://docs.opencv.org/4.x/d6/d6e/group__imgproc__draw.html#ga0ad87faebef1039ec957737ecc633b7b
#markersize increses the size of the overall marker
#thicker increases the bluckiness of the overall marker

'''cv2.drawMarker(img1,(imgw//2,imgh//2),(0,0,255),cv2.MARKER_TRIANGLE_UP,50,3)
cv2.imshow("Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()'''

#-negetive sign in markersize rotates the marker in opposit direction

cv2.drawMarker(img1,(imgw//2,imgh//2),(0,0,255),cv2.MARKER_TRIANGLE_UP,-50,3)
cv2.imshow("Image",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()