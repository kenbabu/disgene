import os 
from  xml.etree.ElementTree import ElementTree
from  xml.etree.ElementTree import Element
import xml.etree.ElementTree as et

base_path = os.path.dirname(os.path.realpath(__file__))

xml_file = os.path.join(base_path, 'data/request.xml')


root= Element("requests")
tree= ElementTree(root)
toppfun = Element("toppfun")
enrichment = Element("enrichment-config")
trainingset= Element("trainingset")
gene = Element("gene")
features = Element("features")
feature = Element("feature")

