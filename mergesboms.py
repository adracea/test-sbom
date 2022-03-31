import xml.etree.ElementTree as ET
import os, os.path, sys
import glob

ns = {'default':'http://cyclonedx.org/schema/bom/1.3'}
files = glob.glob("./bom*.xml")
print("Found the following files:")
print(files)
tree = ET.parse(files[0])
rootComps = []
rootTools = []
rootMetaComps = []
for fil in files[1:]:
    root1 = ET.parse(fil).getroot().find('default:components',ns).findall('default:component',ns)
    root2 = ET.parse(fil).getroot().find('default:metadata',ns).find('default:tools',ns).findall('default:tool',ns)
    root3 = ET.parse(fil).getroot().find('default:metadata',ns).findall('default:component',ns)
    rootComps.extend(root1)
    rootTools.extend(root2)
    rootMetaComps.extend(root3)
for element in rootComps:
    tree.getroot().find('default:components',ns).append(element)
for element in rootTools:
    tree.getroot().find('default:metadata',ns).find('default:tools',ns).append(element)
for element in rootMetaComps:
    tree.getroot().find('default:metadata',ns).append(element)
tree.write("./finalBom.xml")
strfile= ""
with open("./finalBom.xml") as file:
    strfile = file.read().replace("ns0:","").replace(":ns0","")
    strfile = '<?xml version="1.0" encoding="UTF-8"?>' + strfile
with open("./finalBom.xml","w") as file:
    file.write(strfile)
print("Finished merging SBOMs.")
