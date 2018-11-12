import cv2
import numpy as np

image1 = cv2.imread('testImages/beachBright.jpeg', cv2.IMREAD_COLOR)
image2 = cv2.imread('testImages/medBeach.jpeg', cv2.IMREAD_COLOR)
image3 = cv2.imread('testImages/darkBeach.jpeg', cv2.IMREAD_COLOR)

image1Total = (0.2162 * np.sum(image1[:,:,0])) + (0.7152 * np.sum(image1[:,:,1])) + (0.0722 * np.sum(image1[:,:,2]))
image2Total = (0.2162 * np.sum(image2[:,:,0])) + (0.7152 * np.sum(image2[:,:,1])) + (0.0722 * np.sum(image2[:,:,2]))
image3Total = (0.2162 * np.sum(image3[:,:,0])) + (0.7152 * np.sum(image3[:,:,1])) + (0.0722 * np.sum(image3[:,:,2]))

image1Average = image1Total/(image1.shape[0] * image1.shape[1])
image2Average = image2Total/(image2.shape[0] * image2.shape[1])
image3Average = image3Total/(image3.shape[0] * image3.shape[1])
print("Bright Beach Total: " + str(image1Average))
print("Medium Beach Total: " + str(image2Average))
print("Dark Beach Total: " + str(image3Average))
