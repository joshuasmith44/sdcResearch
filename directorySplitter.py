import os, glob
from random import shuffle
data_dir = '/Users/joshuasmith/Desktop/annotationOutputTest/'
image_dir1 = '/Users/joshuasmith/Desktop/BDDXmlData/Training/'
image_dir2 = '/Users/joshuasmith/Desktop/BDDXmlData/Testing/'
myFilenames = glob.glob('/Users/joshuasmith/Desktop/annotationOutputTest/*.xml')

shuffle(myFilenames)
filenameLen = len(myFilenames)

dir1 = myFilenames[0:filenameLen/2]
dir2 = myFilenames[filenameLen/2: filenameLen]
i = 0
for filename in dir1:
    i += 1
    os.rename(filename, image_dir1 + filename[len(data_dir):])
g = 0
for filename in dir2:
    g += 1
    os.rename(filename, image_dir2 + filename[len(data_dir):])
print i
print g
