#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import xml.etree.ElementTree as ET

def dump_one_entry(name, kind, path):
    print ("INSERT INTO searchIndex (name, type, path) "
           "VALUES ('%s', '%s', '%s');") % (name, kind, path)

def dump_entries(entries):
    for (name, kind, path) in entries:
        dump_one_entry(name, kind, path)


class XmlExtracter(object):
    def __init__(self, indexXmlFile):
        self.xmlRoot = ET.parse(indexXmlFile).getroot()

class XmlClassExtracter(XmlExtracter):
    def __init__(self, xmlRoot):
        super(XmlClassExtracter, self).__init__(xmlRoot)

    def __class_to_entry(self, child):
        name = child.find('name').text
        refid = child.attrib['refid']
        path = "%s.htm" % (refid)
        return (name, 'Class', path)

    def dump_as_sqlite_script(self):
        dump_entries([self.__class_to_entry(child)
                      for child in self.xmlRoot
                      if child.attrib['kind'] == 'class'])

def print_usage():
    print "Usage: extract_class_from_xml.py <path-to-index.xml>"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please provide path to the index.xml file"
        print_usage()
        exit(1)

    indexXmlFile = sys.argv[1]
    XmlClassExtracter(indexXmlFile).dump_as_sqlite_script()
