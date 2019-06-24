#!/usr/bin/env python
# -*- coding: utf-8 -*-

from xml.etree.ElementTree import parse, Element

doc = parse('pred.xml')
root = doc.getroot()
print(root)

root.remove(root.find('sri'))
root.remove(root.find('cr'))

# print(root.getchildren().index(root.find('nm')))
e = Element('spam')
e.text = 'This is a test'
root.insert(2, e)

doc.write('newpred.xml', xml_declaration=True)