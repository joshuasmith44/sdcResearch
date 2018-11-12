from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

annotation = Element('annotation')
folder = SubElement(annotation, 'folder')
folder.text = 'captures_vlc'
filename = SubElement(annotation, 'filename')
filename.text = 'scene00601.png'
path = SubElement(annotation, 'path')
path.text = '/Users/chansungpark/Documents/captures_vlc/scene00601.png'
source = SubElement(annotation, 'source')
database = SubElement(source, 'database')
database.text = 'Unknown'
size = SubElement(annotation, 'size')
width = SubElement(size, 'width')
width.text = '1920'
height = SubElement(size, 'height')
height.text = '1090'
depth = SubElement(size, 'depth')
depth.text = '3'
segmented = SubElement(annotation, 'segmented')
segmented.text = '0'
object = SubElement(annotation, 'object')
objectName = SubElement(object, 'name')
objectName.text = 'ball'
objectPose = SubElement(object, 'pose')
objectPose.text = 'Unspecified'
objectTruncated = SubElement(object, 'truncated')
objectTruncated.text = '0'
objectDifficult = SubElement(object, 'difficult')
objectDifficult.text = '0'
objectBndbox = SubElement(object, 'bndbox')
objectMinX = SubElement(objectBndbox, 'xmin')
objectMinX.text = '1012'
objectMinY = SubElement(objectBndbox, 'ymin')
objectMinY.text = '772'
objectMaxX = SubElement(objectBndbox, 'xmax')
objectMaxX.text = '1123'
objectMaxY = SubElement(objectBndbox, 'ymax')
objectMaxY.text = '884'

myfile = open("soccerXmlCopy.xml", "w")
myfile.write(prettify(annotation))
