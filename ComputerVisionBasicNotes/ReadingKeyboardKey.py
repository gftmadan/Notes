import cv2

img1 = cv2.imread("E:\ComputerVision\Working Data\Input Data\graf1.png")

cv2.imshow("Image1",img1)
key = 0

'''
print the key to see what will each key integer return value!
'''

# Printing only when a specfic key is present
while key != 115:
    cv2.imshow("Image1",img1)
    key = cv2.waitKey(0)