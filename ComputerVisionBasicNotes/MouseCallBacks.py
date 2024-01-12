import cv2

img1 = cv2.imread(r"E:\ComputerVision\Working Data\Input Data\graf1.png")

'''
structure link of mousecallback func:-https://docs.opencv.org/4.x/d7/dfc/group__highgui.html#gab7aed186e151d5222ef97192912127a4
EVENT_MOUSECALLBACKS flags:-https://docs.opencv.org/4.x/d0/d90/group__highgui__window__flags.html#ga927593befdddc7e7013602bca9b079b0
'''



#Studying the events and its activations accroding to the left mouse botton events
'''
def mousecallbackLMouse(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Pressed{x},{y}")
    if event == cv2.EVENT_LBUTTONUP:
        print(f"Released{x},{y}")
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f"DoubleClicked{x},{y}")
'''

##Studying the events and its activations accroding to the right mouse botton events
'''
def mousecallbackRMouse(event,x,y,flags,params):
    if event == cv2.EVENT_RBUTTONDOWN:
        print(f"PressedR {x},{y}")
    if event == cv2.EVENT_RBUTTONUP:
        print(f"ReleasedR {x},{y}")
    if event == cv2.EVENT_RBUTTONDBLCLK:
        print(f"DoubleClickR {x},{y}")
'''
##Studying the Events and its activation according to middle mouse button events
'''
def mousecallbackMMouse(event,x,y,flags,params):
    if event == cv2.EVENT_MBUTTONDOWN:
        print(f"PressedM{x},{y}")
    if event == cv2.EVENT_MBUTTONUP:
        print(f"ReleasedM{x},{y}")
    if event == cv2.EVENT_MBUTTONDBLCLK:
        print(f"DoubleClickedM{x},{y}")
    if event == cv2.EVENT_MOUSEWHEEL:
        print(flags)
        print(f"MouseWheel{x}.{y}")
'''
#Flag tell us that whether its was uo scrool or down scroll of mouse wheel
#Positive value means UP scroll and negetive value means Backward scroll

#Commmobing All Together

def callback(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"PressedL{x},{y}")
    if event == cv2.EVENT_LBUTTONUP:
        print(f"ReleasedL{x},{y}")
    if event == cv2.EVENT_LBUTTONDBLCLK:
        print(f"DoubleClickedL{x},{y}")
    if event == cv2.EVENT_RBUTTONDOWN:
        print(f"PressedR {x},{y}")
    if event == cv2.EVENT_RBUTTONUP:
        print(f"ReleasedR {x},{y}")
    if event == cv2.EVENT_RBUTTONDBLCLK:
        print(f"DoubleClickR {x},{y}")
    if event == cv2.EVENT_MBUTTONDOWN:
        print(f"PressedM{x},{y}")
    if event == cv2.EVENT_MBUTTONUP:
        print(f"ReleasedM{x},{y}")
    if event == cv2.EVENT_MBUTTONDBLCLK:0
        print(f"DoubleClickedM{x},{y}")
    if event == cv2.EVENT_MOUSEWHEEL:
        print(flags)
        print(f"MouseWheel{x}.{y}")


cv2.imshow("image",img1)
cv2.setMouseCallback("image",callback)
cv2.waitKey(0)
cv2.destroyAllWindows()