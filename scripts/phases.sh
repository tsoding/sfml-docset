cleanSfml() {
    # Assumptions
    test -d './SFML/'
    type git

    # Script
    rm -rf './SFML.docset/'
    rm -f './SFML.tgz'
    pushd './SFML/'
    git reset --hard
    git clean -fdx
    popd
}

patchSfml() {
    # Assumptions
    test -f './patches/enable-docset.patch'
    test -f './SFML/doc/doxyfile.in'
    type git

    # Script
    pushd './SFML/'
    git apply --check '../patches/enable-docset.patch'
    git apply '../patches/enable-docset.patch'
    popd
}

buildSfml() {
    # Assumptions
    test -d './SFML/'
    test ! -e './SFML/build/'
    type cmake

    # Script
    mkdir -p './SFML/build/'
    pushd './SFML/build/'
    cmake -DSFML_BUILD_DOC=TRUE ..
    make -j5
    popd
}

generateDocset() {
    # Assumptions
    test ! -e './SFML.docset/'
    test ! -e './SFML.tgz'
    test -d './SFML/build/doc/html/'
    test -f './resources/Info.plist'
    test -f './resources/icon.png'
    type sqlite3

    # Script
    mkdir -p './SFML.docset/Contents/Resources/'
    cp -rv \
       './SFML/build/doc/html/' \
       './SFML.docset/Contents/Resources/Documents'
    cp -v \
       './resources/Info.plist' \
       './SFML.docset/Contents/'
    cp -v \
       './resources/icon.png' \
       './SFML.docset/'
}

populateDocsetIndex() {
    # Assumptions
    test -d './SFML.docset/Contents/Resources/'
    test -f './SFML.docset/Contents/Resources/Documents/classes.htm'
    test ! -e './SFML.docset/Contents/Resources/docSet.dsidx'
    test -f './scripts/extract_classes.py'
    type sqlite3

    sqlite3 './SFML.docset/Contents/Resources/docSet.dsidx' <<EOF
CREATE TABLE searchIndex(
  id INTEGER PRIMARY KEY, 
  name TEXT, 
  type TEXT, 
  path TEXT
);
CREATE UNIQUE INDEX anchor ON searchIndex (name, type, path);
EOF
    ./scripts/extract_classes.py './SFML/build/doc/xml/index.xml' |
        sqlite3 './SFML.docset/Contents/Resources/docSet.dsidx'
}

archiveDocset() {
    # Assumptions
    test -d './SFML.docset/'
    type tar

    # Script
    tar fvcz SFML.tgz SFML.docset
}
