import cv2
import numpy as np

cap = cv2.VideoCapture('testVids/sunset.mp4')
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
#out = cv2.VideoWriter('outVids/sunsetLabeled.mp4', -1, 20.0, (1280,720))
while cap.isOpened():
    ret, im = cap.read()
    print(ret)
    if not ret:
        break
    imTotal = (0.0722 * np.sum(im[:,:,0])) + (0.7152 * np.sum(im[:,:,1])) + (0.2162 * np.sum(im[:,:,2]))
    #imTotal = np.sum(cv2.cvtColor(im, cv2.COLOR_BGR2HSV)[::2])
    imTotal = 0
    imAverage = imTotal/(im.shape[0] * im.shape[1] * 100)
    numLabel = ("%.1f" % (imAverage * 100)) + '%'
    cv2.putText(im, numLabel , (900, 100), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), lineType=cv2.LINE_AA)
    cv2.imshow('display', im)
    #out.write(im)
cap.release()
cv2.destroyAllWindows()
#out.release()
