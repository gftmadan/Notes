import cv2

img1 = cv2.imread("E:\ComputerVision\Working Data\Input Data\graf1.png")
def nothing(val):
    pass
cv2.namedWindow("Window1",cv2.WINDOW_NORMAL)

cv2.createTrackbar("R","Window1",0,255,nothing)


fg=0
while True:
    cv2.imshow("Window1",img1)
    k = cv2.waitKey(1) & 0xFF
    r = cv2.getTrackbarPos("R","Window1")
    print(r)
    #print(fg)
    #fg +=1

cv2.destroyAllWindows()