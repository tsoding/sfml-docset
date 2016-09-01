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

def node_to_entry(node, kind, path_ending):
    name = node.find('name').text
    refid = node.attrib['refid']
    path = "%s%s" % (refid, path_ending)
    return (name, kind, path)

def dump_sqlite_index_script(node, xml_kind, docset_kind, path_ending):
    dump_entries([node_to_entry(child, docset_kind, path_ending)
                  for child in node
                  if child.attrib['kind'] == xml_kind])

def print_usage():
    print "Usage: extract_class_from_xml.py <path-to-index.xml>"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please provide path to the index.xml file"
        print_usage()
        exit(1)

    entities = [
        ('class', 'Class', '.htm'),
        ('struct', 'Struct', '.htm'),
        ('file', 'File', '_source.htm')
    ]

    index_xml_file = sys.argv[1]
    xml_root = ET.parse(index_xml_file).getroot()

    print "BEGIN TRANSACTION;"
    for (xml_kind, docset_kind, file_ending) in entities:
        dump_sqlite_index_script(xml_root, xml_kind, docset_kind, file_ending)
    print "COMMIT TRANSACTION;"
