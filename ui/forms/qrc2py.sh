#!/bin/bash

# adapted from MediMorph Project
# Thanks guys !!! Awesome script !!!

# Converts all .qrc files in current directory into .py files
for d in `ls *.qrc`; do
  pyrcc4 $d -o "`echo $d | perl -pe 's/\\.[^.]+$//' `_rc.py"
done
