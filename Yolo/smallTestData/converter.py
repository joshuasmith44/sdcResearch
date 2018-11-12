import json, io, glob
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
data_dir = '/Users/joshuasmith/Downloads/bdd100kAnnotations/labels/bdd100k_labels_images_train.json'
output_dir = '/Users/joshuasmith/Desktop/annotationOutputTest/'
image_dir = 'wack'


def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

with open(data_dir) as data_file:
    myData = json.load(data_file)
i = 0
for image in myData:
    i += 1
    print i
    annotation = Element('annotation')
    folder = SubElement(annotation, 'folder')
    folder.text = 'image_folder'
    filename = SubElement(annotation, 'filename')
    filename.text = image['name']
    path = SubElement(annotation, 'path')
    path.text = image_dir + image['name']
    source = SubElement(annotation, 'source')
    database = SubElement(source, 'database')
    database.text = 'BerkeleyDeepDrive100KImages'
    size = SubElement(annotation, 'size')
    width = SubElement(size, 'width')
    width.text = '1280'
    height = SubElement(size, 'height')
    height.text = '720'
    depth = SubElement(size, 'depth')
    depth.text = '3'
    segmented = SubElement(annotation, 'segmented')
    segmented.text = '0'
    for thing in image['labels']:
        if(thing['category'] == 'drivable area' or thing['category'] == 'lane'):
            break
        object = SubElement(annotation, 'object')
        objectName = SubElement(object, 'name')
        objectName.text = thing['category']
        objectPose = SubElement(object, 'pose')
        objectPose.text = 'Unspecified'
        objectTruncated = SubElement(object, 'truncated')
        if thing['attributes']['truncated'] == False:
            objectTruncated.text = '0'
        else:
            objectTruncated.text = '1'
        objectDifficult = SubElement(object, 'difficult')
        objectDifficult.text = '0'
        objectBndbox = SubElement(object, 'bndbox')
        objectMinX = SubElement(objectBndbox, 'xmin')
        objectMinX.text = str(thing['box2d']['x1'])
        objectMinY = SubElement(objectBndbox, 'ymin')
        objectMinY.text = str(thing['box2d']['y1'])
        objectMaxX = SubElement(objectBndbox, 'xmax')
        objectMaxX.text = str(thing['box2d']['x2'])
        objectMaxY = SubElement(objectBndbox, 'ymax')
        objectMaxY.text = str(thing['box2d']['y2'])
    output_file = open( output_dir + str(image['name'][0:-4]) + '.xml', 'w')
    output_file.write(prettify(annotation))
