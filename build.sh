#!/usr/bin/env sh

set -ex

cleanSfml() {
    # Assumptions
    test -d './SFML/'
    type git

    # Script
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
    type cmake

    # Script
    mkdir -p './SFML/build/'
    pushd './SFML/build/'
    cmake -DSFML_BUILD_DOC=TRUE ..
    make -j5
    popd
}

generateSfmlDocset() {
    echo "unimplemented"
    exit 1
}

cleanSfml
patchSfml
buildSfml
# generateSfmlDocset
