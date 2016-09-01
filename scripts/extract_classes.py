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

def print_usage():
    print "Usage: extract_class_from_xml.py <path-to-index.xml>"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please provide path to the index.xml file"
        print_usage()
        exit(1)

    index_file = sys.argv[1]
    XMLClassExtracter(index_file).dump_as_sqlite_script()
