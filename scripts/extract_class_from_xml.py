#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import xml.etree.ElementTree as ET

class XMLClassExtracter:
    def __init__(self, indexXmlFileName):
        self.root = ET.parse(indexXmlFileName).getroot()

    def __dump_class_insert(self, child):
        name = child.find('name').text
        refid = child.attrib['refid']
        path = "%s.htm" % (refid)

        print ("INSERT INTO searchIndex (name, type, path) "
               "VALUES ('%s', 'Class', '%s');") % (name, path)

    def dump_as_sqlite_script(self):
        for child in self.root:
            if child.attrib['kind'] == 'class':
                self.__dump_class_insert(child)

if __name__ == "__main__":
    XMLClassExtracter("SFML/build/doc/xml/index.xml").dump_as_sqlite_script()
