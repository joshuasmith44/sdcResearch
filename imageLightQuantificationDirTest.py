import cv2
import numpy as np
import glob

for filename in glob.glob('testImageDir/*.jpeg'):
    im = cv2.imread(filename, cv2.IMREAD_COLOR)
    imTotal = (0.2162 * np.sum(im[:,:,0])) + (0.7152 * np.sum(im[:,:,1])) + (0.0722 * np.sum(im[:,:,2]))
    imAverage = imTotal/(im.shape[0] * im.shape[1])
    print(filename + " average: " + str(imAverage))
