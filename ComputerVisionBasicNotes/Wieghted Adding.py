import cv2

#cv2.addWeighted Link:-https://docs.opencv.org/4.x/d2/de8/group__core__array.html#gafafb2513349db3bcff51f54ee5592a19


img1 = cv2.imread("E:\ComputerVision\Working Data\Input Data\messi5.jpg")
img1 = cv2.resize(img1,(600,600))
img2 = cv2.imread("E:\ComputerVision\Working Data\Input Data\opencv-logo-white.png")
img2 = cv2.resize(img2,(600,600))
add1 = cv2.add(img1,img2)

'''
alpha,beta,gamma forms the fraction between 0-1
it can have values more than 1 also nut it will increse that respectiver image saturation
gamma higher value increses the brightness
normal add eqauls then aplha=1,beta=1,gamma=0
'''

addwieght = cv2.addWeighted(img1,0.8,img2,0.2,0)
addwieght1 = cv2.addWeighted(img1,0.5,img2,0.5,0)
addwieght2 = cv2.addWeighted(img1,0,img2,0,0)
addwieght3 = cv2.addWeighted(img1,1,img2,1,0)
addwieght4 = cv2.addWeighted(img1,2,img2,1,0)
addwieght5 = cv2.addWeighted(img1,0.8,img2,0.2,100)
addwieght6 = cv2.addWeighted(img1,10,img2,1,0)


cv2.imshow("Added",add1)
cv2.imshow("AddedWeights",addwieght)
cv2.imshow("AddedWeights1",addwieght1)
cv2.imshow("AddedWeights2",addwieght2)
cv2.imshow("AddedWeights3",addwieght3)
cv2.imshow("AddedWeights4",addwieght4)
cv2.imshow("AddedWeights5",addwieght5)
cv2.imshow("AddedWeights6",addwieght6)
cv2.waitKey(0)
cv2.destroyAllWindows()