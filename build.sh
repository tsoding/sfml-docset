#!/usr/bin/env sh

. './scripts/phases.sh'

set -ex

cleanSfml

test ! -e ./SFML.tgz

patchSfml
buildSfml
generateDocset
populateDocsetIndex
archiveDocset

test -f ./SFML.tgz
