import xml.etree.ElementTree as ET
import os, os.path, sys
import glob

ns = {'default':'http://cyclonedx.org/schema/bom/1.3'}
files = glob.glob("./bom*.xml")
tree = ET.parse(files[0])
rootElems = []
for fil in files[1:]:
    rootElems.extend(ET.parse(fil).getroot().find('default:components',ns).findall('default:component',ns))
for element in rootElems:
    tree.getroot().find('default:components',ns).append(element)
tree.write("./finalBom.xml")
strfile= ""
with open("./finalBom.xml") as file:
    strfile = file.read().replace("ns0:","")
with open("./finalBom.xml","w") as file:
    file.write(strfile)
print("Finished Merging SBOMs.")
