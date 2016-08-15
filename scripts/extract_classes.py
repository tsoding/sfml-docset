#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from HTMLParser import HTMLParser

class HTMLClassExtracter(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.classes = []
        self.current_class = None

    def handle_starttag(self, tag, attrs):
        dattrs = dict(attrs)
        if tag == 'a' and dattrs.get('class') == 'el':
            self.current_class = dattrs['href']

    def handle_endtag(self, tag):
        if tag == 'a' and self.current_class is not None:
            self.current_class = None

    def handle_data(self, data):
        if self.current_class is not None:
            self.classes.append((data, self.current_class))

    def print_classes(self):
        print self.classes

    def dump_to_sqite_db(self, c):
        c.executemany("INSERT INTO searchIndex (name, type, path) VALUES (?, 'Class', ?)", self.classes)

    def dump_as_sqlite_sql(self):
        for (name, t) in self.classes:
            print "INSERT INTO searchIndex (name, type, path) VALUES ('%s', 'Class', '%s');" % (name, t)

def print_usage():
    print "Usage: extract_classes.py <path-to-classes.htm>"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please provide path to the classes.htm file"
        print_usage()
        exit(1)

    classes_file = sys.argv[1]

    parser = HTMLClassExtracter()

    with open(classes_file) as f:
        parser.feed(f.read())

    parser.dump_as_sqlite_sql()
