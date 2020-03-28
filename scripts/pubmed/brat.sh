#!/bin/bash

cwd=$(pwd)
projectFolder=$cwd
pubmedFolder=$projectFolder/corpus/pubmed
bratFolder=$pubmedFolder/brat

echo "Clean brat folder..."
rm -rf "$bratFolder"
echo "Create brat folder..."
mkdir "$bratFolder"
echo "Copy text files..."
for i in "$pubmedFolder"/raw/*.txt; do cp "$i" "$bratFolder"; done
echo "Copy annotation files..."
for i in "$pubmedFolder"/annotations/*.a1; do cp "$i" "$bratFolder"; done
echo "Copy brat configuration files..."
cp "$projectFolder"/config/brat/*.conf "$bratFolder"
echo "Done."
