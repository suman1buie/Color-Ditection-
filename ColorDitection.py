import  cv2
import numpy as np
import stack

# path = 'recourse/lambo.PNG'
vdo = cv2.VideoCapture(0)

def empty(q):
    pass

cv2.namedWindow("trackbar")
cv2.resizeWindow("trackbar",640,240)

cv2.createTrackbar("Hue Min","trackbar",0,179,empty)
cv2.createTrackbar("Hue Max","trackbar",179,179,empty)
cv2.createTrackbar("Sat Min","trackbar",0,255,empty)
cv2.createTrackbar("Sat Max","trackbar",255,255,empty)
cv2.createTrackbar("Val Min","trackbar",0,255,empty)
cv2.createTrackbar("Val Max","trackbar",255,255,empty)

while True:
    # img = cv2.imread(path)
    ssce,img = vdo.read()
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","trackbar")
    h_max = cv2.getTrackbarPos("Hue Max","trackbar")
    s_min = cv2.getTrackbarPos("Sat Min","trackbar")
    s_max = cv2.getTrackbarPos("Sat Max","trackbar")
    v_min = cv2.getTrackbarPos("Val Min","trackbar")
    v_max = cv2.getTrackbarPos("Val Max","trackbar")
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imgHSV,lower,upper)
    imgR = cv2.bitwise_and(img,img,mask=mask)
    print(lower,upper)
    # imageAll = stack.stackImages(0.6,([img,mask],[imgHSV,imgR]))
    # imageAllr = cv2.resize(imageAll,(620,510))
    # cv2.imshow("fream",img)
    # cv2.imshow("HSV",imgHSV)
    cv2.imshow("mask",mask)
    # cv2.imshow("result",imageAllr)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break