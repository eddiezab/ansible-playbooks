#!/bin/bash

find ./ -name \*.yml -a ! -regex '.*/skel/.*' -empty -exec bash -c 'echo -en "---\n\n# file: ${1/.\//}\n\n" > $1 ' {} {} \;
