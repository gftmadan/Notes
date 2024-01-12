import cv2
import numpy as np

img1 = np.zeros((600,600,3),dtype=np.uint8)

def trackbar_callback(val):
    R = cv2.getTrackbarPos("R","Window1")
    G = cv2.getTrackbarPos("G","Window1")
    B = cv2.getTrackbarPos("B","Window1")
    img1[:,:] = [B,G,R]
    cv2.imshow("Window1",img1)

cv2.namedWindow("Window1",cv2.WINDOW_NORMAL)
cv2.createTrackbar("R","Window1",0,255,trackbar_callback)
cv2.createTrackbar("G","Window1",0,255,trackbar_callback)
cv2.createTrackbar("B","Window1",0,255,trackbar_callback)
cv2.imshow("Window1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()


