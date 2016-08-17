#!/usr/bin/env sh

. './scripts/phases.sh'

set -ex

cleanSfml
patchSfml
buildSfml
generateSfmlDocset
