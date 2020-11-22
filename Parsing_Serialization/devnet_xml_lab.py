from xml.dom import minidom

with open('pool.xml', 'r') as f:
    xmlString = f.read()

dom = minidom.parseString(xmlString)
xml = dom.toprettyxml()
print(xml)

doc = minidom.parse('pool.xml')
print(type(doc))