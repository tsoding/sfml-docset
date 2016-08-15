#!/usr/bin/env sh

set -ex

cleanSfml() {
    # Assumptions
    test -d './SFML/'
    which git

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
    which git

    # Script
    pushd './SFML/'
    git apply --check '../patches/enable-docset.patch'
    git apply '../patches/enable-docset.patch'
    popd
}

buildSfml() {
    echo "unimplemented"
    exit 1
}

generateSfmlDocset() {
    echo "unimplemented"
    exit 1
}

cleanSfml
patchSfml
buildSfml
generateSfmlDocset
