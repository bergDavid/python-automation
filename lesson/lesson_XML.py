#Web Service XML/JSON
import xml.etree.ElementTree as ET
data = '''<person>
<name>Chuck</name>
<phone type="int">
+1 734 303 4456
</phone>
<email hide="yes"/>
</person>'''
tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
lst = data.findall('person/person')
for item in lst:
    print("Name", item.find('name').text)