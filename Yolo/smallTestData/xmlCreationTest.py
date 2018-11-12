from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.dom import minidom
def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

top = Element('top')
#comment = Comment('Heyo this is a test')
#top.append(comment)

child = SubElement(top, 'middle')
child.text = 'this child has text'

low = SubElement(child, 'bottom')
low.text = 'yeet'

print prettify(top)
